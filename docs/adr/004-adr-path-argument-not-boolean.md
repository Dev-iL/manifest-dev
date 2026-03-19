# ADR-004: Make --adr accept a directory path instead of being a boolean flag

## Status
Accepted

## Context
The initial design used `--adr` as a boolean flag with ADR files written to `/tmp/adr-{timestamp}/`. During implementation, the user provided feedback: "Following the --adr flag should be a folder path where to put said file(s)." This made the output location explicit rather than assumed, removing ASM-4 (assumption about /tmp output being acceptable).

## Decision
Change `--adr` from a boolean flag to `--adr <path>` where the path is the directory where /done writes final ADR files.

## Alternatives Considered
- **Boolean flag with configurable default**: `--adr` enables ADR generation, separate config for output path. Rejected because: two-step configuration for a single feature is unnecessary complexity.
- **Boolean flag with /tmp default**: Original design. Rejected by user feedback — users want control over where ADR files land, especially since ADRs are meant to be committed to the repo (unlike manifests which are working files).

## Consequences

### Positive
- Users control exactly where ADR files are written — natural for repo-committed ADRs (e.g., `docs/adr/`)
- Eliminates an assumption (ASM-4) — output location is explicit intent, not a default
- Single flag handles both "enable" and "where" — no separate configuration

### Negative
- Slightly more complex flag parsing (path value instead of boolean)
- /do no longer accepts --adr (it inherits from manifest metadata) — this was caught and fixed during verification

## Source
- Manifest: /tmp/manifest-20260319-adr.md (Amendment during D1 execution)
- Decided during: /do (user feedback)
