# manifest-to-goal

Turns a Manifest into one standalone goal of at most 4,000 characters, for pasting into a goal field with no Manifest file behind it.

Status: unverified

## Sub-features

- `path` — reads a Manifest file
- `inline` — takes Manifest text pasted in

## How to get to it (user POV)

- `/manifest-to-goal <manifest path or text>`.
- Phrases its description matches: "turn this into a goal", "paste into the goal field".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; a Manifest from a define drive.

- **Convert.** `/manifest-to-goal <path>`. One goal block in the reply.
- **Proof.** Save the reply and count its characters. At most 4,000 characters; every gate's threshold survives; nothing new is invented.

## How it is checked

No behavior case or test.

## Gotchas

- A goal that refers back to the Manifest file is the defect it exists to avoid.

Source: `claude-plugins/manifest-dev-tools/skills/manifest-to-goal/SKILL.md`.
