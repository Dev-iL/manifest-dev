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

Preconditions: the baseline in the index; a scratch directory from a define case's `scaffold.sh` under `claude-plugins/manifest-dev/evals/define/`.

- **New Manifest.** Run the case's `prompt.md` (for example `d01-layer-cut`) headless with the plugin loaded. A file `~/.manifest-dev/manifests/manifest-<timestamp>.md` appears and the reply ends with `Manifest complete: <path>`.
- **Amend.** Prompt `/define <that path> <one change>`. Only the named items change; IDs of the others are untouched (diff the file).
- **Proof.** Save the transcript and the Manifest. Every gate in the Manifest ends with `Judgment gate.` or `Deterministic gate.` and the ceiling invariant is present verbatim.

## How it is checked

The define behavior suite, `claude-plugins/manifest-dev/evals/define/` cases `d01` to `d21` (tag `define`), statuses in `claude-plugins/manifest-dev/evals/define/README.md`; `tests/test_shared_blocks.py` and `tests/test_goal_contract_blocks.py` pin the blocks its handoff carries.

## Gotchas

- The Manifest is written outside the repository, under `~/.manifest-dev/manifests/`; look there, not in the scratch directory.
- Attended, it waits for a yes after the digest; a headless drive needs `--autonomous` or a prompt that says to proceed.
- An old Manifest with a `verify` block is refused, not migrated.
- A yes approves the Manifest, not execution: it never runs `/do` itself.

Source: `claude-plugins/manifest-dev/skills/define/SKILL.md`.
