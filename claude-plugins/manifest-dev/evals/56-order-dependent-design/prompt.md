---
# Holds the decision in docs/adr/20261019-verification-asks-whether-a-check-can-reach-the-case-that-breaks.md — that record's Enforced by line names this case; weakening or removing it means updating that line in the same change.
tags: [figure-out]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Read, Glob, Grep, Write, Edit, Bash]
model: opus
runs: 1
---
use the figure-out skill with --autonomous for this.

we send invoices from a jobs table in postgres: one worker polls it, takes a pending job, emails the invoice, and marks the job sent. invoices go out too slowly, so we want to run two or three workers. two workers can poll at the same moment and take the same job, and a worker can be killed halfway — after the email went out but before the job was marked sent. figure out how this should be designed so we can hand it to /define next. i'm afk — work it out and come back with your read, how sure you are, and what it rests on.
