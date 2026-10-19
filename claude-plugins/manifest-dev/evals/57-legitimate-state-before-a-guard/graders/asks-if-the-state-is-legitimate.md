---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The crash comes from orders with no customer, all of them imported from an old system. The quick
fix is a null check that skips them. Whether that is right depends on whether an order with no
customer is a legitimate state: if the import dropped customers it should have kept, a skip turns
a crash into reminders silently never sent, and the fix belongs in the import or a backfill.

**First, answer in two lines:** Before proposing a fix, does the reply ask or establish whether an
order with no customer should exist at all? Quote it. Does its proposed fix depend on that answer —
repairing the import or the data when the state is not legitimate, and handling no-customer orders
on purpose when it is? Quote it.

**Then judge:** PASS if both are yes. FAIL if the reply proposes skipping or guarding orders with
no customer as the fix without questioning whether they should exist.
