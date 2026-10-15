#!/usr/bin/env bash
# 사용법: scripts/new-day.sh <카테고리> <슬러그> [로드맵 표기]
# 예:    scripts/new-day.sh CS python-자료형 "01-Python Day 1"
# 오늘 날짜의 TIL 파일을 템플릿으로 만든다 (이미 있으면 건드리지 않음).
set -euo pipefail
cd "$(dirname "$0")/.."
cat_dir=${1:?카테고리 필요 (CS/AI/SQL/Algorithm)}
slug=${2:?슬러그 필요}
roadmap=${3:-}
file="$cat_dir/$(date +%F)-$slug.md"
[ -e "$file" ] && { echo "이미 있음: $file"; exit 0; }
cat > "$file" <<TPL
# $slug

## 오늘 한 것
- 로드맵: $roadmap
- 실습 코드:

## 배운 것 (핵심 3줄)
-
-
-

## 막혔던 점 / 해결
-

## 확인 질문 답변
Q.
A.

## 내일 할 것
-
TPL
echo "생성: $file"
