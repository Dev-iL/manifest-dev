# setup-project

Installs a project's surfaces — North Star, glossary, ADR conventions, a verification surface, and the context-file wiring with its surfaces version — seeding them from history, and on a set-up project audits the whole setup against what its references describe and offers each gap.

Status: unverified

## Sub-features

- `install` — a project with no surfaces gets all of them
- `no-mine` — `--no-mine`: wiring and verification surface without mining history
- `update-audit` — a set-up project: each gap against the references offered on its own, what changed since the recorded version marked new
- `verification-surface` — seeds the surface and drives one entry, or says which could not be driven
- `hand-off` — an accepted gap in an existing verification surface becomes a Ticket or a `/define`
- `empty-input` — a repository with nothing: wiring only

## How to get to it (user POV)

- `/setup-project [--no-mine]`.
- Phrases its description matches: "set up the project", "bootstrap ADRs", "check whether the setup is sound".
- figure-out's docs mode offers it: no surfaces at all, a missing or older surfaces version, or a broken surface met on the way.

## Driving it

Preconditions: the baseline in the index; a scratch directory from `claude-plugins/manifest-dev/evals/30-update-offer-for-older-setup/scaffold.sh` (no version), `47-update-offer-from-previous-version` (one behind) or `45-current-setup-offers-nothing` (current).

- **Install.** From an empty scratch git repository, `/setup-project`. `docs/adr/CONVENTIONS.md`, `CONTEXT.md`, `NORTH_STAR.md`, `docs/NORTH_STAR_CONVENTIONS.md` exist and the context file carries `<!-- setup-project surfaces vN -->` with the newest N.
- **Audit a current project.** Scaffold case `45`, then `/setup-project`. It offers gaps item by item even though the version is current, and backfills `Enforced by` only on records in effect.
- **Proof.** Save the transcript and `git -C <scratch> diff`. Nothing was written that the run did not offer and accept.

## How it is checked

`tests/test_setup_project_versions.py` (a change to an emitted file ships a new version) and `tests/test_project_conventions_forks.py` (this repo's copies match the defaults); behavior cases `30`, `45`, `47` cover figure-out's offer of it, not a setup run.

## Gotchas

- It writes many project files and changes every later session's context. Scratch directory only.
- It never overwrites a project-owned copy: differences are offered, not applied.
- Accepting the audit does not build harness improvements; look for a Ticket or a `/define` in the report.

Source: `claude-plugins/manifest-dev/skills/setup-project/SKILL.md`.
