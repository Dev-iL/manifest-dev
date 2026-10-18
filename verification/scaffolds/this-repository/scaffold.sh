#!/usr/bin/env bash
# The scratch project is this repository at its last commit. A drive passes the checkout's path
# as DRIVE_CHECKOUT and runs this in the scratch project; uncommitted changes are not in the copy.
set -euo pipefail
git -C "${DRIVE_CHECKOUT:?run this through scripts/drive-skill.sh --scaffold, which sets DRIVE_CHECKOUT}" archive HEAD | tar -x
