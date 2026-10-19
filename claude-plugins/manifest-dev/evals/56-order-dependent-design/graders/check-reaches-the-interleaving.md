---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

Two failures here depend on timing: two workers taking one job, and a crash after the email but
before the job is marked sent. A handful of example tests, or running two workers on staging for a
while, will usually not hit either.

**First, answer in two lines:** Does the reply say that ordinary example tests are unlikely to
reach these interleavings? Quote it. Does it propose a check that can reach them — generated or
controlled sequences of the workers' steps run against the real code, a model checker over the
design, or a forced crash at each step — rather than only example tests? Quote it.

**Then judge:** PASS if both are yes. FAIL if verification is example tests, a load test, or
"watch it in staging" alone.
