# review-code

Reviews a change along exactly one quality dimension and returns PASS, FAIL or BLOCKED with graded findings.

Status: verified (2026-10-14); not driven: the description phrases, define's coding gates, review-pr's fleet

## Sub-features

- `dimension` — one of: change-intent, code-bugs, code-design, code-simplicity, code-maintainability, code-testability, test-quality, type-safety, contracts, operational-readiness, docs, prose-value, defect-class, context-file-adherence
- `scope` — a supplied range, or the diff against the remote default branch

## How to get to it (user POV)

- `/review-code <dimension> [scope]`.
- Phrases its description matches: "review this diff for bugs", "audit the change for type safety".
- define's coding gates (run under `/do`); review-pr's reviewer fleet.

## Driving it

Preconditions: the baseline in the index; a scratch repository with a commit on a branch ahead of its default branch.

- **Review.** `scripts/features/drive.sh review-code <prompt>` with a prompt that commits a small change with one bug on a branch, then `/manifest-dev:review-code code-bugs`. A report naming the dimension, findings with severity and evidence, and one verdict.
- **Proof.** From the drive's summary and its full evidence. Every finding points at a line inside the change.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_review_scope.py` pins how scope is resolved. No behavior case measures the review. Drive evidence: `docs/features/evidence/review-code/20261014T063700Z.md`.

## Gotchas

- One dimension per call; asking for two gets one.
- `defect-class` needs a change that fixes a defect, or it reports none found.
- No comparison base resolves to BLOCKED.

Source: `claude-plugins/manifest-dev/skills/review-code/SKILL.md`.
