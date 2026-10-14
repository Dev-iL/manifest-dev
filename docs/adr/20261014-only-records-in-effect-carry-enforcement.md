# ADR: Only records in effect carry enforcement

## Status
Accepted

## Area
ADR conventions

## Decided by
The user

## Context
20261013-decision-records-name-what-enforces-them added `Enforced by` and had setup-project backfill it and define build `not yet` checks, but neither said which records count. In this repository 20 of the 170 records are superseded or deprecated; a backfill or a `not yet` search across all of them would spend effort on dead decisions, and a check built for a superseded record would hold the old decision against the new one.

## Decision
- Only an `Accepted` record is in effect, including one a later record narrows or amends.
- Whatever acts on records reads only those in effect: backfilling `Enforced by`, building a `not yet` check, and citing a record as a binding ruling.
- A deprecated or superseded record is history. Its check is retargeted or retired with the record that changed it, and its `Enforced by` line is not backfilled or kept current.
- The rule lives once, in the ADR conventions' lifecycle, which setup-project, figure-out and define already load.

## Alternatives Considered
- **State the filter in each skill that reads records**: three copies of one rule that drift apart.
- **Backfill every record for completeness**: effort on decisions nobody follows, and checks that hold dead decisions.

## Consequences

### Positive
- Backfill and check-building cost scale with the decisions in force.

### Negative
- A record wrongly left `Accepted` after its decision lapsed still draws enforcement until someone restatuses it.

## Enforced by
partly — `tests/test_project_conventions_forks.py` keeps this repository's `docs/adr/CONVENTIONS.md` in step with the shipped default that states the rule. Whether each reader filters by status stays judgment.

## Source
- Session: investigation of setup-project's update behavior.
- Related: 20261013-decision-records-name-what-enforces-them
