# design instruments

Two local command-line tools under the design skills: `design-tools.mjs` measures a supplied HTML page or image (and structured observations) and `design-check.mjs` triages an HTML page. Neither fetches, renders for you, or scores quality.

Status: verified (2026-10-14); not driven: the design skill's instruments reference, review-design's HTML check

## Sub-features

- `catalog` — `design-tools.mjs catalog` lists the instruments
- `inspect` — `design-tools.mjs inspect <HTML|text|observations.json>`
- `image` — `design-tools.mjs image <PNG|JPEG|WebP|GIF|RGBA.json> [--artifacts dir]`
- `appearance` — `design-tools.mjs appearance <image|features.json|->`
- `structured` — `design-tools.mjs journey|data|timeline|survey|content|viewing|palette <JSON>`
- `compare` — `design-tools.mjs compare <report.json> --other <report.json>`
- `design-check` — `review-design/scripts/design-check.mjs <file.html>`: static checks, render checks when Playwright is present

## How to get to it (user POV)

- Run directly with `node` from the skill directory.
- The design skill's instruments reference (`design/references/instruments/usage.md`).
- review-design's step that runs the HTML check.

## Driving it

Preconditions: the baseline in the index; Node 20+; Python 3 for HTML; Pillow for native images; Playwright with Chromium only for design-check's render samples. Commands run from the repository root; `<scratch>` is a directory outside it holding a small `page.html`.

- **Catalog.** `node claude-plugins/manifest-dev/skills/design/scripts/design-tools.mjs catalog`. Exit `0`; JSON with `version` and an `instruments` object.
- **Inspect.** `node claude-plugins/manifest-dev/skills/design/scripts/design-tools.mjs inspect <scratch>/page.html --output <scratch>/inspect.json`. Exit `0`; `inspect.json` has `schemaVersion`, `command: "inspect"`, `coverage` and `observations`.
- **Refuses a URL.** `node claude-plugins/manifest-dev/skills/design/scripts/design-tools.mjs inspect https://example.com`. Exit `1` with `Supply a local artifact; the agent owns acquisition`.
- **HTML check.** `node claude-plugins/manifest-dev/skills/review-design/scripts/design-check.mjs <scratch>/page.html`. Exit `0`; `NOTE`/`OK`/`FINDING` lines, `SKIPPED  render samples` when Playwright is absent, and a closing count line.
- **Proof.** Each command, its exit code and its output, written to a summary under `docs/features/evidence/design-instruments/`. Outputs match the end states above.

## How it is checked

`tests/test_design_instruments.py` (runs `tests/fixtures/design-instruments/test-instruments.mjs`) and `tests/test_design_check.py`; `scripts/design-evals/` is the harness for wider experiments and says what it does not measure. Drive evidence: `docs/features/evidence/design-instruments/20261014T064010Z.md`.

## Gotchas

- Exit `0` means the run completed, findings or not; read the output.
- Without Playwright the render samples are `SKIPPED`, which is not a pass.
- Raster input is capped at 512 px on the long edge.

Source: `claude-plugins/manifest-dev/skills/design/scripts/design-tools.mjs`.
