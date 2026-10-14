# prompt-engineering

Guides creating, updating, reviewing or discussing an LLM prompt, skill or agent, leading with where each line came from.

Status: unverified

## Sub-features

- `write` — draft a new prompt or skill
- `update` — change one without piling up stale rules
- `diagnose` — find why a prompt misbehaves

## How to get to it (user POV)

- `/prompt-engineering <request>`.
- Phrases its description matches: "improve this prompt", "this skill needs work".
- define and figure-out before prompt-shaped work; review-prompt first; manifest-to-goal.

## Driving it

Preconditions: the baseline in the index; a prompt file in a scratch directory.

- **Diagnose.** `/prompt-engineering why does this prompt over-ask? <file>`. An answer that traces lines to their source and proposes specific edits.
- **Proof.** Save the transcript. It cites lines from the file, not general advice.

## How it is checked

No behavior case or test; review-prompt applies its principles as a gate.

## Gotchas

- It is guidance; it edits only when asked to.

Source: `claude-plugins/manifest-dev-tools/skills/prompt-engineering/SKILL.md`.
