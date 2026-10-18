#!/usr/bin/env bash
# Run a plugin eval suite with the claude CLI, detached, writing its JSON result.
#
#   scripts/evals/run_eval.sh [--wait] <name> <out-json> [extra `claude plugin eval` flags...]
#
# <name>      names the run; it lives in
#             ${MANIFEST_DEV_EVAL_RUNS:-$HOME/.local/state/manifest-dev-evals}/<name>/<stamp>/
# <out-json>  result path, relative to claude-plugins/manifest-dev unless absolute, e.g.
#             evals/results/hillclimb-define/v2/aggregate-result.json
# --wait      waits for the run to end and exits with its status; the run still survives this
#             shell ending while it waits.
#
# Example, one case of a hill-climb round (plugin arm only, three runs; the suite README's
# *Hill-climbing a prompt against a suite* loops it over the climb set):
#   scripts/evals/run_eval.sh --wait hc-v2-d05 evals/results/hillclimb-define/v2/d05-conflicting-goals.json \
#     --case d05-conflicting-goals --tag define --ablation none --runs 3 --judge-model sonnet \
#     --scaffold --max-cost-usd 6
#
# The run evaluates a copy of claude-plugins/manifest-dev made in its own directory, outside this
# checkout, so the checkout can change while it runs. It starts `claude plugin eval` from that
# directory with no user settings and no MCP servers of yours (scripts/lib/claude-cli.sh has the
# flags), detached from this shell, so it keeps running after the shell that started it exits.
# Its run directory holds eval.log, which opens with the CLI version (recorded, not pinned), and
# exit-code, written when it ends. Exit 2 from the suite means --max-cost-usd stopped it with a
# partial result.
#
# Needs: the claude CLI on PATH and signed in, and python3; exits 3 without them. A suite is many
# sessions on your sign-in. On macOS each eval child may raise a keychain dialog (evals/README.md).
set -euo pipefail

usage() { sed -n '2,17p' "$0"; exit 2; }
die() { echo "run_eval: $*" >&2; exit 1; }

wait_for=0
if [[ ${1:-} == --wait ]]; then wait_for=1; shift; fi
[[ $# -ge 2 ]] || usage
name=$1 out=$2
shift 2
case $name in
  "" | */* | .*) echo "run_eval: the run name '$name' must be one plain word, with no / and no leading dot" >&2; exit 2 ;;
esac

root=$(git -C "$(dirname "$0")" rev-parse --show-toplevel)
root=$(cd "$root" && pwd -P)
# shellcheck source=../lib/claude-cli.sh
source "$root/scripts/lib/claude-cli.sh"
case $out in /*) ;; *) out=$root/claude-plugins/manifest-dev/$out ;; esac

claude_cli_ready run_eval

store=${MANIFEST_DEV_EVAL_RUNS:-$HOME/.local/state/manifest-dev-evals}
store=$(python3 -c 'import os, sys; print(os.path.realpath(sys.argv[1]))' "$store")
case $store/ in
  "$root"/*) die "the run store $store is inside this checkout, where the run could change it; set MANIFEST_DEV_EVAL_RUNS to a directory outside it" ;;
esac
mkdir -p "$store/$name" 2>/dev/null ||
  die "cannot create $store/$name; set MANIFEST_DEV_EVAL_RUNS to a writable directory outside this checkout"
run="$store/$name/$(date -u +%Y%m%dT%H%M%SZ)"
base=$run n=1
until mkdir "$run" 2>/dev/null; do
  [[ -e $run ]] || die "cannot create $run (is $store writable?)"
  n=$((n+1)); run="$base-$n"
done
mkdir -p "$(dirname "$out")" 2>/dev/null || die "cannot create the directory for $out; name a writable result path"

target=$(copy_plugin manifest-dev "$run")
log=$run/eval.log status_file=$run/exit-code
echo "CLI: $CLAUDE_CLI_VERSION" >"$log"

# setsid puts the run in a session of its own, so neither this shell ending nor its terminal
# closing stops it; exit-code is written by rename, so a reader never sees it half written.
cd "$run"
python3 -c 'import os, sys; os.setsid(); os.execvp(sys.argv[1], sys.argv[1:])' \
  bash -c 'log=$1 status=$2; shift 2; code=0; "$@" >>"$log" 2>&1 || code=$?
           echo "$code" >"$status.tmp" && mv "$status.tmp" "$status"' run_eval "$log" "$status_file" \
  "${CLAUDE_SESSION_ENV[@]}" claude "${CLAUDE_ISOLATION[@]}" plugin eval "$target" \
  --allow-tools Write Bash -j 8 --no-publish --trust-plugin --json "$out" "$@" \
  </dev/null >/dev/null 2>&1 &
pid=$!

echo "run_eval: started $name (pid $pid, $CLAUDE_CLI_VERSION); it keeps running if this shell exits"
echo "  log:    $log"
echo "  result: $out, written when the run ends; $status_file then holds its exit status"
echo "run_eval: a full suite is many sessions on your sign-in and counts against its usage limits" >&2
((wait_for == 1)) || exit 0

wait "$pid" || true
[[ -s $status_file ]] || die "the run ended without writing $status_file, so it was stopped from outside; read $log for how far it got"
code=$(<"$status_file")
if ((code != 0)); then
  echo "run_eval: $name exited $code; read $log for the cause (exit 2 is the cost ceiling stopping it with a partial result)" >&2
  exit "$code"
fi
echo "run_eval: $name finished; result: $out"
