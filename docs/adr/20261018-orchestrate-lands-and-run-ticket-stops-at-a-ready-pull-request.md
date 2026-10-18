# ADR: orchestrate lands pull requests, and run-ticket stops at a ready one

## Status
Accepted

## Area
Ticketing

## Decided by
The user

## Context
20260812-auto-ticket-completes-after-required-landing made `run-ticket` land its own repository
work: it refreshes the Ticket's authority, its claim, the pull-request head and the repository
state, merges through the protected mechanism, observes the merge, and only then writes DONE and
closes the Ticket. It rejected letting the trigger adapter press merge, because the adapter would
have to duplicate the definition of done and the pull-request and outcome logic. That ruling came
from a time when each run worked alone. With `orchestrate` running many Tickets at once, landing
is where runs meet: who lands next, against which base, and whether a moved base needs a
re-check. A run sees only its own Ticket; the orchestrator sees all of its runs.

## Decision
- `run-ticket` ends at a ready pull request. It writes the full completion record on the Ticket —
  head commit, gate evidence, pull-request reference — marks it ready to land, and exits.
- `orchestrate` lands. In its scope it gives out one landing turn at a time. Before it merges, it
  refreshes the claim, the Auto grant, the pull-request head and the protections, and checks that
  the base has not moved since the run's last check. When the base moved, it relaunches the run to
  merge the base in and re-run its gates. It merges with the head pinned, observes the merged
  state, adds the landing reference to the Ticket, and closes it.
- The landing procedure is written once, in the shared automation reference, so it has one owner.
  A prompt may still tell `run-ticket` to land, and it then follows the same procedure. The owner
  wants this flexible, not fixed.
- A Ticket still closes only after its landing is observed, so dependents never start on work that
  is not on the target branch.
- Where two orchestrators land on one branch, the repository should require up-to-date branches or
  use a merge queue. An orchestrator does not refuse to run without one; its plan names the
  remaining race once.
- A person who runs `run-ticket` by hand gets a ready pull request to merge.

## Alternatives Considered
- **`run-ticket` keeps landing**: the run holds the context to re-check after it merges the base
  in, and a hand run still lands. Recommended in the session and not taken: the owner ruled that
  landing belongs to the actor that sees every run, now that runs land beside each other.
- **`orchestrate` lands its runs and `run-ticket` lands hand runs by default**: two landing paths,
  which can drift apart.
- **Always a human merge**: rejected in 20260812-auto-ticket-completes-after-required-landing for
  Auto Ticket graphs, and still rejected on the same grounds.

## Consequences

### Positive
- Landings in one scope are serialized by the one actor that sees them all.
- `run-ticket` no longer waits through checks and merge observation.

### Negative
- When the base moves after a run is ready, a relaunched run merges it in and re-checks, without
  the first run's context.
- A hand run no longer lands by itself.

## Enforced by
not yet — `tests/test_ticket_automation_prompts.py` would retarget
`test_run_ticket_recovers_and_lands_before_done` to fail if `run-ticket` stops at anything but a
ready pull request with its record marked ready to land, and would fail if `orchestrate`'s landing
loses the refresh before merge, the unchanged-base check, or closing only after the merge is
observed.

## Source
- Session: figure-out on running unattended Ticket work with many agents at once (2026-10-18).
- Related: amends 20260812-auto-ticket-completes-after-required-landing; see also
  20261018-an-orchestrating-skill-runs-the-queue-and-replaces-the-sweep,
  20260812-run-ticket-owns-attempt-not-dispatch
