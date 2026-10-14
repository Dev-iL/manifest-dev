# setup-project

Installs a project's surfaces — North Star, glossary, ADR conventions, a verification surface, and the context-file wiring with its surfaces version — seeding them from history, and on a set-up project audits the whole setup against what its references describe and offers each gap.

Status: verified (2026-10-14); not driven: the description phrases, figure-out's offer

## Sub-features

- `install` — a project with no surfaces gets all of them
- `no-mine` — `--no-mine`: wiring and verification surface without mining history
- `update-audit` — a set-up project: each gap the project needs now offered on its own, what changed since the recorded version marked new
- `verification-surface` — seeds the surface and drives one entry, or says which could not be driven
- `surface-parts` — an existing verification surface is offered only missing parts; its harness grows with later work
- `empty-input` — a repository with nothing: wiring only

## How to get to it (user POV)

- `/setup-project [--no-mine]`.
- Phrases its description matches: "set up the project", "bootstrap ADRs", "check whether the setup is sound".
- figure-out's docs mode offers it: no surfaces at all, a missing or older surfaces version, or a broken surface met on the way.

## Driving it

Preconditions: the baseline in the index; a prompt file starting `/manifest-dev:setup-project`, followed by whether the user accepts every item; the scaffold of case `30` (no version), `47` (one behind) or `45` (current) under `claude-plugins/manifest-dev/evals/`.

- **Update one version behind.** `scripts/features/drive.sh setup-project <prompt> --scaffold claude-plugins/manifest-dev/evals/47-update-offer-from-previous-version --max-turns 80`, accepting every item. The report lists what it offered, applied and declined; the context file ends at the newest version; the summary's files include `verify/features/README.md` and the reshaped feature files.
- **Audit a current project.** The same with case `45`. It offers gaps item by item though the version is current, and backfills `Enforced by` only on records in effect.
- **Install.** The same with no `--scaffold`. `docs/adr/CONVENTIONS.md`, `CONTEXT.md`, `NORTH_STAR.md` and `docs/NORTH_STAR_CONVENTIONS.md` exist, and the context file carries the newest version line.
- **Proof.** The drive's summary under `docs/features/evidence/setup-project/`. Nothing was written that the run did not offer and accept.

## How it is checked

`tests/test_setup_project_versions.py` (a change to an emitted file ships a new version) and `tests/test_project_conventions_forks.py` (this repo's copies match the defaults); behavior cases `30`, `45`, `47` cover figure-out's offer of it, not a setup run. Drive evidence: `docs/features/evidence/setup-project/20261014T061913Z.md`.

## Gotchas

- It writes many project files and changes every later session's context. Scratch directory only.
- It never overwrites a project-owned copy: differences are offered, not applied.
- It offers no harness or drive work for an existing surface; that comes from the change that needs it.

Source: `claude-plugins/manifest-dev/skills/setup-project/SKILL.md`.
