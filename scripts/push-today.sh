#!/usr/bin/env bash
# 사용법: scripts/push-today.sh ["커밋 메시지"]
# 변경분을 확인(git status)한 뒤 커밋하고 push한다.
set -euo pipefail
cd "$(dirname "$0")/.."
git status --short
msg=${1:-"TIL: $(date +%F)"}
git add -A
git commit -m "$msg"
git push -u origin HEAD
