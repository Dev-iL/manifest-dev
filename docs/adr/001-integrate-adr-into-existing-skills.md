# ADR-001: Integrate ADR generation into existing skills rather than a separate skill

## Status
Accepted

## Context
Issue #43 proposed exporting manifest decisions as Architecture Decision Records (ADRs). The feature needed a home in the codebase. Two approaches were viable: (a) create a standalone `/adr` skill that post-processes manifests, or (b) integrate `--adr` as a flag into the existing /define, /do, /done workflow chain.

The existing workflow already captures decisions in discovery logs and execution logs. ADR generation is fundamentally a synthesis step — transforming existing records into a different format — not a new data collection mechanism.

## Decision
Integrate `--adr <path>` as a flag into /define, /do, and /done rather than creating a separate skill.

## Alternatives Considered
- **Standalone `/adr` skill**: Would provide cleaner separation of concerns and could be invoked post-hoc on any manifest. Rejected because: the issue specifically requests flag-based toggling (`--adr`), a separate skill adds invocation friction, and incremental ADR building (a key requirement) requires hooks into the interview and execution phases that a post-hoc skill cannot access.
- **Hook-based approach**: Use Claude Code hooks to intercept workflow events and build ADRs. Rejected because: hooks are Python scripts suited for gating/validation, not multi-phase synthesis across workflow stages.

## Consequences

### Positive
- ADRs build incrementally as decisions are made — /define captures interview decisions, /do captures implementation decisions, /done finalizes
- Zero additional commands for users — existing workflow, one extra flag
- ADR context propagates automatically via manifest metadata, no re-specification needed

### Negative
- Adds complexity to already-large skill files (mitigated by keeping additions minimal and delegating detail to ADR_FORMAT.md reference file)
- Tighter coupling between ADR feature and core workflow (mitigated by conditional gating — all ADR behavior is no-op without the flag)

## Source
- Manifest: /tmp/manifest-20260319-adr.md
- Decided during: /define
