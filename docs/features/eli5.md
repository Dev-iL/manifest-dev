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

- **Explain.** `/eli5 how a manifest becomes a pull request`. One HTML page whose path or Artifact the reply names.
- **Proof.** Save the page and a screenshot of it. Nothing the topic needs is hidden behind interaction.

## How it is checked

No behavior case or test.

## Gotchas

- Without design available it styles by hand; contrast should still read.

Source: `claude-plugins/manifest-dev-tools/skills/eli5/SKILL.md`.
