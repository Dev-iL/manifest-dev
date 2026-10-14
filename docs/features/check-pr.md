# check-pr

Inspects one GitHub pull request — CI, review threads, description sync, mergeability — and returns PASS or FAIL per gate, with the next action for each wait. It never merges and never writes.

Status: unverified

## Sub-features

- `inspect` — baseline gates for one pull request
- `steering` — extra gates, approvers, flaky-check guidance, wait overrides
- `directives` — names the next action: wait, retrigger, reply, re-request review, sync the description

## How to get to it (user POV)

- `/check-pr <pr-url | owner/repo#N>`.
- Phrases its description matches: "is this PR ready to merge", "check mergeability", "babysit a PR".
- `run-ticket` before merge; `/do` through a pull-request lifecycle gate (and so `babysit-pr`).

## Driving it

Preconditions: the baseline in the index; `gh auth status` succeeds and a pull request the run may read.

- **Inspect.** `scripts/features/drive.sh check-pr <prompt>` with `/manifest-dev:check-pr <url of a throwaway pull request>`. One PASS or FAIL report with a line per gate.
- **Proof.** From the drive's summary and its full evidence. The report's mergeability matches GitHub's; no comment, label or merge appeared on the pull request.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it. define's pull-request lifecycle task file names it as a gate.

## Gotchas

- Without GitHub access every entry point is `unreachable`.
- The drive container carries no GitHub credentials, so a drive through `scripts/features/drive.sh` reaches this entry only after a GitHub token for a throwaway repository is added to it; until then its GitHub entry points are `unreachable`.
- GitHub's `UNKNOWN` merge state is a wait, not a PASS.
- PASS means mergeable, not authorized to merge.

Source: `claude-plugins/manifest-dev/skills/check-pr/SKILL.md`.
