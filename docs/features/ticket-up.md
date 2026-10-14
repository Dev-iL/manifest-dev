# ticket-up

Writes self-sufficient Tickets into the project's Ticket store — from a Manifest (one Shaped Ticket by default), a direct request, an open question, or follow-ups from another Ticket.

Status: unverified

## Sub-features

- `from-manifest` — one Shaped Ticket; split by Deliverable only when asked for delegation
- `direct` — a Ticket from a plain work request
- `question` — a Ticket for an open question
- `follow-up` — grouped follow-ups from another Ticket, with their own Auto decision
- `venues` — file store, GitHub Issues, or another tracker named in the store config

## How to get to it (user POV)

- `/ticket-up <manifest path | request | question>`.
- Phrases its description matches: "create tickets", "ticket up the plan", "hand this to a teammate".
- figure-out when questions stop depending on each other; `run-ticket` for follow-ups; setup-project's hand-off of a surface gap.

## Driving it

Preconditions: the baseline in the index; a scratch repository with a file store (`tickets/store-config.md` naming the file venue).

- **From a Manifest.** `/ticket-up <manifest path>` in the scratch repository. One file `tickets/<effort>/NN-<slug>.md` with the convention's sections.
- **Proof.** Save the transcript and the Ticket files. Each Ticket stands alone: a reader with no Manifest knows what to do and how it is checked.

## How it is checked

`tests/test_ticket_automation_prompts.py` checks its authoring boundary, Auto grants and venue mapping.

## Gotchas

- It reads `tickets/store-config.md` first; without a store it asks where Tickets live.
- A GitHub venue writes real Issues. Use a throwaway repository.
- File-store claims do not cross clones or branches.

Source: `claude-plugins/manifest-dev/skills/ticket-up/SKILL.md`.
