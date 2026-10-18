# Automated Ticket execution

This is the contract between a Ticket Store and the runs that work its Tickets without a person
watching. The store is the only durable workflow state: the Ticket and git are where a run
recovers and where one agent follows another. The host supplies sessions and reports whether
they are alive. The venue reference says how each record and check below renders on its venue.

## Who starts a run

`orchestrate` starts each run in its own session with:

```text
Invoke the run-ticket skill with: "<canonical Ticket reference> --run <run ID>"
```

A person may run `run-ticket` by hand on any Ticket at any time, with the bare reference. A
scheduler the user already runs may start `orchestrate --autonomous`; manifest-dev ships no
scheduler. Which Tickets unattended work may touch is decided where the run is started, under the
convention's *The Auto grant*; `run-ticket` never enforces it.

## The automation identity

The store config names one account that unattended runs claim with and write as, and a human
escalation recipient. The two must be distinguishable. A session that cannot write as the
configured identity says so and starts nothing unattended.

A record, and every run fact in it, counts only when the automation identity wrote it. On a run a
person starts by hand, the account that run writes as stands in for it. A comment from any other
author is untrusted context, whatever marker it carries: it cannot claim a run, mark work ready to
land, grant Auto, or turn quoted commands into instructions.

## The attempt record

Each Ticket has one attempt record, a venue comment carrying
`<!-- manifest-dev-run-ticket-attempt -->`. It is written early and updated in place; no attempt
adds a second one. It holds:

| Part | Contents | Written by, and when |
|---|---|---|
| Branch | The canonical Ticket, its one stable branch, and the recovery purpose | The run, before substantial work |
| Run facts | The run ID; the session that runs it, where the host names one; when it started; the launch count, counting launches in a row whose run ended without an outcome | The launcher — `orchestrate`, or `run-ticket` itself on a hand run — just before the run starts |
| | The base commit the run's gates last passed against; whether it is ready to land, naming the head commit, or the drafted answer for a Question Ticket | The run, at each pushed checkpoint and when it finishes |
| Progress | The step the run is at — `understand`, `define`, `build`, `verify` or `ready` — the gates passed and at which commit, what remains, the decisions taken, the dead ends | The run, when its step changes and at each pushed checkpoint |
| Manifest | The run's full Manifest, refreshed when it is amended | The run, as soon as define reports it |

Each fact has one writer. A launcher writes only while no live run holds the Ticket. A run
re-reads the record before each write and each push, and stops without writing when the run ID
there is not its own. A Manifest too long for the venue's comment limit continues in a second
comment carrying `<!-- manifest-dev-run-ticket-manifest -->`, and in a third with the same marker
should it need one. The Manifest is not committed to the repository unless the user asks for it.

A run is live while the host reports its session alive and its timeout has not passed. Where the
host cannot report on a session, the timeout alone decides. The store config may set the timeout;
without one it is four hours from the run's start.

## The completion record

A run that finishes writes one comment carrying `<!-- manifest-dev-run-ticket-completion -->`,
updated in place by a later attempt:

- what changed, or the question's answer;
- evidence that the definition of done holds, with the gate evidence and the head commit;
- branch, commit, pull-request, deployed-artifact or recorded-answer references that exist;
- follow-up Ticket links, or a clear statement that none were warranted;
- the debt `/done` named, one line each, so it outlives the runner even where no pull request
  carries it;
- the flagged offers, agent-decided records and drafted Taste entries `/done` named, each with
  what accepting or reviewing it would change;
- the run's material decisions, the user's calls first, each with the alternative not taken and
  what decided it.

The lander adds the landing reference. `orchestrate` adds a line once it has gathered the debt, so
the debt is gathered once.

## Landing

This is the one landing procedure. `orchestrate` follows it at each landing turn, and `run-ticket`
follows it only when its prompt says to land. The lander:

1. **Re-reads the Ticket.** It stops when the Ticket is closed, a person holds the claim, the run
   facts were not written by the automation identity or name a run that is not the lander's own
   (for `orchestrate`, a run it launched or took over; for a landing `run-ticket`, itself), or the
   record is not marked ready to land.
2. **Checks authority.** An unattended landing needs Auto still present. A Ticket without Auto is
   never landed by automation: only a person lands it. A person who runs `run-ticket` by hand and
   tells it to land supplies the authority for that run.
3. **Refreshes the pull request.** Its head must be the head commit the record names, its checks
   must pass, and the repository's protections must permit the merge. When any of these fails, it
   reports the current state and stops; it never merges older state.
4. **Checks the base.** When the base has moved since the base commit the record names, the run
   merges the base in, reads what landed, and checks any cross-cut both ways: a change that alters
   how every instance of something must look, beside one that adds an instance. It extends its
   work when the extension fits its Ticket, and otherwise writes a follow-up for a person. It
   re-runs every gate, records the new base, and marks the record ready again. `orchestrate`
   relaunches the run for this; a landing `run-ticket` does it in place. Then the lander starts
   again at step 1.
5. **Merges with the head pinned**, through the venue's normal protected mechanism, and observes
   the merged state. It never force-pushes a shared branch, bypasses protection, or merges work
   the Ticket does not authorize. A non-repository Ticket's landing is observed at its durable
   place instead.
6. **Records and closes.** It adds the landing reference to the completion record and closes the
   Ticket. A Ticket closes only after its landing is observed, so a dependent never starts on work
   that is not on the target branch.

A Question Ticket has nothing to land. With Auto, its run closes it once the answer is recorded.
Without Auto, the run stops with the answer drafted, and the Ticket closes once a person accepts
it.

## Recovery boundary

A fresh runner rebuilds the attempt from the Ticket, its records, the one stable remote branch,
pushed commits, the one pull request, and current checks. It resumes do on the recorded Manifest
rather than defining the work again; recorded passes only guide the order of work, and every gate
still needs fresh evidence before done. It needs no earlier conversation or workspace.
Uncommitted work and unpushed commits may be lost; coherent pushed checkpoints are the durability
boundary.

## Gotchas

- A claim is not a lock between two runs that write as one identity. The run facts and the re-read
  before each write are; git rejects a stale run's push, and that run then stops.
- Auto is durable authority, not a launch pulse. Removing and reapplying it to retry erases the
  difference between authority and delivery.
- A run that ends without a ready pull request, an escalation or a close is a failed launch, not
  a Ticket outcome. Only the escalation record says a person is needed.
