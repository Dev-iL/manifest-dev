---
type: llm
focus: last_message
weight: 1
---
Work through the steps below privately, without writing them out. Your entire reply is one word:
PASS or FAIL.

The project already has `src/loans.py` with `overdue_loans(loans, today)`, which returns the open
overdue loans with their days overdue, and `src/mailer.py` with `send_to_member(member, subject,
body)`, the one place the tool sends email. The user proposed a new `reminders.py` with a
ReminderService class whose methods `get_overdue()`, `compose()` and `send()` would mostly forward
to those two functions.

**First, list** what the reply proposes the remind feature should be built from.

**Then judge.** PASS only if both hold:
- The reply reuses `overdue_loans` and `send_to_member` (or names them as what the feature calls)
  rather than proposing new code that recomputes overdue loans or sends email another way.
- The reply questions or drops the forwarding class: it says the class would mostly forward, is a
  shallow or pass-through layer, or proposes a shape without it (for example the command calling
  the two functions plus a small function that composes the message).

FAIL if either is missing, or if the reply has already written implementation code.
