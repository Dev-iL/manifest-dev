# review-prompt

Reviews a prompt against the prompt-engineering principles and reports findings and an overall assessment without changing the file.

Status: unverified

## Sub-features

- `review` — findings led by where each line came from
- `assess` — Excellent, Good with Minor Issues, or Needs Work

## How to get to it (user POV)

- `/review-prompt <file or prompt>`.
- Phrases its description matches: "review this prompt", "audit this system prompt".
- define's prompting gate (run under `/do`); review-pr for diffs that touch prompts.

## Driving it

Preconditions: the baseline in the index; a prompt file in a scratch directory.

- **Review.** `scripts/features/drive.sh review-prompt <prompt> --tools` with `/manifest-dev-tools:review-prompt` and a prompt pasted inline. A report with an assessment and findings, each with a fix.
- **Proof.** From the drive's summary and its full evidence. The file is unchanged.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- It loads prompt-engineering first; if that skill is missing the review is shallower and should say so.

Source: `claude-plugins/manifest-dev-tools/skills/review-prompt/SKILL.md`.
