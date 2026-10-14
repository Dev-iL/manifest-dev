# Summarize notes

A coding agent with the Notes plugin installed summarizes a set of notes into one short brief,
citing each note it used.

Status: unverified

## Sub-features

- `summarize-direct` summarizes the notes the user names.
- `summarize-query` finds the notes matching a query first, then summarizes them.
- `summarize-empty` says plainly that nothing matched instead of inventing a summary.

## How to get to it (user POV)

- The `/summarize <query or titles>` slash command.
- Asking the agent to "sum up my notes on …" or "brief me on the plan", which matches the skill's
  description.
- The `weekly-review` skill, which calls it for the past week's notes.

## Driving it

Preconditions: baseline state; a fresh, non-interactive agent session with the plugin loaded
from this checkout, one prompt per session.

- **Direct.** Prompt `/summarize "Quarterly plan"`. The reply is a brief that cites
  `Quarterly plan` and no other note.
- **Query.** Prompt `/summarize budget`. The reply cites every note whose title or body mentions
  the budget, and only those.
- **Empty.** Prompt `/summarize volcano`. The reply says no note matched and offers no summary.
- **Proof.** Save each prompt and reply under `artifacts/summarize/`, with the `notes` commands
  the agent ran, read from its transcript rather than its own account.

## How it is checked

Behavior cases `evals/summarize-cites-sources/` and `evals/summarize-empty-query/`.

## Gotchas

- The agent may answer from memory of an earlier run. Start each drive in a fresh session.
- A reply that *describes* running `notes search` is not evidence that it ran. Read the
  transcript.
