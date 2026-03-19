# ADR-002: Use memento pattern with a single draft file for ADR state across workflow phases

## Status
Accepted

## Context
ADR generation spans three workflow phases: /define (interview decisions), /do (implementation decisions), /done (finalization). State must persist across these phases, which may run in separate sessions. The existing workflow already uses the memento pattern — discovery logs for /define, execution logs for /do — to externalize state to files.

## Decision
Use a single ADR draft file (`/tmp/adr-draft-{timestamp}.md`) as the shared state. /define creates and populates it, /do appends to it, /done reads and finalizes it into individual ADR files. The draft file path is stored in the manifest's Intent & Context metadata so downstream phases auto-discover it.

## Alternatives Considered
- **Embed ADR drafts directly in the manifest**: Would keep everything in one file but bloats the manifest with non-verification content. The manifest is consumed by /verify agents — ADR drafts would be noise.
- **Use the discovery/execution logs directly**: /done could synthesize ADRs from raw logs at finalization time. Rejected because: the raw logs are noisy (contain all decisions, not just ADR-worthy ones), and the decision-worthiness filtering would need to happen at finalization rather than incrementally, losing the context of why decisions were tagged.
- **Database or structured state file**: Overkill for what is fundamentally a text-accumulation problem in a CLI tool.

## Consequences

### Positive
- Follows established memento pattern precedent — consistent with how the rest of the workflow manages state
- Each phase only needs to know the draft file path (from manifest metadata), not the internals of other phases
- Draft can be inspected mid-workflow for debugging

### Negative
- File-based state is fragile if /tmp is cleaned between sessions (mitigated: /do recreates from manifest if draft is missing)
- Producer-consumer format must be specified explicitly (mitigated: ADR_FORMAT.md defines the draft format as a contract)

## Source
- Manifest: /tmp/manifest-20260319-adr.md
- Decided during: /define
