# do

Executes a Manifest with full autonomy until every Acceptance Criterion and Global Invariant holds on fresh evidence, then reports what changed and the basis for each gate.

Status: unverified

## Sub-features

- `execute` — works toward every gate; judgment gates read the change once, then deltas
- `log` — append-only log at `~/.manifest-dev/logs/do-<name>-<hash>.md`; `--no-log` turns it off
- `amend` — changes the Manifest only through define
- `harvest` — turns corrections into locks and lists the debt it leaves
- `verification-surface` — builds or repairs the project's surface where the Manifest touches it
- `backstop` — arms a goal or prints a goal block so the run survives interruption

## How to get to it (user POV)

- `/do <manifest-path> [--no-log]`.
- Phrases its description matches: "execute the manifest", "run the plan", "implement it".
- `auto` after define; `babysit-pr` after its Manifest; `run-ticket` through `auto`.

## Driving it

Preconditions: the baseline in the index; a Manifest from a define drive, and a scratch git repository it may change.

- **Execute.** `/do <manifest-path>` headless from the scratch repository. The run ends in `/done` or `/escalate`; the log file exists at the documented path.
- **No log.** `/do <manifest-path> --no-log`. No `do-*.md` log is written for that Manifest.
- **Proof.** Save the transcript, the log, and `git log`/`git diff` of the scratch repository. The completion report gives a basis per gate and lists the user's calls first.

## How it is checked

Indirectly by the define suite's executor-facing cases under `claude-plugins/manifest-dev/evals/define/`; `tests/test_goal_contract_blocks.py` pins the goal block verbatim.

## Gotchas

- It changes files, commits, and may push or open pull requests as its Manifest allows. Never drive it on this checkout.
- A plan approval is not a request to run; it says the Manifest is ready and stops.
- An external process still running is a wait, never success.

Source: `claude-plugins/manifest-dev/skills/do/SKILL.md`.
