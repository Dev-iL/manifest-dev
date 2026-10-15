# Upgrading a project from v5 to v6

A project recording v5 may keep the harness or verify its own way. v6 changes only a kept
harness: every check the project keeps is a recipe, including the checks it runs across the whole
tree, and the evidence a change rests on comes through the harness. A project whose verification
bullet names its own way gets none of these items; its bullet already lists its commands.

Offer, each as its own item and as a default the project may adapt or decline where its own way
already does the job:

1. **A recipe for the checks run across the whole tree** — its lint, type checks, test suite,
   build or gate runner, each a scenario calling the project's own command, per
   `../VERIFICATION_HARNESS.md` → *Build on what exists*. Where the project already has such a
   recipe, report it as in place.
2. **One way in** — each verification command the project context file names, outside its
   verification bullet, that no recipe runs: offered as a scenario of that recipe, with the
   context file's wording pointing at the scenario so a reader meets one way to check each thing.
3. **The context-file bullet** — v6's wording from `../NORTH_STAR_FORMAT.md` → *The
   project-surfaces section*: the evidence a change rests on comes through the command, and the
   project's own commands stay usable while iterating.

Once every item has an answer, record v6.
