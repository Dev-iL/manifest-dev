# sweep-tickets

From a scheduled trigger, recovers one interrupted automation-owned Auto Ticket or starts one ready Auto Ticket through run-ticket, then stops.

Status: unverified

## Sub-features

- `recover` — resumes one interrupted Ticket first
- `select` — otherwise starts the ready Auto Ticket whose delay costs most
- `one-and-stop` — at most one Ticket per invocation

## How to get to it (user POV)

- `/sweep-tickets`, normally from a scheduler.
- Phrases its description matches: "scheduled agent trigger", "resume one interrupted".
- The automation setup in ticket-up's `references/AUTOMATED_EXECUTION.md`.

## Driving it

Preconditions: the baseline in the index; a prompt that first has ticket-up file one Ticket granted Auto in a file store, then runs `/manifest-dev:sweep-tickets`.

- **Sweep.** `scripts/features/drive.sh sweep-tickets <prompt> --max-turns 120`. Exactly one `run-ticket` invocation in the transcript, then the run stops.
- **Proof.** From the drive's summary and its full evidence. No second Ticket was touched.

## How it is checked

`tests/test_ticket_automation_prompts.py` checks the sweep and its hand-off to run-ticket.

## Gotchas

- It is not a batch runner: one Ticket, then stop.
- Only Tickets granted Auto are eligible.

Source: `claude-plugins/manifest-dev/skills/sweep-tickets/SKILL.md`.
