# Upgrading a project from v3: what v4 gives it

A project recording v3, or reaching it on the path from an older version, carries its
verification in the pre-v4 form: a verification surface (a harness with its feature map, an eval
suite or a reader-task list, with a README, statuses and a repository check), a feature map, a
reader-task list, and the context-file bullets naming them. v4 replaces all of them with one
verification harness, which arrives in the shape `../VERIFICATION_HARNESS.md` describes.

Offer, each as its own item and as a default the project may adapt or decline where its own way
already does the job:

1. **The harness**, per `MOVE_TO_HARNESS.md` beside this file: the tool, `harness.md`, a recipe
   for each entry the old surface carries, each feature-map entry and each reader task, with its
   content and evidence, a recipe for the checks the project runs across the whole tree — its
   lint, type checks, test suite, build or gate runner — calling its own commands
   (`../VERIFICATION_HARNESS.md` → *Build on what exists*, which also offers a scenario for each
   verification command the context file names that no recipe runs), the `ask-first` marks, and
   the removal of the old surface, its directories, its README and its repository checks, except
   an eval suite, which stays as it is. Where the project has none of those pieces and holds
   something future runs will change, recommend a new harness seeded per
   `../VERIFICATION_HARNESS.md` → *What setup creates, and what runs build* instead; its ask-first
   choice and bullet are the items below.
2. **The ask-first setting** — `ask` by default, or `run`.
3. **The context-file bullet** — the one verification bullet, in the newest wording from
   `../NORTH_STAR_FORMAT.md` → *The project-surfaces section*, replacing the verification-surface
   and feature-map bullets the project carried.
