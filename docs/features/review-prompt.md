# review-prompt

Reviews a prompt against the prompt-engineering principles and reports findings and an overall assessment without changing the file.

Status: verified (2026-10-14); not driven: the description phrases, define's prompting gate, review-pr's fleet

## Sub-features

- `review` — findings led by where each line came from
- `assess` — Excellent, Good with Minor Issues, or Needs Work
- `precedence` — the user's stated rules and the project's conventions govern over the prompt-engineering principles, except a High issue that makes the prompt miss its goal

## How to get to it (user POV)

- `/review-prompt <file or prompt>`.
- Phrases its description matches: "review this prompt", "audit this system prompt".
- define's prompting gate (run under `/do`); review-pr for diffs that touch prompts.

## Driving it

Preconditions: the baseline in the index; a prompt file in a scratch directory.

- **Review.** `scripts/features/drive.sh review-prompt <prompt> --tools` with `/manifest-dev-tools:review-prompt` and a prompt pasted inline. A report with an assessment and findings, each with a fix.
- **Team rule with a goal-missing prompt.** A team rule followed by a prompt that misses its stated goal. The High issue is still reported.
- **Team rule.** A prompt stating a team rule the principles would question (a ROLE line), then a prompt following it. No finding on the rule, and the report names it.
- **Proof.** From the drive's summary and its full evidence. The file is unchanged.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh` (`docs/features/evidence/review-prompt/20261014T080122Z.md`, `docs/features/evidence/review-prompt/20261014T091413Z.md`); `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- It loads prompt-engineering first; if that skill is missing the review is shallower and should say so.

Source: `claude-plugins/manifest-dev-tools/skills/review-prompt/SKILL.md`.
