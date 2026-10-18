# ADR: figure-out and define ask through the host's question capability by default

## Status
Accepted

## Area
define / figure-out

## Decided by
The user

## Context
20261012-figure-out-asks-through-the-hosts-question-capability-on-request kept plain text as
figure-out's default and used the host's question-selection capability only when the user's
instructions asked for it. It rested on the grounds of
20260727-figure-out-adopts-a-default-turn-shape: a reader typed free text through the capability,
it is harness-bound, and a menu invites a rubber stamp. define asks in prose too. In this session
the owner asked for the capability and answered about twenty asks through it: four times choosing
something other than the recommended answer, and five more times adding a note that changed the
design. The menu did not produce a rubber stamp, and the free text typed through it carried real
content. The owner wants it as the default, in define as well, and asked whether asks could be
batched. This decision concerns how the workflow asks, which sits outside what the North Star's
*Diagnosis* names.

## Decision
- When the host offers a question-selection capability, figure-out and define deliver their asks
  through it by default, with the recommended answer as the first option. The rule names the
  capability in universal language, so it binds no harness. Without such a capability, asks stay in
  plain text, and a user's instruction to ask in prose wins.
- figure-out still asks one crux at a time. It batches only asks whose answers cannot change each
  other, because most answers move the next question.
- define batches its key calls, which are mostly independent of each other.
- In plain text, a turn carries one ask: several asks in prose are hard to read and to answer.
- Autonomous runs still never ask, and team mode still asks in its channel.

## Alternatives Considered
- **Keep plain text as the default**: the owner's own use answered its main ground, the rubber
  stamp.
- **Batch freely in figure-out**: saves turns, but an answer that would have changed a later
  question arrives too late to change it.
- **A flag**: one more thing to remember.

## Consequences

### Positive
- Users choose or annotate instead of retyping an answer the run already proposed.
- define's interview takes fewer turns.

### Negative
- The headless eval harness offers no question capability, so the default most users now get is
  not measured; the evals measure the plain-text path.
- A menu can still invite a rubber stamp from a less engaged reader; the recommendation as the
  first option and a free-text answer stay the guard.

## Enforced by
partly — `tests/test_skill_frontmatter.py` — `test_shipped_text_names_no_host_tool` fails if
shipped text names a host's question tool instead of the capability; the default, the one-crux
rule and define's batching stay judgment.

## Source
- Session: figure-out on running unattended Ticket work with many agents at once (2026-10-18).
- Supersedes 20261012-figure-out-asks-through-the-hosts-question-capability-on-request
- Related: amends 20260803-figure-out-turn-carries-one-concrete-claim; see also
  20260727-figure-out-adopts-a-default-turn-shape
