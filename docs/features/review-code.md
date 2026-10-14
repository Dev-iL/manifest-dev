# review-code

Reviews a change along exactly one quality dimension and returns PASS, FAIL or BLOCKED with graded findings.

Status: unverified

## Sub-features

- `dimension` — one of: change-intent, code-bugs, code-design, code-simplicity, code-maintainability, code-testability, test-quality, type-safety, contracts, operational-readiness, docs, prose-value, defect-class, context-file-adherence
- `scope` — a supplied range, or the diff against the remote default branch

## How to get to it (user POV)

- `/review-code <dimension> [scope]`.
- Phrases its description matches: "review this diff for bugs", "audit the change for type safety".
- define's coding gates (run under `/do`); review-pr's reviewer fleet.

## Driving it

Preconditions: the baseline in the index; a scratch repository with a commit on a branch ahead of its default branch.

- **Review.** `/review-code code-bugs` in the scratch repository. A report naming the dimension, findings with severity and evidence, and one verdict.
- **Proof.** Save the transcript and the diff it reviewed. Every finding points at a line inside the change.

## How it is checked

No behavior case or runtime test; `tests/test_review_scope.py` pins how scope is resolved.

## Gotchas

- One dimension per call; asking for two gets one.
- `defect-class` needs a change that fixes a defect, or it reports none found.
- No comparison base resolves to BLOCKED.

Source: `claude-plugins/manifest-dev/skills/review-code/SKILL.md`.
