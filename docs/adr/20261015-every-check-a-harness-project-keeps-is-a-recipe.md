# ADR: Every check a harness project keeps is a recipe, and the evidence a change rests on comes through the harness

## Status
Accepted

## Area
define / do

## Decided by
The user

## Context
20261014-one-verification-harness-per-project made every check a recipe and had recipes delegate to the project's existing commands, so there is one way to check each thing. The shipped text that builds a harness did not carry that far. `VERIFICATION_HARNESS.md` defined a recipe as one file per thing a user reaches or a reader relies on; the upgrade guides built a harness by moving an older surface's entries one for one, and reached *Build on what exists* only where a project had no surface; the setup audit offered recipes for what users reach and nothing else; and the three example recipes were a feature, a skill and a walk. A production project upgraded from a feature map ended with a harness of user-reachable features while its lint, type checks, unit suite, build and gate runner lived outside it, and its context file taught them as a separate way in. An agent asked whether a change worked ran the lint command directly, recorded nothing through the harness, and the harness's statuses said nothing about lint, types or tests.

## Decision
- Where a project keeps the verification harness, every check it keeps is a recipe, including the checks it runs across the whole tree — lint, type checks, its test suite, a build, a gate runner. Each becomes a scenario of a recipe of kind `suite` that covers the whole tree and calls the project's own command, so there is still one definition of each check.
- The evidence a run reports a change on comes through the harness. Calling the underlying command directly while iterating stays fine.
- Every path that builds or audits a harness adopts those checks: a first install, an upgrade that moves an older surface into recipes, and an audit of a harness that lacks them. A context file that names a verification command no recipe runs teaches a second way in, and the audit offers to close it.
- A project that verifies its own way is untouched: its verification bullet already lists its commands, and no run builds or offers a harness there (20261015-the-verification-harness-is-optional).
- The change ships as surfaces v6, with a fourth example recipe for the checks run across the whole tree and a sentence in the verification bullet saying where the evidence comes from.

## Alternatives Considered
- **Keep the harness a catalog of user-reachable things and let the context file name the gate set**: two ways in, and the harness's statuses stay silent on lint, types and tests, which is the failure above.
- **A separate `gates:` setting in `harness.md`**: a second concept for what a recipe already does, with its own evidence rules to learn.
- **Force every call through the harness, even while iterating**: adds friction to the inner loop and gains nothing; what matters is that the reported evidence comes through it.

## Consequences

### Positive
- `verify list` is the one place to learn every check a harness project keeps, and its statuses speak for all of them.
- Workflow runs gate on the whole-tree recipe like any other touched recipe, so the evidence a pull request rests on is recorded.

### Negative
- A whole-tree recipe goes stale on every change until it is driven, which is the intended signal but shows on every branch.
- Each new surfaces version updates every upgrade guide.

## Enforced by
partly — `tests/test_harness_adopts_project_wide_checks.py` fails when `VERIFICATION_HARNESS.md`, setup-project's audit items, an upgrade guide or `MOVE_TO_HARNESS.md` loses the adoption of the checks run across the whole tree, or when the example recipe is removed. Whether a setup run actually offers the recipe on a real project stays judgment until an eval case measures it.

## Source
- Session: the owner's ruling on what going through the harness guarantees, 2026-10-15
- Related: Amends 20261014-one-verification-harness-per-project; see also 20261015-the-verification-harness-is-optional
