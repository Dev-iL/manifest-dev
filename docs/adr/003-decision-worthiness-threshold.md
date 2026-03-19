# ADR-003: Define explicit decision-worthiness criteria to filter ADR-worthy decisions

## Status
Accepted

## Context
Issue #43 explicitly noted: "not every decision maps to an ADR, as there needs to be some amorphous threshold of how much of a downstream effect a decision has." The manifest workflow captures dozens of decisions per session — quality gates, process defaults, scope choices, architecture decisions. Without filtering, ADR output would be noisy and low-value.

## Decision
Define explicit decision-worthiness criteria in ADR_FORMAT.md with a clear threshold: **downstream architectural impact**. Provide positive examples (architecture choices, trade-off resolutions, scope decisions, constraint decisions, approach pivots) and negative examples (quality gate selections, process guidance defaults, mechanical choices, known assumptions). Include a practical litmus test: "Would a new team member joining in 6 months benefit from knowing WHY this was decided this way?"

## Alternatives Considered
- **Let users tag decisions manually**: Each decision would be presented with "Make this an ADR?" during the interview. Rejected because: it adds cognitive load to every decision, most users can't predict which decisions have downstream impact during the interview, and it conflicts with the autonomous interview style.
- **Record everything, filter later**: Generate ADRs for all decisions and let users delete unwanted ones. Rejected because: it defeats the purpose — the value of ADRs is curation, not completeness. A dump of all decisions is just the discovery log in a different format.
- **AI-only detection with no criteria**: Trust the model to identify important decisions without explicit guidance. Rejected because: without criteria, the model defaults to recording everything (safe choice), producing the same noise problem.

## Consequences

### Positive
- ADR output is curated — typically 2-3 ADRs per manifest rather than 10+
- Criteria are transparent and auditable (in ADR_FORMAT.md), not hidden in model behavior
- The litmus test is intuitive for users reviewing ADR output

### Negative
- Criteria require judgment calls — borderline decisions may be inconsistently classified across sessions
- The threshold may need tuning as users provide feedback on what they find valuable

## Source
- Manifest: /tmp/manifest-20260319-adr.md
- Decided during: /define
