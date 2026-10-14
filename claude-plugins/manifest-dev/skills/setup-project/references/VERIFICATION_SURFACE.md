# The verification surface — what it is and how to create one

A verification surface is a project's durable way to check that an artifact still does its job:
built once, kept current by the runs that touch it, and used by every later run instead of each
run working out again how to launch, drive and observe the result. A surface that is wrong is
worse than none, so every part of it says how much it can be trusted.

## When an artifact gets one, and which form

Give a surface to an artifact that future runs will change. One-shot work — a single report, a
throwaway script — is checked in its own run and gets none.

The form follows the artifact:

| Artifact | Form | What one entry covers |
|---|---|---|
| A runnable product — service, CLI, UI, app | A harness plus a feature map | One user-facing feature |
| Prompts, skills, agents | A behavior eval suite | One behavior the prompt owes |
| A living document — README, runbook, guide, or a site or page whose job is to inform | A list of reader tasks, each walked by a reader with fresh context | One task a reader comes to do |

A project with several such artifacts keeps one surface per artifact and lists each in the
project-surfaces section of the context file.

Beside whichever forms it keeps, a project whose artifact people invoke — a product's routes
and commands, a library's public calls, a plugin's skills — keeps one feature map over all of
it, described below. The forms above check an artifact; the map is how a run finds where to go,
and each map entry names the check that holds it.

## Build on what exists

Before writing anything, look for verification assets the project already has: end-to-end
specs, test harnesses, scripts that drive the product, an eval suite, a verification skill,
documented manual checks. Adopt and extend them. A second harness beside an existing one gives
the next run two ways to verify the same thing, and it will pick either.

An adopted asset keeps the scope the project gave it. Setup adds the parts the surface lacks —
statuses, the README, the repository check — and never entries for what that scope leaves out:
an eval suite that covers two skills on purpose is not a gap for every other skill. Where the
asset already has a README, extend that README instead of writing a second one.

## A runnable product: the harness

The harness is a small command-line tool kept with the surface, so a run executes a command
instead of writing a throwaway script each time. It covers:

- **Launch** — start the product from an empty data directory to a state where it is usable,
  not merely answering: migrations, seed data, test users, configuration, and a consistent
  bring-up of whatever it depends on.
- **Doctor** — one read-only check that says whether an instance is worth driving: it is up,
  it runs the expected build, the ports and data belong to this run, auth works.
- **Drive** — the actions a user takes, through stable handles (routes, commands, accessible
  names, data attributes) rather than coordinates or tab order.
- **Debug** — whatever the stack can expose: logs, traces, profiles, console and network
  output. A stack that is hard to observe makes every later run guess.
- **Evidence** — capture the action and the resulting state, side effects included, as files
  that survive cleanup, at a location the harness names, so a person can open them.
- **Cleanup** — remove what this run started, never what it did not, and never the evidence.

Make it easy for an agent to use well: a small composable interface over a lot of capability;
subcommands that reveal functionality a level at a time; `--dry-run` on anything destructive;
rich `--help`; machine-readable output; and errors that say what to do instead. Give the
harness its own checks, so a broken harness fails loudly instead of failing every run that
uses it.

## The feature map

The map lets a run go straight to the right place: place a vague report against a feature,
then reach and drive that feature without working out its entry points again. It describes the
artifact from the user's side only. Where in the code a feature lives is read from the code at
run time; frozen internals are the first thing to go stale. A report that fits no entry is said
so and gets an entry, never a guessed path.

The map is a directory: an index, plus one file per user-facing feature.

**The index** carries what every recipe shares:

- **Baseline preconditions** — the state every recipe starts from: the instance or invocation,
  its data, the tools on the path, the health check that must pass first, and that a run never
  drives an instance it did not start.
- **Driving conventions** — stable handles over positions, commands taken literally, and how a
  mutation is undone.
- **Proof and skip rules** — capture the action and the resulting state, not only the end;
  record the feature and entry point with every piece of evidence; report an entry point that
  could not be driven with the attempt and the unmet prerequisite; and never report an entry
  point as verified because a different one worked.
- **The list of features**, one line each, linking its file.

**Each feature file** opens with a title and one paragraph on what the user sees it do, then a
`Status:` line, then these sections in this order:

1. `Sub-features` — short IDs, one line per behavior.
2. `How to get to it (user POV)` — every entry point: menu path, shortcut, command, trigger
   phrase, or another feature that calls it.
3. `Driving it` — a `Preconditions:` line, then labeled steps pairing each action with its exact
   command and observable result, ending in what proves it works.
4. `How it is checked` — the harness recipe, behavior case, test or reader task that holds it.
5. `Gotchas` — traps that waste or invalidate a run.

An entry carries what a reader cannot get elsewhere: entry points past the obvious one, how to
drive it, what proves it worked, its traps. An entry that restates a description the artifact
already shows its users costs upkeep and guides nobody.

The `Status:` line reads:

- `unverified` — catalogued but not yet driven; not proof of anything;
- `verified (YYYY-MM-DD)` — driven by a run on that date;
- `stale (YYYY-MM-DD): <what differs>` — a run found it drifting from the artifact;
- `unreachable (YYYY-MM-DD): <prerequisite>` — a run tried an entry point and could not reach
  it, naming the prerequisite it lacked and what it tried.

The first build catalogs the artifact from its source — routes, commands, menus, invocable
skills, documented features — and marks each entry `unverified`. That gives the map its
breadth, so a vague report about any feature can be placed. Runs then verify the entries they
exercise. `feature-map-example/` beside this file is a worked map in this shape.

## Prompts, skills, agents: the eval suite

One case per behavior the prompt owes, run against the prompt as shipped, judged on what it
did — files it opened and wrote, what it reported — never on its own account of what it did,
and with no eval wording in what the candidate sees. Each case carries a status:

- `unmeasured` — written but never run; not proof of anything;
- `measured` — run, with the date and the result;
- `stale` — a prompt it covers changed after it was measured, so its numbers no longer hold.

## A living document: the reader-task list

One entry per task a reader comes to the document to do, with what the reader needs to end up
able to do. A check walks each task with a fresh reader that has only the document, and records
where it got stuck. Each entry carries `unverified`, `verified` or `stale`, written as a feature
map writes them.

## Every form

- **A repository check** fails when an entry points at something that no longer exists — a
  route, a command, a selector, a case, a section. It runs with the project's tests, or as a
  script the harness's doctor calls where the project has no test runner, with or without CI, so
  structural drift fails even for contributors who never use this workflow.
- **The surface's own README** says what the surface covers, how to run it, what each status
  means, and how a stale line reads. Emit it from `VERIFICATION_README_TEMPLATE.md` beside this
  file, adapted to the form.
- **Location** — keep the surface with the project, where any runner that checks out the
  repository finds it, and name the location in the project-surfaces section.

## Fit to trust

A surface can have every part and still not be worth trusting. Judge an existing one by the
jobs it has to do, never by how this file would have built it:

- **A cold proof run passes** — one entry, driven end to end from nothing, leaves evidence that
  is still there after cleanup.
- **Health is checkable** — something tells a usable instance from one that merely answers.
- **Runs are isolated** — a run cannot drive a shared instance or another run's data.
- **PASS means the real path** — not mocks past a boundary the product does not isolate, not a
  test-only endpoint, not a skipped entry point counted as another's success.

A surface that fails one of these has a gap, however complete it looks. Scripts instead of one
command-line tool, another test runner, another layout: those are the project's choices, not
gaps.

## What setup creates, and what runs build

Setup seeds the surface: it records the form and location, adopts existing assets, catalogs
entries from source in the form's first status (`unverified`, or `unmeasured` for an eval
suite), writes the README and the repository check, and wires the project-surfaces entry. It
builds harness commands only as far as existing assets already reach. Then it drives one entry
end to end by that entry's own recipe and checks the evidence survives cleanup, setting the
entry's status; where no entry can be driven yet, its report names the entry it tried and what
stopped it. A map nobody has driven reads as proof it is not, so it is never handed over
unsaid. The run that first needs to exercise an entry builds the rest, inside the change that
needs it.
