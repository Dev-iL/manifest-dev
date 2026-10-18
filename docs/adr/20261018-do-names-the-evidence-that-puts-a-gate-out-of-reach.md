# ADR: do names the evidence that puts a gate out of reach

## Status
Accepted

## Area
define / do

## Decided by
The user

## Context
`/do` treats an obligation as blocked only when no authorized path remains after credible alternatives, including when it needs a change to a binding requirement (`20260907-executors-own-unattended-decisions-within-explicit-bounds`). For a measured target there is always one more optimization to try, so the alternatives never visibly run out: the run cannot tell "not yet" from "not possible" and keeps trying. A user watched `/do` pursue an FPS target that was never reachable. The rule was right; nothing said what evidence ends the trying.

## Decision
Evidence, never a count of tries, says when a gate is out of reach: a measured limiter that every remaining authorized option leaves in place, recent attempts that no longer move the result beyond its run-to-run noise, or two gates where repairing one fails the other. Any of these makes the gate blocked as needing a change to a binding requirement. Its blocker names the best result reached, the limiter, the attempts made and the requirement change that would unblock it; the bar stays as written. The run then continues independent work and escalates only when none remains, as before.

## Alternatives Considered
- **A cap on attempts**: stop after N tries — Not chosen: N is a number nobody can source, and it stops a run that is still making progress.
- **Let the run lower the bar to what it reached**: — Not chosen: gate text changes only on the user's say-so (`20260727-gate-text-changes-on-the-users-say-so`).
- **Leave it to `/define` alone**: — Not chosen: a floor the user set can still prove unreachable, and only the run's measurements show it.

## Consequences

### Positive
- An unreachable target ends in a blocker with the evidence a person needs to decide, instead of an open-ended run.
- A run still making progress keeps going: the evidence, not impatience, decides.

### Negative
- A run must measure noise and name a limiter before it can stop, which costs a profile it might otherwise skip.

## Enforced by
none — whether a run reads its evidence correctly is judgment; the `do` recipe's `out-of-reach` scenario exercises it.

## Source
- Session: figure-out read and define run on 2026-10-18
- Related: 20260907-executors-own-unattended-decisions-within-explicit-bounds, 20261018-a-target-of-unknown-reach-binds-a-floor-and-advises-an-aim
