# Create a note

A user saves a titled note from the browser or the CLI, can cancel an unfinished draft, and finds
the saved note again from the note list.

Status: verified (2026-10-01)

## Sub-features

- `create-open` opens a blank editor from each browser entry point.
- `create-save` stores a title and body.
- `create-cancel` discards an unfinished draft.
- `create-cli` creates the same note from the terminal.

## How to get to it (user POV)

- The `New note` button in the browser toolbar.
- Pressing `n` in the browser while focus is outside a text field.
- `notes create --title <title> --body <body>` in a terminal.

## Driving it

Preconditions: baseline state; no note titled `Release checklist`.

- **Open the editor.** Run `control-notes browser click --role button --name "New note"`. A form
  named `Note editor` appears with focus in `Title`.
- **Save.** Run `control-notes browser fill --role textbox --name "Title" --value "Release checklist"`,
  then `control-notes browser click --role button --name "Save note"`. A status reads `Note saved`.
- **Read it back.** Run `control-notes browser click --role link --name "All notes"`, then open
  `Release checklist`. The editor shows the saved title.
- **Cancel a draft.** Open a new note, type `Discard me`, run
  `control-notes browser click --role button --name "Cancel"`. The list has no `Discard me`.
- **CLI.** Run `control-notes cli -- notes create --title "CLI note" --body "From terminal" --format json`.
  Exit code `0`; stdout holds the new note's ID and title.
- **Proof.** Snapshot and screenshot the note list into `artifacts/create-note/`. Both show
  `Release checklist` and `CLI note`.

## How it is checked

This recipe, driven through `control-notes`; `tests/e2e/create_note.spec.ts` covers the save path
on every build.

## Gotchas

- Pressing `n` inside a text field types the letter instead of opening an editor.
- Titles are trimmed on save. Compare against the rendered title, not the typed value.
- `Note saved` alone proves nothing. Reopen the note from the list.
