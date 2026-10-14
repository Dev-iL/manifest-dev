# review-pr

Reviews a pull request and posts high-signal comments in the user's voice under their account — a reviewer fleet, a premise check, thread follow-up — in one batched review per pass.

Status: unverified

## Sub-features

- `fleet` — no Manifest: one review-code run per relevant dimension, plus review-prompt for prompts
- `manifest` — `--manifest <path>`: verifies only that Manifest's contract
- `bundle` — `--bundle <urls>` and linked pull requests for coupled changes
- `loop` — `--loop`: checkpoints and wakes for later passes
- `threads` — re-judges its own earlier threads against the new code

## How to get to it (user POV)

- `/review-pr [pr-url] [--manifest <path>] [--bundle <urls>] [--loop]`.
- Phrases its description matches: "review this PR", "post a review", "watch this PR".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; `gh auth status` succeeds and a throwaway pull request in a repository the run owns.

- **Review.** `/review-pr <url>`. One GitHub review whose comments each carry `<!-- manifest-dev:review-pr -->`.
- **Proof.** Save the transcript and `gh api repos/<o>/<r>/pulls/<n>/reviews`. No `REQUEST_CHANGES` review; approval only after the user confirmed it.

## How it is checked

`tests/test_dist_skill_references.py` checks its markers, Manifest mode and fleet references. No behavior case.

## Gotchas

- Posting is public and does not undo. Never drive it on someone else's pull request to test it.
- Manifest mode needs the checkout at the pull request's head.

Source: `claude-plugins/manifest-dev-tools/skills/review-pr/SKILL.md`.
