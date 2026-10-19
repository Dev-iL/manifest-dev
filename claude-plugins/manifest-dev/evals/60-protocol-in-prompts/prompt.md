---
tags: [figure-out]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Read, Glob, Grep, Write, Edit, Bash]
model: opus
runs: 1
---
use the figure-out skill with --autonomous for this.

we're writing a skill that several coding agents run at once against one github issue list. each agent picks an open issue labeled `ready`, claims it by posting a comment "claimed by <agent>", works it on a branch, and closes the issue when its pull request merges. if an agent sees no update on a claimed issue for an hour, it may take the issue over. it's all prompt text — no server, no locks. figure out how the skill's rules should be designed so we can hand it to /define next. i'm afk — work it out and come back with your read, how sure you are, and what it rests on.
