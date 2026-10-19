# ADR: Recall reads reverted fixes and review corrections

## Status
Accepted

## Area
define / figure-out

## Decided by
The user

## Context
20261013-figure-out-and-define-recall-earlier-sessions-on-the-same-repo has figure-out and define
read what earlier work left on a repository: logs and Manifests, open Tickets, and the "Debt left"
sections of recent pull requests on the topic's paths. Two records of what was tried and undone
stayed unread: a fix that shipped and was reverted, and a reviewer's request to do a change
differently. A new fix for the same failure can then repeat what was undone, which pstack
0.15.27's review flow guards against by reading earlier corrections.

## Decision
- On the pull requests recall already lists, it also reads the review comments that asked for
  changes, and on the topic's paths it lists the commits that revert an earlier one.
- figure-out's bug probes ask whether a fix like this one shipped and was reverted, or a reviewer
  already asked for a change like it to be made differently; what undid it constrains the fix.
- What it finds stays a dated lead to check, as everything recall finds does.

## Alternatives Considered
- **Read every comment on those pull requests**: more context at more cost, mostly approvals and
  discussion that shaped nothing.
- **Leave reverts to the investigator's own git habits**: the base model often reads the code and
  not its history.

## Consequences

### Positive
- A fix that was reverted, and the reason, reaches the next attempt at the same failure.

### Negative
- One more query per recall on a repository with a forge.

## Enforced by
partly — eval case `59-reverted-fix` measures it once run; how far back to read stays judgment.

## Source
- Session: figure-out and define comparing pstack 0.15.27 with manifest-dev (2026-10-19).
- Related: amends 20261013-figure-out-and-define-recall-earlier-sessions-on-the-same-repo
