# design

Gives design guidance for a page, app, document, deck, graphic or prototype from the person, their moment and the subject. It guides; building and checking stay with whoever called it.

Status: unverified

## Sub-features

- `direction` — feeling, strength and visual material from person, moment and subject
- `references` — medium-specific guidance loaded as the artifact needs
- `instruments` — optional measurements through `claude-plugins/manifest-dev/skills/design/scripts/design-tools.mjs` (see design-instruments)

## How to get to it (user POV)

- `/design <artifact, brief or file>`.
- Phrases its description matches: "restyle this page", "how should this look and feel".
- figure-out when it renders a draft; eli5; walk-pr's canvas mode.

## Driving it

Preconditions: the baseline in the index; a brief, or an HTML file in a scratch directory.

- **Guide.** `scripts/features/drive.sh design <prompt>` with `/manifest-dev:design <brief>`. Guidance that names the person, the moment and the chosen direction.
- **Proof.** From the drive's summary and its full evidence. It produced guidance and did not claim to have built or verified anything.

## How it is checked

`tests/test_design_standalone.py` keeps it self-contained and free of delegation; the instruments have their own entry.

## Gotchas

- "It didn't build the page" is intended.
- Its instruments measure; they do not score quality.

Source: `claude-plugins/manifest-dev/skills/design/SKILL.md`.
