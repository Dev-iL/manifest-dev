# ADR Format

Architecture Decision Records capture significant decisions with their context, alternatives, and consequences. Based on the MADR (Markdown Any Decision Records) standard.

## ADR Template

```markdown
# ADR-NNN: [Decision Title]

## Status
Draft | Accepted

## Context
[What situation motivated this decision? What constraints, requirements, or tensions existed?]

## Decision
[What was decided and why this option was chosen.]

## Alternatives Considered
- **[Alternative A]**: [Description] — [Why not chosen]
- **[Alternative B]**: [Description] — [Why not chosen]

## Consequences

### Positive
- [What becomes easier or better]

### Negative
- [What becomes harder or is traded away]

## Source
- Manifest: [manifest file path]
- Decided during: /define | /do
```

## File Naming

`NNN-kebab-case-title.md` — numbered sequentially starting at 001.

Examples: `001-integrate-adr-into-workflow.md`, `002-use-madr-format.md`

## Decision-Worthiness Criteria

Not every decision during a manifest workflow warrants an ADR. The threshold is **downstream architectural impact** — decisions that shape the system's structure, constrain future options, or would be costly to reverse.

### ADR-Worthy (record these)

| Source | What to capture | Manifest elements |
|--------|----------------|-------------------|
| **Architecture choices** | Technology, patterns, component structure, integration approach | Approach → Architecture |
| **Trade-off resolutions** | When competing concerns were weighed and one was preferred | T-* items |
| **Scope decisions with rationale** | Deliberate inclusion/exclusion that shapes the system boundary | Interview decisions with "why not" reasoning |
| **Key constraint decisions** | Invariants established from multiple valid options | INV-G* chosen from alternatives |
| **Approach pivots** | When /do adjusts architecture based on reality | Execution log adjustments with rationale |

### NOT ADR-Worthy (skip these)

| Category | Why not |
|----------|---------|
| **Quality gate selections** | Verification configuration, not architecture |
| **Process guidance defaults** | How-to-work, not system structure |
| **Mechanical choices** | Obvious implementations with no meaningful alternatives |
| **Known assumptions** | Defaults chosen without deliberation — no alternatives weighed |
| **Bug fixes** | Corrections, not decisions (unless the fix involves an architectural choice) |

### Decision Test

When uncertain, apply: *"Would a new team member joining in 6 months benefit from knowing WHY this was decided this way?"* If yes → ADR. If they'd just accept it as obvious → skip.

## Draft File Format

The ADR draft file (`/tmp/adr-draft-{timestamp}.md`) is the shared state between /define, /do, and /done. It accumulates draft ADR entries that /done finalizes into individual files.

### Structure

```markdown
# ADR Draft

Source manifest: [manifest path]

---

## DRAFT-001: [Title]
- **Status:** Draft
- **Decided during:** define | do
- **Context:** [Why this decision was needed]
- **Decision:** [What was chosen]
- **Alternatives:** [What else was considered and why not]
- **Consequences:** [Impact — positive and negative]
- **Log reference:** [Discovery log entry or execution log entry that captured this]

---

## DRAFT-002: [Title]
...
```

### Conventions

- Entries delimited by `---` (horizontal rules) for parsing
- Each entry prefixed with `DRAFT-NNN:` for identification
- **Decided during** tracks origin phase (/define or /do)
- **Log reference** links back to the discovery or execution log entry
- /define creates the file and adds entries from the interview
- /do appends entries when approach adjustments or trade-off applications occur
- /done reads the file and generates individual ADR files from each DRAFT-NNN entry into the output directory specified in the manifest's ADR metadata

## Synthesis Guidance

When generating ADR entries from logs:

**From discovery log**: Look for architecture decisions, trade-off resolutions, and scope decisions where alternatives were explicitly considered. The discovery log's resolution status (`RESOLVED`, `SKIPPED`) indicates which decisions had deliberation.

**From execution log**: Look for approach adjustments with rationale and trade-off applications. The key signal is "changed because" or "preferred X over Y because" — these indicate deliberation.

**Quality over quantity**: A manifest with 10 decisions might produce 2-3 ADRs. The Context and Alternatives sections are what make ADRs valuable — a decision without context is just a fact. If you can't articulate why alternatives were rejected, the decision may not be ADR-worthy.

**Context comes from the interview, not the output**: The most valuable ADR content is the reasoning that happened during /define — user preferences, rejected approaches, constraint trade-offs. This is in the discovery log, not the manifest. The manifest records WHAT was decided; the log records WHY.
