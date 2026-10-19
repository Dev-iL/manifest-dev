# ADR: The first grant decision stands, and a person's decline removes the grant

## Status
Accepted

## Area
Ticketing

## Decided by
The user

## Context
20261018-orchestrate-tickets-up-debt-and-grants-auto-where-the-criterion-holds has each
orchestrator gather the debt of Tickets that landed and grant Auto, in `--autonomous`, wherever
the grant criterion holds; in default mode it asks the person. Two orchestrators whose scopes
overlap could gather one Ticket's debt twice. A propose-mode orchestrator could ask a person about
a follow-up while an autonomous one granted it, and a person's decline recorded only a withhold,
so a grant made in the meantime stayed and the Ticket landed unattended.

## Decision
- An orchestrator gathers debt only for Tickets whose landing it recorded, plus Tickets whose
  landing reference is older than the run timeout with no gathered line.
- A grant decision is a grant or a recorded withhold. Where a Ticket carries two, the one created
  first decides, and the writer of the other takes it back with any label it applied, so a grant
  that lost a race leaves no `auto` label behind.
- A propose-mode orchestrator records a withhold naming the person as asked before it asks, which
  leaves the decision to that person and reads as decided to any orchestrator, whatever version it
  runs. Each venue reference renders it, the file store's included.
- A person's decline or withdrawal records the withhold and removes the grant itself, as the venue
  renders it, so no unattended run lands that Ticket.

## Alternatives Considered
- **The latest decision decides**: lets an autonomous grant written after a person's decline win.
- **Only the propose-mode orchestrator may decide once a person is involved**: needs each
  orchestrator to know the others' modes, which the store does not record.

## Consequences

### Positive
- A person's "no" holds against every orchestrator, attended or not.
- Each landed Ticket's debt becomes Tickets once.

### Negative
- An asked person who never answers holds the Ticket's grant until they do.

## Enforced by
`tests/test_ticket_automation_prompts.py` — `test_debt_and_grants_are_decided_once_and_a_persons_no_stands`
fails if debt gathering loses the lander rule, the first-created grant decision stops deciding, the
asked-person record is dropped, or a decline stops removing the grant on the convention or a venue.

## Source
- Session: figure-out and define comparing pstack 0.15.27 with manifest-dev, and a model of the
  ticket protocol (2026-10-19).
- Related: amends 20261018-orchestrate-tickets-up-debt-and-grants-auto-where-the-criterion-holds;
  see also 20261019-the-comment-the-venue-created-first-decides-each-ticket-fact
