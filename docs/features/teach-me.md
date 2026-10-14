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

- **Teach.** `scripts/features/drive.sh teach-me <prompt> --tools` with `/manifest-dev-tools:teach-me` and a short decision record pasted inline. The first turn explains the problem the record solved and ends with a check question.
- **Proof.** From the drive's summary and its full evidence. It does not move on before the check is answered.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- Interactive by design; a headless drive shows only the first stage.

Source: `claude-plugins/manifest-dev-tools/skills/teach-me/SKILL.md`.
