---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The project records surfaces version v6, one behind the newest (v7). It already has everything v1
to v6 brought: the version line, an `Enforced by` field on its decision record, the
records-in-effect rule, one verification harness (`scripts/verify`, `verification/harness.md`
with `start`, `logs` and `stop` control commands on a per-run identity, two feature recipes), a
`project-checks` recipe running its tests and linter, and the v6 verification bullet. Under
`verification/evidence/` it commits run summaries, three of which carry time lines in a
`- **Line:**` field (one raised with a reason, one frozen naming `#41`), and its context file tells
runs to commit that evidence in two places. What v7 adds: each line moved into its scenario's
recipe as a `Line:` field, keeping the raise's reason and the freeze's Ticket, before the
committed evidence is removed from the repository and the evidence directory is ignored; and the
two context-file lines rewritten so runs no longer commit evidence.

**First, list** what the reply offers to add, change or remove in the project's setup.

**Then judge.** PASS only if all of these hold:

- It offers to update the setup to v7, naming at least two of: moving the time lines from the
  evidence into the recipes, no longer committing evidence (removing it from the repository or
  ignoring its directory), and changing the context-file lines that say to commit evidence.
- Where it offers both moving the lines and removing the evidence, it moves the lines first, or
  says the lines are read from the evidence before it goes.
- It does not offer, as missing, anything v1 to v6 already gave: the version line, an `Enforced
  by` field, the records-in-effect rule, a verification harness or `scripts/verify` as something
  new, control commands or a per-run identity, a recipe for the tests or the linter, moving a
  feature map or reader tasks into recipes, or a redo of the glossary, North Star or conventions.

FAIL otherwise.
