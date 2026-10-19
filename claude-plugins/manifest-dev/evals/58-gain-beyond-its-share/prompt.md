---
tags: [figure-out]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Skill, Read, Glob, Grep, Write, Edit, Bash]
model: opus
runs: 1
---
use the figure-out skill with --autonomous for this.

last sprint we replaced the JSON parser in our reporting dashboard with a faster library. the dashboard's page load went from 2.0 s to 0.8 s at the median over a week. a profile we took a month before the swap showed JSON parsing at about 15% of page load. we want to write this up for the team and make the same swap in our other two apps. figure out whether we should. i'm afk — work it out and come back with your read, how sure you are, and what it rests on.
