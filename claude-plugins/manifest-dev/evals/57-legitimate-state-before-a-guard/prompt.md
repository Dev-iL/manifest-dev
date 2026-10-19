---
tags: [figure-out]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Read, Glob, Grep, Write, Edit, Bash]
model: opus
runs: 1
---
use the figure-out skill with --autonomous for this.

our nightly reminder job crashes with `AttributeError: 'NoneType' object has no attribute 'email'` on the line `send_reminder(order.customer.email, order.total)`. it only happens for orders imported last month from our old shop system; every other order has a customer. we need the job running again. figure out the fix so we can hand it to /define next. i'm afk — work it out and come back with your read, how sure you are, and what it rests on.
