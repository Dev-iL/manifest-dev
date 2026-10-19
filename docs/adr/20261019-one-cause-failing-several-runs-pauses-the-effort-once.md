# ADR: One cause failing several runs pauses the effort once

## Status
Accepted

## Area
Ticketing

## Decided by
The user

## Context
Under 20261018-an-orchestrating-skill-runs-the-queue-and-replaces-the-sweep, a `Paused:` line on
an effort's front item stops new launches and landing turns, and only a person writes it. When the
base branch goes red, or CI or the venue is down, every live run fails on that one cause. Each run
then escalates or tries to repair its own Ticket, and the person gets one item per Ticket for one
problem, or runs spend quota repairing what is not theirs.

## Decision
- When two or more live runs fail on one cause outside their Tickets, `orchestrate` pauses the
  effort instead: it writes a `Paused:` line naming the cause and its own ID, and raises one item
  naming the cause on the list of what waits on the person.
- Once the cause is fixed it removes only the `Paused:` line it wrote, never one a person wrote.
  A status-page write re-reads the front item just before its edit and changes nothing else, so a
  person's `Paused:` line is never erased.

## Alternatives Considered
- **Escalate each Ticket**: the standing behavior; one cause becomes many items.
- **Retry until the cause clears**: spends quota on a failure no run can fix, with no one told.

## Consequences

### Positive
- One cause reaches the person once, and the fleet stops spending on it.

### Negative
- `orchestrate` now writes a line a person used to own alone, and judges what counts as one cause.

## Enforced by
partly — `tests/test_ticket_automation_prompts.py` — `test_the_pause_line_is_never_erased_and_one_cause_pauses_once`
fails if the common-cause pause, its own-line-only removal or the re-read before the status-page
write is dropped; deciding that failures share a cause stays judgment.

## Source
- Session: figure-out and define comparing pstack 0.15.27 with manifest-dev (2026-10-19).
- Related: amends 20261018-an-orchestrating-skill-runs-the-queue-and-replaces-the-sweep; see also
  20261019-each-item-waiting-on-the-person-carries-its-recommendation-risk-and-evidence
