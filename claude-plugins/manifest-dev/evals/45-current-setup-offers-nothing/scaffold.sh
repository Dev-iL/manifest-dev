#!/usr/bin/env bash
set -euo pipefail
mkdir -p docs/adr src tests data
cat > CLAUDE.md <<'EOF'
# Shelfnote

Command-line tool that tracks books a reading club has borrowed.

## Project surfaces

<!-- setup-project surfaces v7 -->

This project keeps its direction, vocabulary, and decision memory in the repo. Read
`NORTH_STAR.md` and `CONTEXT.md` at the start of every session.

- **NORTH_STAR.md** — why this project exists and who it's for.
- **CONTEXT.md** — what words mean here.
- **docs/adr/** — why decisions went the way they did. Write new records per
  `docs/adr/CONVENTIONS.md`.
- **Verification** — how this project checks that its work still does its job: in a scratch copy
  of the repository, run each `python3 src/shelfnote.py` command the README lists and check that
  the loans in `data/loans.json`, or the lines it prints, are the ones the command names. Run them
  before saying a change works and when reproducing a reported problem; a change that needs a
  check none of them has adds one in the same form, and a change that finds one of them broken,
  flaky or slow repairs it. This project verifies its own way by choice: add no separate
  verification tool to it.
EOF
cat > CONTEXT.md <<'EOF'
# Shelfnote

Tracks borrowed books for a reading club.

## Language

**Loan**:
One book lent to one member, from checkout to return.
EOF
cat > NORTH_STAR.md <<'EOF'
# North Star — Shelfnote

## Who it's for

Volunteer organizers of small reading clubs.

— hypothesis: from the README. 2026-05
EOF
cat > docs/adr/CONVENTIONS.md <<'EOF'
# ADR Conventions

Write a record for a decision that shapes the system or would be costly to reverse.

## Template

```markdown
# ADR: [Decision Title]

## Status
Accepted

## Area
[One short label]

## Context
## Decision
## Alternatives Considered
## Consequences
## Source
```

Files are `docs/adr/YYYYMMDD-kebab-case-title.md`. Writing a record is one act: the record,
the restatus of what it changes, and the index.
EOF
cat > docs/adr/README.md <<'EOF'
# Architecture Decision Records

| Date | ADR | Status | Area |
|------|-----|--------|------|
| 2026-05-02 | [Loans are stored in one JSON file](20260502-loans-in-one-json-file.md) | Accepted | Storage |
EOF
cat > docs/adr/20260502-loans-in-one-json-file.md <<'EOF'
# ADR: Loans are stored in one JSON file

## Status
Accepted

## Area
Storage

## Context
A club has at most a few hundred loans.

## Decision
All loans live in `data/loans.json`, written only by `src/store.py`.

## Alternatives Considered
- **SQLite**: more than the club needs.

## Consequences
### Positive
- Nothing to install.
### Negative
- One writer at a time.

## Source
- Session: (none)
EOF
cat > src/store.py <<'EOF'
# Enforces docs/adr/20260502-loans-in-one-json-file.md: the only writer of data/loans.json.
import json, pathlib
PATH = pathlib.Path("data/loans.json")
def load():
    return json.loads(PATH.read_text()) if PATH.exists() else []
def save(loans):
    PATH.write_text(json.dumps(loans, indent=1) + "\n")
EOF
cat > data/loans.json <<'EOF'
[
 {"member": "ana", "book": "Middlemarch", "due": "2026-01-10", "returned": false},
 {"member": "ben", "book": "Persuasion", "due": "2099-01-10", "returned": false}
]
EOF

cat > README.md <<'EOF'
# Shelfnote

Command-line tool that tracks books a reading club has borrowed.

    python3 src/shelfnote.py checkout --member cal --book "Emma"
    python3 src/shelfnote.py return --book "Middlemarch"
    python3 src/shelfnote.py overdue
    python3 src/shelfnote.py export --format csv
EOF
cat > src/shelfnote.py <<'EOF'
import argparse, csv, datetime, json, sys
import store
LOAN_DAYS = 21
def main(argv=None):
    p = argparse.ArgumentParser(prog="shelfnote")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("checkout"); c.add_argument("--member", required=True); c.add_argument("--book", required=True)
    r = sub.add_parser("return"); r.add_argument("--book", required=True)
    sub.add_parser("overdue")
    e = sub.add_parser("export"); e.add_argument("--format", choices=["csv", "json"], default="csv")
    args = p.parse_args(argv)
    loans = store.load()
    today = datetime.date.today()
    if args.cmd == "checkout":
        due = today + datetime.timedelta(days=LOAN_DAYS)
        loans.append({"member": args.member, "book": args.book, "due": due.isoformat(), "returned": False})
        store.save(loans)
    elif args.cmd == "return":
        open_loans = [l for l in loans if l["book"] == args.book and not l["returned"]]
        if not open_loans:
            sys.exit(f"no open loan for {args.book}")
        open_loans[0]["returned"] = True
        store.save(loans)
    elif args.cmd == "overdue":
        for l in loans:
            if not l["returned"] and datetime.date.fromisoformat(l["due"]) < today:
                print(f'{l["member"]}\t{l["book"]}\t{l["due"]}')
    elif args.format == "json":
        json.dump(loans, sys.stdout, indent=1); print()
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=["member", "book", "due", "returned"])
        w.writeheader(); w.writerows(loans)
if __name__ == "__main__":
    main()
EOF
