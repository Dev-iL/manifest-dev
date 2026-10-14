# review-design

Reviews a digital artifact as delivered — rendered, played or opened in its real medium — against the user's task and direction, and reports evidence-backed graded findings.

Status: verified (2026-10-14); not driven: a rendered review (no browser in the drive container), the description phrases, define's UI gates

## Sub-features

- `select` — the named artifact, or the most recent one the user can see
- `genre` — `genre=` wins; otherwise inferred and disclosed
- `html-check` — runs `claude-plugins/manifest-dev/skills/review-design/scripts/design-check.mjs` on HTML (see design-instruments)
- `grade` — CRITICAL to LOW; PASS by default at no MEDIUM or above
- `precedence` — the user's stated rules and the project's design system govern over the shipped standards

## How to get to it (user POV)

- `/review-design [artifact] [genre=…]`.
- Phrases its description matches: "design review", "is this page accessible".
- define's UI gates (run under `/do`).

## Driving it

Preconditions: the baseline in the index; an HTML file and, for render checks, Playwright with Chromium.

- **Review.** `scripts/features/drive.sh review-design <prompt>` with a prompt that writes a small `page.html`, then `/manifest-dev:review-design page.html`. A report with findings tied to rendered evidence, or BLOCKED naming the evidence it could not get.
- **Project rule.** A prompt that writes a context file with a rule a standard would flag (a fixed-width layout), a page following it, then a review. The overridden checks raise no finding and the report names the rule; rendered properties are BLOCKED where no browser runs.
- **Proof.** From the drive's summary and its full evidence. The artifact is unchanged.

## How it is checked

`docs/features/evidence/review-design/20261014T080122Z.md` (project rule, source-only); `tests/test_design_check.py` exercises its check script; `tests/test_design_standalone.py` keeps its support files reachable.

## Gotchas

- Reading source alone is not a design verdict; without rendering it reports BLOCKED or SKIPPED, never PASS.
- The check script's exit 0 means it completed, not that the page is clean.

Source: `claude-plugins/manifest-dev/skills/review-design/SKILL.md`.
