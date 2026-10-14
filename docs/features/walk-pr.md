# walk-pr

Walks the user through a pull request or large diff one sub-change and one review topic at a time, and posts the comments they approve as one review.

Status: unverified

## Sub-features

- `walk` — one sub-change, one topic per turn
- `canvas` — `--canvas`: the walk runs in a live HTML page, styled through design
- `comments` — each comment confirmed on its own, posted together at the end

## How to get to it (user POV)

- `/walk-pr [pr-url | range] [--canvas]`.
- Phrases its description matches: "walk me through this PR", "review this together".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; a pull request or a local range; for posting, GitHub access to a throwaway pull request.

- **Walk a range.** `scripts/features/drive.sh walk-pr <prompt> --tools` with a prompt that makes two commits in the scratch project, then `/manifest-dev-tools:walk-pr HEAD~1..HEAD`. The first turn covers one sub-change and asks about one topic.
- **Proof.** From the drive's summary and its full evidence. Nothing posts until the user confirms each comment.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- It is interactive by design; a headless drive shows only the first turn.
- Posted comments are public.

Source: `claude-plugins/manifest-dev-tools/skills/walk-pr/SKILL.md`.
