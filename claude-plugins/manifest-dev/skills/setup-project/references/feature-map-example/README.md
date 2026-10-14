# Notes feature map

How to reach and drive each user-facing feature of Notes, a note-taking app with a browser UI, a
`notes` command-line tool, and a `summarize` skill for coding agents. Read this index first, then
open the feature file that matches what you need.

## Baseline preconditions

- Start Notes with `control-notes launch --data-dir /tmp/notes-verify-$RUN_ID`, which seeds notes
  titled `Quarterly plan` and `Grocery list` and serves the UI at `http://127.0.0.1:4173`.
- Run `control-notes doctor`. Drive nothing until it reports the expected URL, the data directory
  above, and the current build revision.
- Put `control-notes` and the `notes` CLI on `PATH`.
- Never drive an instance this run did not start.

## Driving conventions

- Start every recipe from the baseline state unless its preconditions say otherwise.
- Reach controls by role and accessible name, never by CSS selector or position.
- Take every command literally, quoted names and flags included.
- Restore seeded data after a change. Cleanup never removes evidence.

## Proof and skip rules

- Capture the action and the resulting state, not only the final screen.
- UI proof is an accessibility snapshot plus a screenshot with the app identity visible; CLI proof
  is the command, stdout, stderr and exit code.
- A change is proven by reading the stored value back through a second view.
- Save evidence under `artifacts/<feature>/` and name the feature and entry point it came from.
- An entry point that could not be driven is reported with the command tried and the prerequisite
  that was missing. It is never reported as verified because another entry point worked.

## Features

- [Create a note](./create-note.md) — browser and CLI creation, cancelling a draft, persistence.
- [Summarize notes](./summarize-skill.md) — the agent skill that summarizes a set of notes.
