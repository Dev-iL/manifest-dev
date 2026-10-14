# handoff

Writes a self-contained context payload a fresh agent can continue from without re-deriving what this session established.

Status: unverified

## Sub-features

- `new` — writes `~/.manifest-dev/handoffs/handoff-<UTC timestamp>.md`
- `rewrite` — given an earlier handoff's path, writes a fresh one from it

## How to get to it (user POV)

- `/handoff <what the next session is for>`.
- Phrases its description matches: "hand this off", "switching tools", "start a clean session".
- No other skill calls it.

## Driving it

Preconditions: the baseline in the index; a session with some work to hand over.

- **Write.** `/handoff continue the parser migration`. A new file under `~/.manifest-dev/handoffs/` whose path the reply names.
- **Proof.** Save the file. A fresh session given only that file can state the goal, the state and the next step.

## How it is checked

No behavior case or test.

## Gotchas

- The file is outside the repository.
- Passing an earlier handoff rewrites it into a new file; it does not append.

Source: `claude-plugins/manifest-dev-tools/skills/handoff/SKILL.md`.
