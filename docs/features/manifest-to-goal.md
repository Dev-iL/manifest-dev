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

- **Convert.** `scripts/features/drive.sh manifest-to-goal <prompt> --tools` with `/manifest-dev-tools:manifest-to-goal` and a Manifest pasted inline. One goal block in the reply.
- **Proof.** From the drive's summary and its full evidence. At most 4,000 characters; every gate's threshold survives; nothing new is invented.

## How it is checked

This entry's recipe, driven through `scripts/features/drive.sh`; `tests/test_skill_frontmatter.py` and `tests/test_entry_points.py` hold that the skill parses and stays in the declared set. No behavior case measures it.

## Gotchas

- A goal that refers back to the Manifest file is the defect it exists to avoid.

Source: `claude-plugins/manifest-dev-tools/skills/manifest-to-goal/SKILL.md`.
