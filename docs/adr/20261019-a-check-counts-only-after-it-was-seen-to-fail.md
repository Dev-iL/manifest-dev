# ADR: A check counts only after it was seen to fail

## Status
Accepted

## Area
define / do

## Decided by
The user

## Context
*Fit to trust* judges a check a project keeps by the jobs it does: a cold proof run, checkable
health, isolated runs, PASS on the real path, speed, control, and failures that explain
themselves (20261015-runs-keep-the-harness-fit-for-speed-control-and-diagnosis). A check that can
never fail meets every one of those jobs: it runs from cold, passes quickly and leaves evidence.
pstack 0.15.27's verification skills make a check fail on purpose before trusting it, and the
ticket protocol model added in the same change showed why: its pre-fix scenario is what proves the
model can catch the bugs it was built for.

## Decision
- *Fit to trust* gains a job, **It was seen to fail**: the check failed on a scratch break of what
  it proves — a change that makes the checked behavior wrong — and the break was then dropped.
- It reaches the runs through the same list as the other jobs: figure-out asks it, define's
  *Trust the check before relying on it* Default carries it, and do repairs or reports a check
  that fails it. The glossary's *Fit to Trust* entry names it.

## Alternatives Considered
- **Keep the scratch break as a permanent negative test**: proves more on every run, but turns
  every check into two and fits poorly where breaking the product needs a scratch edit.
- **Leave it to the test-quality review**: that review asks whether a test would fail on a
  contradictory implementation, but runs only where a review runs and only on tests, not on
  recipes, scripts or checklists.

## Consequences

### Positive
- A check that passes on anything is caught before its PASS is relied on.

### Negative
- Each new or repaired check costs one scratch break and one more run.

## Enforced by
none — whether a check was seen failing is a fact about a run, not about the files a check could
read; the `prefix` scenario of `verification/recipes/ticket-protocol-model.md` is this
repository's own instance.

## Source
- Session: figure-out and define comparing pstack 0.15.27 with manifest-dev (2026-10-19).
- Related: amends 20261015-runs-keep-the-harness-fit-for-speed-control-and-diagnosis; see also
  20261019-a-model-checks-the-ticket-protocol-against-the-prose-it-quotes
