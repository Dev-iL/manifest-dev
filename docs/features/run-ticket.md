# run-ticket

Takes one exact Ticket, recovers any earlier attempt, runs it through auto and its required landing, and writes DONE or ESCALATED evidence back on that same Ticket.

Status: unverified

## Sub-features

- `recover` — reconciles an earlier attempt's marker, branch and pull request
- `execute` — invokes auto with the Ticket as the task
- `land` — observes the required landing, using check-pr before merge
- `record` — DONE or ESCALATED written to the Ticket, with its marker comment
- `follow-ups` — separate findings routed to ticket-up

## How to get to it (user POV)

- `/run-ticket <ticket reference>`.
- Phrases its description matches: "run this ticket end to end", a hosted trigger or agent runner supplying an issue.
- `sweep-tickets` for the one Ticket it selects.

## Driving it

Preconditions: the baseline in the index; a prompt that first has ticket-up file one small Ticket with a checkable end, then runs `/manifest-dev:run-ticket` on it in the same session.

- **Run.** `scripts/features/drive.sh run-ticket <prompt> --max-turns 120`. The Ticket gains `<!-- manifest-dev-run-ticket-attempt -->` and, at the end, a DONE section or `<!-- manifest-dev-run-ticket-escalated -->`.
- **Proof.** From the drive's summary and its full evidence. The landing the Ticket asks for is observed, not assumed.

## How it is checked

`tests/test_ticket_automation_prompts.py` checks markers, recovery and follow-up routing.

## Gotchas

- It does not pick from a backlog; a missing or ambiguous reference stops before any work.
- Running it by hand does not grant Auto.
- Everything auto and do may do, it may do — and a GitHub venue writes to real Issues.

Source: `claude-plugins/manifest-dev/skills/run-ticket/SKILL.md`.
