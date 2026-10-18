#!/usr/bin/env bash
# Scratch copy of this repository at the commit carrying the v4 guidance, its surfaces still at v3.
# A drive passes the checkout's path as DRIVE_CHECKOUT and runs this in the scratch project.
set -euo pipefail
git -C "${DRIVE_CHECKOUT:?run this through scripts/drive-skill.sh --scaffold, which sets DRIVE_CHECKOUT}" archive 9207ee65 | tar -x
