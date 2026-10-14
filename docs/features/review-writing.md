# review-writing

Reviews prose against the project's writing standards in the register it detects — documentation or human-voiced writing — and reports graded findings with the fix.

Status: unverified

## Sub-features

- `docs-register` — specs, READMEs, reports
- `voice-register` — posts, articles, marketing copy
- `register-choice` — an explicit register wins; otherwise it infers and says so

## How to get to it (user POV)

- `/review-writing [file or pasted text] [register=docs|voice]`.
- Phrases its description matches: "does this read as AI-written", "review this before publishing".
- define's writing and document gates.

## Driving it

Preconditions: the baseline in the index; a short markdown file in a scratch directory.

- **Review.** `scripts/features/drive.sh review-writing <prompt>` with `/manifest-dev:review-writing` and a short draft pasted inline. A report naming the register it used and findings with severity and a fix.
- **Proof.** From the drive's summary and its full evidence. The draft is unchanged.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- A wrong register gives a wrong review; name it when the text is mixed.
- Whether prose earns its place in a code change is review-code's `prose-value`, not this.

Source: `claude-plugins/manifest-dev/skills/review-writing/SKILL.md`.
