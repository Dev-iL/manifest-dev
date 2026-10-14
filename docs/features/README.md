# manifest-dev feature map

How to reach and drive each feature this repository ships: every user-invocable skill in the
two plugins, and the design instruments command-line tools. Read this index, then open the
feature file that matches the report or the change. Each file follows the shape in
`claude-plugins/manifest-dev/skills/setup-project/references/VERIFICATION_SURFACE.md` →
*The feature map*. Where a skill lives in the source is read from the source; this map says
how a user reaches it and how a run drives it.

## Baseline preconditions

- A checkout of this repository at the commit under test, with the virtual environment active
  (`source .venv/bin/activate`; `scripts/setup.sh` creates it).
- Health first: `python3 -m pytest tests/test_skill_frontmatter.py tests/test_entry_points.py -q`
  passes. A skill whose frontmatter does not parse is absent on some hosts, so a drive of it
  proves nothing.
- A skill is driven in a fresh, non-interactive agent session that loads the plugin from this
  checkout — for Claude Code, `claude -p --plugin-dir ./claude-plugins/manifest-dev "<prompt>"`
  (add `--plugin-dir ./claude-plugins/manifest-dev-tools` for its skills) — one prompt per
  session, from a scratch directory outside this repository.
- Anything a skill writes to a project goes into that scratch directory, built from the matching
  eval case's `scaffold.sh` where one exists. Never drive a skill that edits files against this
  checkout.
- Skills that act on GitHub, Slack or a shared Ticket store are driven only against a
  throwaway repository, channel or store the run owns. Their effects reach other people and do
  not undo.

## Driving conventions

- Name the skill in the prompt (`use the define skill …` or the slash command). Auto-activation
  from a description varies by phrasing; `claude-plugins/manifest-dev/evals/README.md` →
  *Why the prompts name the skill* says why.
- Take commands and flags literally. A flag counts only as a top-level argument, not quoted
  inside the topic.
- Read what the skill did from the session transcript and the files it wrote, never from its
  own account of what it did.
- Delete the scratch directory after a drive; keep the evidence.

## Proof and skip rules

- Evidence is the prompt, the transcript (`--output-format stream-json` for Claude Code), and
  the files the skill wrote, saved under `/tmp/manifest-dev-features/<feature>/<date>/`, outside
  the checkout so cleanup and `git clean` never touch it.
- Record the feature, the sub-feature and the entry point with every piece of evidence.
- An entry point that could not be driven — no GitHub access, no Slack, no Ticket store — is
  recorded as `unreachable` with the prerequisite and what was tried. It is never reported as
  verified because another entry point worked.
- The behavior cases in `claude-plugins/manifest-dev/evals/` are the measured check where an
  entry names them; a drive from this map shows the feature runs, not that it beats the
  no-plugin baseline.

## Features

Workflow (`manifest-dev`):

- [figure-out](./figure-out.md) — reach shared understanding of any topic; the investigation entry point.
- [figure-out-team](./figure-out-team.md) — the same investigation, run in a Slack channel or thread.
- [define](./define.md) — turn understanding into a Manifest.
- [do](./do.md) — execute a Manifest until every gate holds.
- [auto](./auto.md) — figure-out, define and do chained without approval stops.
- [setup-project](./setup-project.md) — install and audit a project's North Star, glossary, decision records and verification surface.
- [check-pr](./check-pr.md) — read-only PASS/FAIL on one pull request's readiness.
- [ticket-up](./ticket-up.md) — write Tickets into the project's store.
- [next-ticket](./next-ticket.md) — pick and claim the Ticket to work on now.
- [run-ticket](./run-ticket.md) — run one exact Ticket end to end and record the outcome on it.
- [sweep-tickets](./sweep-tickets.md) — scheduled recovery or start of one Auto Ticket.

Review and design (`manifest-dev`):

- [review-code](./review-code.md) — review a change along one quality dimension.
- [review-writing](./review-writing.md) — review prose against the writing standards.
- [design](./design.md) — design guidance for a page, document, deck or prototype.
- [review-design](./review-design.md) — review a rendered artifact against its task and medium.
- [design-instruments](./design-instruments.md) — the `design-tools.mjs` and `design-check.mjs` command-line tools.

Tools (`manifest-dev-tools`):

- [babysit-pr](./babysit-pr.md) — tend your own pull request through CI, threads and mergeability.
- [review-pr](./review-pr.md) — review someone else's pull request and post the comments.
- [walk-pr](./walk-pr.md) — walk a pull request together, one sub-change at a time.
- [handoff](./handoff.md) — write a context payload a fresh agent can continue from.
- [manifest-to-goal](./manifest-to-goal.md) — turn a Manifest into a pasteable goal.
- [prompt-engineering](./prompt-engineering.md) — write or improve a prompt, skill or agent.
- [review-prompt](./review-prompt.md) — review a prompt without changing it.
- [teach-me](./teach-me.md) — be taught a change or topic, step by step.
- [eli5](./eli5.md) — a picture explainer of a topic.
