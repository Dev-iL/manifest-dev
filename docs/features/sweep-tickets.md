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

Preconditions: the baseline in the index; a scratch repository with a shared-store config and one ready Auto Ticket.

- **Sweep.** `/sweep-tickets` in the scratch repository. Exactly one `run-ticket` invocation in the transcript, then the run stops.
- **Proof.** Save the transcript and the Ticket files. No second Ticket was touched.

## How it is checked

`tests/test_ticket_automation_prompts.py` checks the sweep and its hand-off to run-ticket.

## Gotchas

- It is not a batch runner: one Ticket, then stop.
- Only Tickets granted Auto are eligible.

Source: `claude-plugins/manifest-dev/skills/sweep-tickets/SKILL.md`.
