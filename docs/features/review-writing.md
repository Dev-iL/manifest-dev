# review-writing

Reviews prose against the project's writing standards in the register it detects — documentation or human-voiced writing — and reports graded findings with the fix.

Status: verified (2026-10-14); not driven: the description phrases, define's writing gates, the voice register

## Sub-features

- `docs-register` — specs, READMEs, reports
- `voice-register` — posts, articles, marketing copy
- `register-choice` — an explicit register wins; otherwise it infers and says so
- `precedence` — the project's style sheet, `AUTHOR_VOICE.md` and the user's stated rules outrank the shipped references; a CRITICAL on the applied register's scale is still reported

## How to get to it (user POV)

- `/review-writing [file or pasted text] [register=docs|voice]`.
- Phrases its description matches: "does this read as AI-written", "review this before publishing".
- define's writing and document gates.

## Driving it

Preconditions: the baseline in the index; a short markdown file in a scratch directory.

- **Review.** `scripts/features/drive.sh review-writing <prompt>` with `/manifest-dev:review-writing` and a short draft pasted inline. A report naming the register it used and findings with severity and a fix.
- **User rule that causes a CRITICAL.** A team rule whose result is a CRITICAL (softening a required step to "may"). The CRITICAL is still reported, naming the rule.
- **User rule.** A prompt stating two team rules the references contradict (Title Case headings, "utilize"), then a draft following them. Neither raises a finding, and the report says which rules it applied.
- **Proof.** From the drive's summary and its full evidence. The draft is unchanged.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh` (`docs/features/evidence/review-writing/20261014T080014Z.md`, `docs/features/evidence/review-writing/20261014T091413Z.md`); `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- A wrong register gives a wrong review; name it when the text is mixed.
- Whether prose earns its place in a code change is review-code's `prose-value`, not this.

Source: `claude-plugins/manifest-dev/skills/review-writing/SKILL.md`.
