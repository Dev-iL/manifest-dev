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

- **Walk a range.** `/walk-pr main..HEAD` in a scratch repository with two commits. The first turn covers one sub-change and asks about one topic.
- **Proof.** Save the transcript. Nothing posts until the user confirms each comment.

## How it is checked

No behavior case or test.

## Gotchas

- It is interactive by design; a headless drive shows only the first turn.
- Posted comments are public.

Source: `claude-plugins/manifest-dev-tools/skills/walk-pr/SKILL.md`.
