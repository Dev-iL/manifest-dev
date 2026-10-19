---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The design's correctness depends on the order of events: two workers taking the same job at the
same moment, and a worker killed between sending the email and marking the job sent. Example tests
rarely reach those orders.

**First, answer in one line:** Does the reply propose modeling the design — its states and steps,
explored across the orders in which two workers and a crash can interleave, by a model checker or
an equivalent exhaustive exploration — before the design is built, and say what the model would
check (no invoice sent twice, none left unsent)? Quote it.

**Then judge:** PASS if yes. FAIL if the reply goes from the design straight to code and tests, or
mentions modeling only as an optional afterthought with nothing it would check.
