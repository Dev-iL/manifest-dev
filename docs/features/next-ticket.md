# next-ticket

Reads the Ticket store, picks the one Ticket whose delay would cost the project most, claims it, and presents it with why it leads. It does not run the Ticket.

Status: unverified

## Sub-features

- `select` — ranks open Tickets across efforts
- `claim` — claims the chosen Ticket before presenting it
- `present` — shows the whole Ticket and the reason it leads

## How to get to it (user POV)

- `/next-ticket`.
- Phrases its description matches: "what's next", "what should I work on".
- No other skill calls it; `run-ticket` and `sweep-tickets` deliberately do not.

## Driving it

Preconditions: the baseline in the index; a prompt that first has ticket-up file two small Tickets in a file store, then runs `/manifest-dev:next-ticket` in the same session.

- **Select.** `scripts/features/drive.sh next-ticket <prompt>`. One Ticket presented with a reason; the summary's files show only that Ticket gaining a claim line.
- **Proof.** From the drive's summary and its full evidence. Only the chosen Ticket changed, and only by its claim.

## How it is checked

`tests/test_ticket_automation_prompts.py` covers the Ticket skills' boundaries; nothing exercises its ranking.

## Gotchas

- It claims at once; a GitHub venue assigns the Issue for real.
- "It didn't start the work" is intended: execution belongs to `run-ticket` or the person holding the claim.

Source: `claude-plugins/manifest-dev/skills/next-ticket/SKILL.md`.
