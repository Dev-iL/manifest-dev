# eli5

Explains a topic as a dead-simple picture explainer page: big pictures, few words.

Status: unverified

## Sub-features

- `explainer` — one HTML page, styled through design

## How to get to it (user POV)

- `/eli5 <topic>`.
- Phrases its description matches: "explain like I'm five", "a dead-simple picture".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; a host that can write files or Artifacts.

- **Explain.** `scripts/features/drive.sh eli5 <prompt> --tools` with `/manifest-dev-tools:eli5 how a manifest becomes a pull request`. One HTML page whose path or Artifact the reply names.
- **Proof.** From the drive's summary and its full evidence. Nothing the topic needs is hidden behind interaction.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- Without design available it styles by hand; contrast should still read.

Source: `claude-plugins/manifest-dev-tools/skills/eli5/SKILL.md`.
