# Upgrading a project from v4 to v6

A project recording v4 already has a verification harness, which it may keep or set aside for its
own way of verifying; set aside, its files stay or go as the user says, since the own-way bullet,
not the files, records the choice. v5 makes a kept harness control what it checks, hold check run time against
creep, keep one summary per scenario, find what a diff touches, and narrow the ask-first mark to
cost; v6 adds a recipe for the checks it runs across the whole tree, so every check it keeps is
listed and recorded in the harness.

Offer, each as its own item and as a default the project may adapt or decline where its own way
already does the job. The harness is recommended, but the project may opt out of it whole and keep its own way of
verifying: then offer none of the harness items, and offer instead the own-way form of the
verification bullet from `../NORTH_STAR_FORMAT.md` → *The project-surfaces section*, naming its
commands and steps, so no figure-out, define or do run builds or offers one:

1. **The tool update** — the shipped `../harness/verify.mts` (and `verify` entry) shown as a
   difference from the project's own copy, so its customizations stay visible; a ported tool gets
   the same commands and evidence fields described in `../VERIFICATION_HARNESS.md` → *The parts*.
   Older evidence keeps its status; the next run of each scenario leaves one summary, and a
   fixed-workload scenario starts its time line.
2. **Control commands**, per `../VERIFICATION_HARNESS.md` → *The parts*: `start`, `running`,
   `logs`, `reset` and `stop` declared in `harness.md` where the project's existing scripts already
   start, observe or stop what it runs, each on the run's `VERIFY_RUN_ID` in place of a fixed data
   directory or port; none where the project runs nothing.
3. **Ask-first marks given for run time** — each recipe whose `ask-first` reason is run time
   alone, offered for removal of the mark; a mark whose reason names cost stays.
4. **Scenarios whose work varies** — an agent session, a document walk, the affected tests — get
   `Workload: varies`, per `../VERIFICATION_HARNESS.md` → *Time lines*, so ordinary run-to-run
   variation never reads as creep.
5. **A recipe for the checks run across the whole tree** — its lint, type checks, test suite,
   build or gate runner, as scenarios calling the project's own commands, per
   `../VERIFICATION_HARNESS.md` → *Build on what exists*, which also offers a scenario for each
   verification command the context file names that no recipe runs, so the file teaches one way in.
6. **The context-file bullet** — v6's wording from `../NORTH_STAR_FORMAT.md` → *The
   project-surfaces section*: unmarked recipes are free to run as often as they help, the
   ask-first reason is cost, never time, and the evidence a change rests on comes through the
   command while the project's own commands stay usable while iterating.

Once every item has an answer, record v6.
