---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The project records surfaces version v5, one behind the newest (v6). It already has everything v1
to v5 brought: the version line, an `Enforced by` field on its decision record, the
records-in-effect rule, and one verification harness (`scripts/verify`, `verification/harness.md`
with `start`, `logs` and `stop` control commands on a per-run identity, two feature recipes with
evidence, and the v5 verification bullet). Its context file also has a *Before merging* section
naming `python3 -m pytest tests/` and `ruff check src tests`, which no recipe runs. What v6 adds: a
recipe for the checks run across the whole tree (the tests and the linter, each a scenario calling
the project's own command), pointing the *Before merging* wording at that recipe so there is one
way in, and the bullet's new wording.

**First, list** what the reply offers to add, change or remove in the project's setup.

**Then judge.** PASS only if all of these hold:

- It offers to update the setup to v6, naming the tests or the linter as something the harness
  should run (a recipe or scenarios for them), or the *Before merging* commands as a second way in
  outside the harness.
- It does not offer, as missing, anything v1 to v5 already gave: the version line, an `Enforced
  by` field, the records-in-effect rule, a verification harness or `scripts/verify` as something
  new, control commands or a per-run identity, moving a feature map or reader tasks into recipes,
  or a redo of the glossary, North Star or conventions.

FAIL otherwise.
