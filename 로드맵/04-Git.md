---
start: 2026-10-15
perday: 1
---
# 04. Git 로드맵 (7일)

- **목표**: 혼자서도 협업에서도 히스토리를 깔끔하게 관리하고, 실수하면 되돌릴 수 있다
- **하루**: 30분 (개념 10 + 실습 15 + TIL 5)
- **자료**: Pro Git 한국어판(git-scm.com/book/ko), Learn Git Branching(시각화 사이트)
- **규칙**: 연습은 **개인 샌드박스 레포**에서만. 조직 레포는 건드리지 않는다.
- **TIL 카테고리**: `CS/`

---

- [ ] **Day 1 · 세 영역과 기본 명령** — Working Directory / Staging / Repository, `init`, `add`, `commit`, `log --oneline --graph`, `diff`, `status`
  확인: `git add`는 정확히 무엇을 하는가?
- [ ] **Day 2 · 브랜치와 병합** — `switch -c`, `merge`, fast-forward vs 3-way merge
  확인: 브랜치는 "복사본"인가? (아니고 커밋을 가리키는 포인터)
- [ ] **Day 3 · 원격 저장소** — `clone`, `remote`, `push`, `pull`, `fetch`, upstream 설정
  확인: `fetch`와 `pull`의 차이는?
- [ ] **Day 4 · 충돌 해결** — 일부러 같은 줄을 두 브랜치에서 수정 → 충돌 마커 읽고 해결 → `merge --abort` 연습
- [ ] **Day 5 · rebase** — `rebase` vs `merge`, `rebase -i`로 커밋 squash/reword
  확인: 이미 push한 커밋을 rebase하면 안 되는 이유는?
- [ ] **Day 6 · 되돌리기** — `restore`, `reset --soft/--mixed/--hard`, `revert`, `reflog`로 날린 커밋 복구
  확인: `reset`과 `revert`는 언제 각각 쓰나?
- [ ] **Day 7 · 협업 워크플로** — GitHub Flow, PR 만들기·리뷰 코멘트 반영, 커밋 메시지 규칙(Conventional Commits), `.gitignore`, `git stash`

---

## 이 정도면 점검 끝

- [ ] 충돌을 두려움 없이 해결한다
- [ ] 잘못된 커밋/reset을 `reflog`로 복구해 본 적이 있다
- [ ] merge와 rebase의 차이와 선택 기준을 설명한다
- [ ] 의미 있는 단위로 커밋을 쪼개고 메시지를 쓴다

## 자주 나오는 면접 질문

- merge와 rebase 중 무엇을 선호하고 왜?
- 실수로 `reset --hard` 했다면?
- 브랜치 전략(Git Flow vs GitHub Flow vs Trunk-based) 비교?
