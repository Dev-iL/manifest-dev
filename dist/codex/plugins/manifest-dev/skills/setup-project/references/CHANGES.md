# Surfaces versions

What each surfaces version gives a project that setup-project has set up. A project's context
file records the version it carries in its project-surfaces section; an update offers the
entries after that version, each on its own, and records the newest version once the user has
answered them.

## v1

- Decision records gain an `Enforced by` field naming the strongest check that holds the
  decision, or `not yet` with the check a later run builds. It is editable in place, and superseding or narrowing a record retargets or
  retires the old record's check.
- The project-surfaces section records its surfaces version and gains an entry for the
  project's verification surface, telling every contributor that a change to what an entry
  covers updates and exercises that entry.
- A verification surface is seeded for each artifact future runs will change: its form and
  location, existing verification assets adopted within the scope the project gave them,
  entries catalogued from source as `unverified` (`unmeasured` for an eval suite), its README,
  and a repository check that its entries still point at things that exist.

Digest: da90c4ccd748aa536d84461ee3530690097de3080a519644f9e1437fb5d880da

## v2

- A setup-project run audits the whole setup against what the references describe, whatever
  version the project records, and offers each gap on its own; what changed since the recorded
  version is marked new. An accepted gap in an existing verification surface is handed to a
  normal run instead of being built during setup.
- A verification surface is judged fit to trust by its jobs — a cold proof run of one entry,
  a health check, isolation, the real path exercised — not by its tooling, and setup drives one
  entry end to end before handover or says which entry it could not drive.
- The feature map takes a fixed shape: an index carrying baseline preconditions, driving
  conventions and proof and skip rules, and one file per feature with a `Status:` line and the
  sections `Sub-features`, `How to get to it (user POV)`, `Driving it`, `How it is checked` and
  `Gotchas`, with a worked example. It covers whatever users invoke — a plugin's skills included
  — not only a runnable app, and gains an `unreachable` status naming the missing prerequisite;
  the surface README template gains that status, and the project-surfaces section gains a
  feature-map entry where the map is not already the verification surface.
- The ADR conventions state that only an `Accepted` record is in effect, and that backfilling
  `Enforced by`, building a `not yet` check, and citing a record as a ruling read only records
  in effect.

Digest: 973cb32f0ae0beb4afb70511c1e39532a217cac3381a5443e3d3504411ed470b
