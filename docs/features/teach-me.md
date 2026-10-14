# teach-me

Teaches the user a body of work — this session's changes, a pull request, a decision record, a topic — stage by stage, confirming understanding before moving on.

Status: unverified

## Sub-features

- `session` — no argument: the current session's changes
- `topic` — a pull request, decision record or subject

## How to get to it (user POV)

- `/teach-me [topic]`.
- Phrases its description matches: "teach me what we did", "explain this ADR".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; a topic: a decision record path is the easiest.

- **Teach.** `/teach-me docs/adr/<record>.md`. The first turn explains the problem the record solved and ends with a check question.
- **Proof.** Save the transcript. It does not move on before the check is answered.

## How it is checked

No behavior case or test.

## Gotchas

- Interactive by design; a headless drive shows only the first stage.

Source: `claude-plugins/manifest-dev-tools/skills/teach-me/SKILL.md`.
