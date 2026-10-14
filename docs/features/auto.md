# auto

Chains figure-out, define and do with no approval stops: understanding, then a Manifest, then execution, all in one run.

Status: unverified

## Sub-features

- `chain` — figure-out `--autonomous` (when needed) → define `--autonomous` → do
- `checkpoint` — continues past figure-out's read and define's handoff instead of stopping

## How to get to it (user POV)

- `/auto <task>`; the Pi template `dist/pi/prompts/auto.md`.
- Phrases its description matches: "autonomous", "end-to-end", "from idea to done".
- `run-ticket`, with the Ticket as the task.

## Driving it

Preconditions: the baseline in the index; a scratch git repository and a small task with a checkable end.

- **Chain.** `/auto <task>` headless. The transcript shows define reporting a Manifest path and do starting on that same path in the same run.
- **Proof.** Save the transcript, the Manifest and the do log. The run ends in `/done` or `/escalate`, not at a handoff waiting for the user.

## How it is checked

`tests/test_dist_skill_references.py` checks the chain and that do alone owns the continuation; no behavior case.

## Gotchas

- Stopping after figure-out's read or define's handoff is the defect it exists to avoid.
- Everything do may do, auto may do. Scratch repository only.

Source: `claude-plugins/manifest-dev/skills/auto/SKILL.md`.
