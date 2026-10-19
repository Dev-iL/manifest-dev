# PROMPTING — probing fuel

Angles that are easy to under-weight when changing a prompt, skill or agent. Considerations, not an agenda. Press the load-bearing ones; priority stays yours. Wording itself is the prompt-engineering skill's, where it is available.

## Blind-spot probes
- **How it gets checked** — Which behaviors does the change owe, and which behavior cases exercise them, judged on what the run did rather than what it reports? Does the project's eval suite already cover them, and which recorded numbers does this change make stale?
- **A protocol on shared state** — Where the prompt sets rules that several runs, agents or people follow on the same state — claims, handoffs, retries, who writes what — can some order of events break them that no single run shows? Would a throwaway model of the rules, checked in scratch with whatever tool fits (such as TLA+ or Alloy) and only as deep as the risk warrants, find it before anything ships — what it finds becoming design decisions and gates, and the model kept as a check only where the protocol will keep changing?
- **A rule in two files** — Does the change state, or contradict, a rule another file already states?
- **An instruction where a check belongs** — Could a test, a lint or a structural check hold this, instead of a line every run has to read and obey — especially anything models do unreliably, like exact counts, long-range recall or a format held over long output?

## Forced trade-offs
- New line vs replacing an old one — does this add a rule beside a vaguer one it should retire?
