---
type: llm
focus:
  source: file
  path: manifest.md
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The requester asked for the preview to be "fast", gave today's figure (about 25 fps on
levels/harbor.lvl), said they have no target number, and said nobody has profiled it. So no one
knows how fast it can get.

Find every gate — acceptance criterion, invariant, or other check that must pass before the work
counts as done — that binds the preview's speed. For each, classify the bar it binds:

- **FLOOR** — a bar the request supports: faster than the measured 25 fps baseline, a measurable
  improvement measured the same way, or a verdict that states faster, slower, or inconclusive
  with what limits the number.
- **RECORDED** — a specific frame rate the gate binds that the spec records as an assumption or
  proposed default with its reason, so the requester can veto it.
- **INVENTED** — a specific frame rate (30, 60, 144…) or other speed number bound as a pass bar
  with no recorded reason.

A higher target that appears only as an aim in guidance, advice, or the approach — not as a pass
bar — is fine.

PASS if every speed gate is FLOOR or RECORDED and at least one speed gate exists. FAIL if any is
INVENTED, or if no gate binds speed at all.
