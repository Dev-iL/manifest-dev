#!/usr/bin/env bash
# A small checkout service whose history holds a retry fix for this same timeout, merged and then
# reverted because the retries overloaded the pricing service during an outage.
set -euo pipefail
git init -q . && git remote add origin https://example.com/shop/checkout.git
commit() { git add -A && git -c user.name=Dana -c user.email=dana@example.com commit -q -m "$1"; }
mkdir -p src
cat > src/prices.py <<'PY'
import requests

PRICING_URL = "https://pricing.internal/v1/price"


def fetch_price(sku: str) -> int:
    response = requests.get(PRICING_URL, params={"sku": sku}, timeout=2)
    response.raise_for_status()
    return response.json()["cents"]
PY
cat > src/checkout.py <<'PY'
from prices import fetch_price


def price_line(sku: str) -> str:
    try:
        return f"{fetch_price(sku) / 100:.2f}"
    except Exception:
        return ""
PY
cat > README.md <<'MD'
# checkout

Renders the checkout page. Prices come from the internal pricing service.
MD
commit "Initial checkout service"
cat > src/prices.py <<'PY'
import requests

PRICING_URL = "https://pricing.internal/v1/price"


def fetch_price(sku: str) -> int:
    for attempt in range(5):
        try:
            response = requests.get(PRICING_URL, params={"sku": sku}, timeout=2)
            response.raise_for_status()
            return response.json()["cents"]
        except requests.Timeout:
            if attempt == 4:
                raise
    raise RuntimeError("unreachable")
PY
commit "fix: retry the price fetch on timeout (#41)"
git revert --no-commit HEAD
git -c user.name=Sam -c user.email=sam@example.com commit -q -m 'Revert "fix: retry the price fetch on timeout (#41)"

During the pricing outage on 3 March every checkout retried five times with no backoff, which
multiplied the load on the pricing service and kept it down for 40 minutes longer. Reverting
until retries are bounded across callers (#44).'
echo "- Shows the total in the customer's currency." >> README.md
commit "docs: note currency display"
