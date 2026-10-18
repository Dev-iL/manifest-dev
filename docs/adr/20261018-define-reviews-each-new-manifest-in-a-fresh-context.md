# ADR: define reviews each new Manifest in a fresh context before the digest

## Status
Accepted

## Area
define

## Decided by
The user

## Context
`/define`'s own rules already forbid the failures users kept meeting: a specific with no source ("not a number made up to look measurable"), gates that cannot hold together, and a reread of every gate body before handoff. They still slipped through. One user asked in figure-out for a renderer to be "fast"; `/define` bound a fixed FPS number nobody had checked, and `/do` chased it. The context that writes the gates also rereads them, and it reads them as it meant them: it knows the number was a guess, while `/do` reads it cold as a requirement. The digest the user approves shows no gate text, so nobody else read the bound value before execution. The user ran fresh-context reviews of their Manifests by hand — handing the Manifest, `/define`'s instructions, the figure-out log and the transcript to a new context — and those reviews caught invented or too-strict targets, conflicting gates, and points from the session the Manifest dropped. `20260606-harden-figure-out-truth-seeking-inline-defer-independent-pass` had already found that a same-context self-critique shares the converged frame.

## Decision
Every new Manifest gets one review in a fresh context before the digest, attended or unattended. The fresh context is handed the Manifest, `/define`'s rules (its `SKILL.md`, the schema and the task files the session loaded) and the session record (the figure-out log, and the transcript where the host keeps one it can read, else the conversation verbatim). Its brief, `define/references/REVIEW.md`, has it check the Manifest against every one of those rules and against the session, looking hardest at unsourced or too-strict specifics, unestablished targets, gates too loose to settle, gates that cannot hold together, and settled points dropped or changed. It reports findings and never edits; a fix never adds a number the session did not give. The author settles every finding in one pass, and a fix that changes what the user agreed is the user's call. Where no isolated context is available, the author reviews against the brief and says the review was self-graded. The digest also lists every number a gate binds, so the user can veto one before execution. Amendments get no review.

## Alternatives Considered
- **Strengthen the inline rules again**: another sharpening of the sourcing and hold-together bullets — Not chosen: the rules are already stated and were hill-climbed; the failure is self-grading, which more text in the same context does not reach.
- **Review only attended sessions**: save the extra context when no one is present — Not chosen: unattended runs are where no person reads the Manifest before `/do` holds the work to it.
- **Review amendments too**: — Deferred: amendments have not shown the failure; the review can extend to them if they do.
- **Let the reviewer edit the Manifest**: — Not chosen: the author holds the conversation and the user's calls, and a reviewer that edits can make gates stricter unseen.
- **A loop until the review is clean**: — Not chosen: a run that keeps verifying past the point it is satisfied is a defect, and one pass caught the failures in manual use.

## Consequences

### Positive
- Invented numbers, dropped points and conflicting gates are caught by a reader who meets the Manifest the way `/do` will.
- The user sees every bound number before execution.

### Negative
- Each new Manifest costs one more fresh context.
- A thin or unusual Manifest can draw many findings, which the author must triage.

## Enforced by
partly — `tests/test_skill_frontmatter.py` keeps the review's wording host-neutral; whether `/define` runs it and settles its findings is judgment, checked by the `define` recipe's `fresh-review` scenario and the define eval case `d25-vague-target`.

## Source
- Session: figure-out read and define run on 2026-10-18, with the user's manual reviews as evidence
- Related: 20260606-harden-figure-out-truth-seeking-inline-defer-independent-pass, 20261018-a-target-of-unknown-reach-binds-a-floor-and-advises-an-aim, 20261018-do-names-the-evidence-that-puts-a-gate-out-of-reach
