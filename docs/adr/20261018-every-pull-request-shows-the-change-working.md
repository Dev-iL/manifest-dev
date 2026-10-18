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
sets. Since version 2.99 (September 2026), the GitHub CLI can attach images and videos to a pull
request's description or comments with `--attach`, through the same upload the web editor uses.

## Decision
- Every Manifest whose work ships through a GitHub pull request carries a Quality Gate: the pull
  request shows the change working. It applies whether `run-ticket` runs the work or not, and it
  lives with define's pull-request gates.
- The top of the description reads in about a minute: what changed and why, how it was shown
  working, the decisions with the user's calls first, and the debt left. Long lists fold.
- The proof comes from runs of the checks the change touches, on a local or dev instance, or on a
  preview deploy where the project's CI already makes one — never production. A user path in a UI
  shows as screenshots, and motion as a short GIF.
- Images are attached to the pull request with `gh pr create`, `gh pr edit` or `gh pr comment`
  and `--attach`, so GitHub stores them as it stores images dropped into the web editor. No branch,
  other repository or service is involved, and nothing needs cleaning up.
- Where the upload is unavailable — a `gh` older than 2.99, GitHub Enterprise Server, or a token the
  upload refuses — the description says the images could not be attached and why, and the proof
  is command output.

## Alternatives Considered
- **Only for `run-ticket`'s pull requests**: every pull request has a reader who needs the proof.
- **A Default instead of a gate**: whether a description shows the change working can be read
  from the pull request, so by the task-file rule it is a gate.
- **Release assets or an external host for images**: an external host adds a service and its
  credentials, and release assets fill the project's release list with screenshots.
- **Upload through a browser session**: relies on undocumented endpoints and session cookies.
- **Commit images on the change's own branch**: puts binaries into the target branch's history.
- **One orphan evidence branch**: works wherever git does, but every clone downloads every pull
  request's images, and the branch sits in the branch list for good.
- **One evidence branch per pull request, deleted at close**: keeps clones clean, but nothing
  deletes it on its own, so every landing path and every evidence push carries a cleanup step.
- **A hidden ref per pull request**: out of the branch list and out of clones, but a hosted agent
  session may push only branches; a test push from one was refused.

## Consequences

### Positive
- A reviewer sees the change work without running it.
- The repository gains nothing to clean up: no branch and no stored files of its own.
- The description stays readable however large the change.

### Negative
- Images need `gh` 2.99 or later, write access to the repository, and a token the upload accepts
  (the one `gh auth login` stores, or a classic personal access token). Without them, a UI change's
  proof is text only, and its description says so.
- GitHub Enterprise Server does not offer the upload yet.
- Images do not render in email notifications or for viewers without access to the repository.
- A change with no runnable surface shows its proof as command output only.

## Enforced by
not yet — a test over define's pull-request task file would fail if the gate loses the
one-minute top of the description, the never-production rule, images attached with `--attach`, or
the stated fallback where the upload is unavailable.

## Source
- Session: figure-out on running unattended Ticket work with many agents at once (2026-10-18).
- Related: see also 20261018-the-harness-commits-no-evidence-and-time-lines-live-in-recipes,
  20261018-orchestrate-lands-and-run-ticket-stops-at-a-ready-pull-request
