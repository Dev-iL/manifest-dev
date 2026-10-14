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

- **Diagnose.** `scripts/features/drive.sh prompt-engineering <prompt> --tools` with `/manifest-dev-tools:prompt-engineering why does this prompt over-ask?` and the prompt pasted inline. An answer that traces lines to their source and proposes specific edits.
- **Proof.** From the drive's summary and its full evidence. It cites lines from the file, not general advice.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it. review-prompt applies its principles as a gate.

## Gotchas

- It is guidance; it edits only when asked to.

Source: `claude-plugins/manifest-dev-tools/skills/prompt-engineering/SKILL.md`.
