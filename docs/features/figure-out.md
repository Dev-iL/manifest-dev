# figure-out

Presses on a topic with the user until both understand it, and ends with a named read: a conclusion, its confidence, the evidence, and what would overturn it. It changes nothing in the project except the docs it keeps current.

Status: verified (2026-10-14)

## Sub-features

- `investigate` — attended investigation, one ask per turn, ending in a read
- `docs` — on a project: glossary captures, decision-record offers, North Star updates, the setup offer, stale markers on the verification surface
- `recall` — reads earlier logs, Manifests, Tickets and pull requests' debt for the same repository
- `taste` — offers to save a stated steering preference to the user's memory file
- `prototype` — offers a disposable draft and calls design for its look
- `autonomous` — `--autonomous`: answers its own asks with its recommendation
- `team` — `--team`: the counterparty is a Slack channel or thread
- `no-log / no-docs` — `--no-log`, `--no-docs` turn those parts off

## How to get to it (user POV)

- `/figure-out [topic] [--no-docs] [--no-log] [--autonomous] [--team]`.
- Phrases its description matches: "think through a decision", "dig deeper", "investigate why something is happening".
- `auto` when shared understanding is missing; `define` when the transcript has none; `figure-out-team` with `--team`.

## Driving it

Preconditions: the baseline in the index; a prompt file holding the matching eval case's prompt (the body of its `prompt.md` below the front matter).

- **Current setup, docs mode.** `scripts/features/drive.sh figure-out <prompt> --scaffold claude-plugins/manifest-dev/evals/45-current-setup-offers-nothing` with case `45`'s prompt. The reply says the setup is current, lists nothing the project lacks, does not suggest a setup run, moves to the topic with one ask, and names a log under the drive's `~/.manifest-dev/logs/`; the summary shows no files written.
- **Setup one version behind.** The same with case `47`. The reply offers the update and names only what v2 adds.
- **Autonomous.** Any case's prompt with `--autonomous` added. No question waits for an answer; each self-answered ask appears as a flagged assumption on the read.
- **Proof.** The drive's summary under `docs/features/evidence/figure-out/`. The read names a conclusion, confidence, evidence and what would overturn it.

## How it is checked

The figure-out behavior suite, `claude-plugins/manifest-dev/evals/` cases `01` to `47` (tags `figure-out`, `figure-out-plugin-only`), all `unmeasured` or stale per `claude-plugins/manifest-dev/evals/README.md`; `tests/test_eval_cases.py` keeps its case list in step. Drive evidence: `docs/features/evidence/figure-out/20261014T062318Z.md`.

## Gotchas

- Without the skill named in the prompt it may not fire; the eval README measures how often.
- A user's agreement is not a go: it never edits code, so "it didn't implement" is the intended outcome, not a failure.
- Docs mode writes into the project (glossary, records, surfaces line); the drive's scratch project absorbs it.
- The context file's surfaces version is an HTML comment, and the host strips comments from the copy it loads into the session; a run that reports no version without reading the file from disk has hit that, not a missing line.
- `--team` needs Slack access; without it the team entry point is `unreachable`.

Source: `claude-plugins/manifest-dev/skills/figure-out/SKILL.md`.
