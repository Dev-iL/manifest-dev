---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The skill's rules are a protocol several agents follow on shared state: two agents can claim the
same issue at the same moment, and a takeover can race an agent that was only slow. No single run
of one agent shows those orders of events.

**First, answer in one line:** Does the reply propose checking the rules themselves across the
orders in which several agents' claims, takeovers and merges can interleave — a throwaway model
checked by a model checker, or an equivalent exhaustive exploration — before the skill ships, and
say what it would check (for example, no issue worked by two agents at once, no claimed issue left
stuck)? Quote it.

**Then judge:** PASS if yes. FAIL if the reply goes from the rules straight to writing the skill
and trying it, or mentions modeling only as an optional afterthought with nothing it would check.
