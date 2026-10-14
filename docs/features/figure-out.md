# figure-out

Presses on a topic with the user until both understand it, and ends with a named read: a conclusion, its confidence, the evidence, and what would overturn it. It changes nothing in the project except the docs it keeps current.

Status: unverified

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

Preconditions: the baseline in the index; the matching eval case's scaffold in a scratch directory (any case from `01` to `47` under the eval suite).

- **Investigate.** `claude -p --plugin-dir ./claude-plugins/manifest-dev "use the figure-out skill for this. <topic>"` from the scratch directory. The reply makes one claim and one ask; a log path under `~/.manifest-dev/logs/figure-out-log-*.md` is named and the file exists.
- **Docs on a set-up project.** Scaffold `30-update-offer-for-older-setup` and run its `prompt.md`. The reply offers the setup update; nothing outside `CONTEXT.md`, decision records, `NORTH_STAR.md` or the surfaces line changed.
- **Autonomous.** Same prompt with `--autonomous`. No question waits for an answer; each self-answered ask appears as a flagged assumption on the read.
- **Proof.** Save the transcript, the log file and `git -C <scratch> status`. The read names a conclusion, confidence, evidence and what would overturn it.

## How it is checked

The figure-out behavior suite, `claude-plugins/manifest-dev/evals/` cases `01` to `47` (tags `figure-out`, `figure-out-plugin-only`), all `unmeasured` or stale per `claude-plugins/manifest-dev/evals/README.md`; `tests/test_eval_cases.py` keeps its case list in step.

## Gotchas

- Without the skill named in the prompt it may not fire; the eval README measures how often.
- A user's agreement is not a go: it never edits code, so "it didn't implement" is the intended outcome, not a failure.
- Docs mode writes into the project (glossary, records, surfaces line). Drive it only in a scratch directory.
- `--team` needs Slack access; without it the team entry point is `unreachable`.

Source: `claude-plugins/manifest-dev/skills/figure-out/SKILL.md`.
