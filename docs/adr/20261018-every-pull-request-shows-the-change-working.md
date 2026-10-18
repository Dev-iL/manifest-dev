# ADR: Every pull request shows the change working

## Status
Accepted

## Area
PR lifecycle

## Decided by
The user

## Context
A run's pull request carries its decisions and its debt, and a reviewer judges the change from
its diff. Nothing shows the change working, and nothing keeps the description short: one recent
pull request in this repository changed 297 files, with a description few readers would finish.
A person deciding whether to land a held Ticket, or a reader checking an unattended one, needs
proof that the change works to trust it with minimal review — the bar the North Star's *Promise*
sets. GitHub offers no official way for an agent to attach an image to a pull request.

## Decision
- Every Manifest whose work ships through a GitHub pull request carries a Quality Gate: the pull
  request shows the change working. It applies whether `run-ticket` runs the work or not, and it
  lives with define's pull-request gates.
- The top of the description reads in about a minute: what changed and why, how it was shown
  working, the decisions with the user's calls first, and the debt left. Long lists fold.
- The proof comes from runs of the checks the change touches, on a local or dev instance, or on a
  preview deploy where the project's CI already makes one — never production. A user path in a UI
  shows as screenshots, and motion as a short GIF.
- Images live on one orphan evidence branch, one folder per pull request, linked by commit so the
  links survive later pushes. On a private repository, such links render for viewers with access
  to it, by third-party accounts; this is not yet tested here.

## Alternatives Considered
- **Only for `run-ticket`'s pull requests**: every pull request has a reader who needs the proof.
- **A Default instead of a gate**: whether a description shows the change working can be read
  from the pull request, so by the task-file rule it is a gate.
- **Release assets or an external host for images**: an external host adds a service and its
  credentials, and release assets rest on a path less documented than plain files on a branch.
- **Upload through a browser session**: relies on undocumented endpoints and session cookies.
- **Commit images on the change's own branch**: puts binaries into the target branch's history.

## Consequences

### Positive
- A reviewer sees the change work without running it.
- The description stays readable however large the change.

### Negative
- Each repository that uses it gains one extra branch — plain files that stop no colleague, so the
  North Star's *Never* on requiring adoption holds.
- Images do not render in email notifications or for viewers without access to the repository.
- A change with no runnable surface shows its proof as command output only.

## Enforced by
not yet — a test over define's pull-request task file would fail if the gate loses the
one-minute top of the description, the never-production rule, or images on the evidence branch.

## Source
- Session: figure-out on running unattended Ticket work with many agents at once (2026-10-18).
- Related: see also 20261018-the-harness-commits-no-evidence-and-time-lines-live-in-recipes,
  20261018-orchestrate-lands-and-run-ticket-stops-at-a-ready-pull-request
