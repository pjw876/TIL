#!/usr/bin/env bash
# Git Day 1: 세 영역(Working Directory / Staging / Repository)을 눈으로 확인하는 실습
# 사용법: bash three_areas.sh [샌드박스 경로]   (기본: ~/workspace/git-sandbox)
# 주의: TIL 레포가 아니라 별도 샌드박스 레포에서만 실행한다. 이미 있으면 중단.
set -euo pipefail
sb=${1:-$HOME/workspace/git-sandbox}
[ -e "$sb" ] && { echo "이미 있음: $sb (지우거나 다른 경로를 지정)"; exit 1; }

step() { printf '\n=== %s ===\n' "$*"; }

mkdir -p "$sb" && cd "$sb"
git init -q -b main
git config user.name "sandbox" && git config user.email "sandbox@example.com"

step "1. 파일 생성 직후 (Working Directory에만 존재: untracked)"
echo "hello" > a.txt
git status -s

step "2. git add 후 (Staging에 스냅샷이 올라감: A)"
git add a.txt
git status -s

step "3. add 이후에 파일을 또 수정 (staged 버전과 working 버전이 달라짐: AM)"
echo "world" >> a.txt
git status -s
echo "--- git diff (working vs staging)"
git diff
echo "--- git diff --staged (staging vs HEAD)"
git diff --staged || true

step "4. commit (Staging에 있던 것만 Repository에 기록됨. 3번의 수정은 빠짐)"
git commit -q -m "add a.txt (hello)"
git status -s
echo "--- 커밋된 내용 / working 내용"
git show HEAD:a.txt
cat a.txt

step "5. 수정분까지 add + commit"
git add a.txt && git commit -q -m "append world"

step "6. 히스토리"
git log --oneline --graph
