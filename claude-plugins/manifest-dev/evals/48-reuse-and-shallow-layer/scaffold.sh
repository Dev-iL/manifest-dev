#!/usr/bin/env bash
set -euo pipefail
mkdir -p src tests
cat > README.md <<'EOF'
# Shelfnote

Command-line tool that tracks books a reading club has borrowed.

    python -m shelfnote checkout --member ana --book "Middlemarch"
    python -m shelfnote return --book "Middlemarch"
    python -m shelfnote overdue
EOF
cat > src/shelfnote.py <<'EOF'
import argparse
from store import load_loans
from loans import overdue_loans


def main(argv=None):
    p = argparse.ArgumentParser(prog="shelfnote")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("checkout"); c.add_argument("--member"); c.add_argument("--book")
    r = sub.add_parser("return"); r.add_argument("--book")
    sub.add_parser("overdue")
    args = p.parse_args(argv)
    if args.cmd == "overdue":
        for loan in overdue_loans(load_loans()):
            print(f'{loan["member"]}\t{loan["book"]}\t{loan["days_overdue"]} days')


if __name__ == "__main__":
    main()
EOF
cat > src/loans.py <<'EOF'
"""Loan rules: when a loan is due and which loans are overdue."""
from datetime import date, timedelta

LOAN_DAYS = 21


def due_date(loan):
    return date.fromisoformat(loan["checked_out"]) + timedelta(days=LOAN_DAYS)


def overdue_loans(loans, today=None):
    """Open loans past their due date, each with `days_overdue`, oldest first."""
    today = today or date.today()
    late = []
    for loan in loans:
        if loan.get("returned"):
            continue
        days = (today - due_date(loan)).days
        if days > 0:
            late.append({**loan, "days_overdue": days})
    return sorted(late, key=lambda l: -l["days_overdue"])
EOF
cat > src/mailer.py <<'EOF'
"""Outgoing email for the club. Every message the tool sends goes through here."""
import os
import smtplib
from email.message import EmailMessage

MEMBERS_EMAIL = {"ana": "ana@example.org", "ben": "ben@example.org"}


def send_to_member(member, subject, body):
    """Email one member by their club handle. Skips members with no address on file."""
    address = MEMBERS_EMAIL.get(member)
    if not address:
        return False
    msg = EmailMessage()
    msg["To"], msg["From"], msg["Subject"] = address, "club@example.org", subject
    msg.set_content(body)
    with smtplib.SMTP(os.environ.get("SMTP_HOST", "localhost")) as smtp:
        smtp.send_message(msg)
    return True
EOF
cat > src/store.py <<'EOF'
import json, pathlib
PATH = pathlib.Path("data/loans.json")
def load_loans():
    return json.loads(PATH.read_text()) if PATH.exists() else []
EOF
cat > tests/test_loans.py <<'EOF'
from datetime import date
from loans import overdue_loans

def test_overdue_excludes_returned_and_sorts_oldest_first():
    loans = [
        {"member": "ana", "book": "A", "checked_out": "2026-01-01"},
        {"member": "ben", "book": "B", "checked_out": "2026-01-10"},
        {"member": "ana", "book": "C", "checked_out": "2026-01-01", "returned": True},
    ]
    got = overdue_loans(loans, today=date(2026, 2, 15))
    assert [l["book"] for l in got] == ["A", "B"]
EOF
