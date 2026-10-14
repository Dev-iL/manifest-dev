# define

Turns shared understanding into a Manifest — Problem, Appetite, Deliverables with Acceptance Criteria, Global Invariants, assumptions — written to the user's home directory, ready for `/do`.

Status: unverified

## Sub-features

- `new` — writes a new Manifest from the conversation
- `amend` — a Manifest path in the arguments: targeted changes, stable IDs
- `babysit` — `--babysit <pr-url>`: a lifecycle-only Manifest synthesized from a pull request
- `autonomous` — `--autonomous`: no approval wait; decisions recorded as `(auto)` assumptions
- `recall` — reads earlier work on the repository before encoding

## How to get to it (user POV)

- `/define [task] [<manifest-path>] [--babysit <pr-url>]`.
- Phrases its description matches: "plan", "spec out", "make a manifest", "break down a task".
- `auto` (with `--autonomous`); `do` to amend; `babysit-pr` with `--babysit`; figure-out's offer at the end of a read.

## Driving it

Preconditions: the baseline in the index; a define case's prompt from `claude-plugins/manifest-dev/evals/define/`, with its scaffold where the case has one.

- **New Manifest.** `scripts/features/drive.sh define <prompt>` with the prompt of `claude-plugins/manifest-dev/evals/define/d01-layer-cut/prompt.md` (it needs no scaffold). The drive's home holds `.manifest-dev/manifests/manifest-<timestamp>.md` and the reply ends with `Manifest complete: <path>`.
- **Amend.** In the same prompt, after the Manifest is written, `/manifest-dev:define <that path> <one change>`. Only the named items change; IDs of the others are untouched (diff the file).
- **Proof.** From the drive's summary and its full evidence. Every gate in the Manifest ends with `Judgment gate.` or `Deterministic gate.` and the ceiling invariant is present verbatim.

## How it is checked

The define behavior suite, `claude-plugins/manifest-dev/evals/define/` cases `d01` to `d21` (tag `define`), statuses in `claude-plugins/manifest-dev/evals/define/README.md`; `tests/test_shared_blocks.py` and `tests/test_goal_contract_blocks.py` pin the blocks its handoff carries.

## Gotchas

- A 2026-10-14 drive of `d01-layer-cut` (`docs/features/evidence/define/20261014T063700Z.md`) wrote the Manifest into the project instead of the home directory and kept the requested layer cut; check both when driving it again.
- The Manifest is written to the home directory, not the project: in a drive it is in the evidence's `home-manifest-dev.tar`.
- Attended, it waits for a yes after the digest; a headless drive needs `--autonomous` or a prompt that says to proceed.
- An old Manifest with a `verify` block is refused, not migrated.
- A yes approves the Manifest, not execution: it never runs `/do` itself.
- "It didn't stop for approval" is define only under `--autonomous` or when called by `auto`; a whole chain that never stopped is the auto entry.

Source: `claude-plugins/manifest-dev/skills/define/SKILL.md`.
