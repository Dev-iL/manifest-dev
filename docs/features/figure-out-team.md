# figure-out-team

Runs a figure-out investigation in a Slack channel or thread with several people, owner by Slack handle overruling, with the operator in the local session.

Status: unverified

## Sub-features

- `team` — starts figure-out with `--team` and the given topic
- `no-docs / no-log` — forwarded unchanged to figure-out

## How to get to it (user POV)

- `/figure-out-team [topic] [--no-docs] [--no-log]`.
- Phrases its description matches: "figure out with the team", "press a group asynchronously", "get the team aligned".
- figure-out itself, when a topic needs people who cannot share one chat.

## Driving it

Preconditions: the baseline in the index; Slack access from the session and a channel or thread the run owns.

- **Start.** `/figure-out-team <topic>`, naming the throwaway channel. A first message appears in that channel; the local session reports where it posted.
- **Proof.** Save the channel's messages and the local transcript. Each posted turn carries one ask; nothing posts outside the named channel.

## How it is checked

No behavior case or test covers the team flow; team mechanics live in figure-out's `references/team.md`.

## Gotchas

- Posts reach real people and cannot be unsent. Use a throwaway channel.
- It is a thin wrapper: a team-flow defect is almost always in figure-out's `references/team.md`.

Source: `claude-plugins/manifest-dev/skills/figure-out-team/SKILL.md`.
