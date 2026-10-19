# ADR: Verification asks whether a check can reach the case that breaks, and names the kind of check

## Status
Accepted

## Area
Task guidance

## Decided by
The user

## Context
figure-out and define settle how a change will be verified before it is built, and both lean on
example tests. Some correctness depends on the order of events — two writers, a retry, a crash
halfway — or must hold for every input, and example tests rarely reach the case that breaks it.
Formal methods reach those cases, since a model checker explores every order of events within a
bound, and a model of manifest-dev's own ticket protocol found a stall and a duplicate record that
the review had missed. The question was how much of that to bring into the shipped prompts.

## Decision
- Where correctness depends on the order of events or holds for every input, verification design
  asks whether example tests can reach the case that breaks, and where they cannot, uses the
  cheapest check that can: generated inputs or call sequences on the real code, then a model
  checker for an order-dependent design, then a verifier on the code where the language has one,
  and a proof only where no bound is enough. That check becomes a recipe or a test like any other.
- A design whose correctness depends on the order of events is modeled in scratch and the model
  checked before the design is built; what the model finds becomes design decisions and gates.
- The shipped prompts name the question and the kind of check, never a tool or a specification
  language.
- The changes go into the existing task files' probes and Defaults, in figure-out and define
  alike, as their mirror pairs require. No skill is added, and nothing model-checks a Manifest's
  own text.

## Alternatives Considered
- **A formal-verification skill**: a new skill a person must know to reach for,
  against the North Star's "nothing to memorize"; the question in the probe reaches every coding
  task instead.
- **Name the tools (TLA+, Kani, property-testing libraries)**: concrete, but fits one stack each
  and dates quickly, where the question fits every stack.
- **Translate a Manifest's gates into a formal language and check them**: the translation of prose
  into logic is the unreliable step, and a proof over a wrong translation looks like strong
  evidence while proving nothing.

## Consequences

### Positive
- Order-dependent and every-input designs get a check that can fail on the case that breaks them.

### Negative
- A model in scratch costs time before building, and drifts unless it is kept as a check.
- Which check is cheapest stays the run's judgment.

## Enforced by
partly — eval case `56-order-dependent-design` measures figure-out's half once run; that no
shipped line names a verification tool or specification language stays judgment.

## Source
- Session: figure-out and define reviewing manifest-dev's verification practice, and a model of
  the ticket protocol (2026-10-19).
- Related: see also 20261019-a-model-checks-the-ticket-protocol-against-the-prose-it-quotes,
  20261019-a-check-counts-only-after-it-was-seen-to-fail
