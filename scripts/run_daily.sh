#!/usr/bin/env bash
set -euo pipefail

export PATH="/home/admin/.local/bin:/usr/local/bin:/usr/bin:/bin"
cd /home/admin/horizon

hours="${1:-24}"
/home/admin/.local/bin/uv run horizon --hours "$hours"

git add -f docs/_posts data/summaries
if ! git diff --cached --quiet; then
  git commit -m "Daily summary $(date +%F)"
  git push origin main
fi
