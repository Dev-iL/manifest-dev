# babysit-pr

Tends the user's own pull request through CI, review threads, description sync and mergeability, fixing what it can, with or without an existing Manifest.

Status: unverified

## Sub-features

- `infer-pr` — no URL: the current branch's only open pull request
- `manifest` — `--manifest <path>` uses that Manifest instead of synthesizing one
- `synthesize` — otherwise define `--babysit <url> --autonomous`, then do
- `ci` — `--ci`: one advance, then exit when only waiting remains
- `journal` — append-only journal at `~/.manifest-dev/logs/babysit-<owner>-<repo>-<N>.md`; `--no-log` turns it off

## How to get to it (user POV)

- `/babysit-pr [pr-url] [--manifest <path>] [--ci] [--no-log]`; the Pi template `dist/pi/prompts/babysit-pr.md`.
- Phrases its description matches: "babysit my PR", "get this PR through CI and reviews".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; `gh auth status` succeeds and a throwaway pull request the run may push to.

- **CI pass.** `scripts/features/drive.sh babysit-pr <prompt> --tools` with `/manifest-dev-tools:babysit-pr <url> --ci`. One advance in the transcript, then exit; the journal file exists.
- **Proof.** From the drive's summary and its full evidence. Every push or reply on the pull request appears in the journal.

## How it is checked

`tests/test_goal_contract_blocks.py` checks it owns the goal; `tests/test_dist_skill_references.py` checks its define coupling and Pi template. No behavior case.

## Gotchas

- It pushes commits and replies on GitHub; those reach reviewers and do not undo.
- The drive container carries no GitHub credentials, so a drive through `scripts/features/drive.sh` reaches this entry only after a GitHub token for a throwaway repository is added to it; until then its GitHub entry points are `unreachable`.
- `--ci` is one advance, not a waiter.

Source: `claude-plugins/manifest-dev-tools/skills/babysit-pr/SKILL.md`.
