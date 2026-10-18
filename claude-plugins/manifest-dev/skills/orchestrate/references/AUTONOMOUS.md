# `--autonomous`: act until no ready work is left

No plan waits for approval. Show the plan as the record of what starts, then act on it.

## Fill slots

At each check-in, rank the ready work again and fill every free slot, up to `--max-batch` live
runs. Auto Tickets run end to end and land. Tickets without Auto that the convention allows run
up to a ready pull request, or a drafted answer, and wait on the person; they never land here,
and a drafted answer is never accepted here.

Whatever needs the person goes on the list of what waits on them, never into a slot: held pull
requests, escalations, Tickets left alone because their author lacks write access, refactor
proposals, and start lines for deep planning. A planning session needs the person, so this mode
never starts one; its start line waits on the list.

## Grant Auto where the criterion holds

For each Ticket an agent wrote that no grant decision covers yet — the debt Tickets this
orchestrator wrote and the follow-ups runs wrote — apply the convention's grant criterion. Where it
holds, grant Auto through `ticket-up`, naming `orchestrate --autonomous` as the grantor. Where it
does not, record that Auto was withheld and why, and list the Ticket as awaiting a person's grant.
Each Ticket is judged once: a grant a person withdrew stays withdrawn. The run that found the work
never grants it, and a refactor proposal never receives a grant here. A Ticket granted here joins
the ready work at once.

## Stop

Stop when no ready work is left in scope, nothing waits for a landing turn, and no run is live.
Check in a last time, then report what landed, what waits on the person in its order, and the
page's link.
