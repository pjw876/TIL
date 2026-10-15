---
start: 2026-10-26
perday: 1
---
# 05. Linux 로드맵 (10일)

- **목표**: 서버에 접속해서 로그를 보고, 프로세스를 관리하고, 자동화 스크립트를 쓸 수 있다
- **하루**: 40분 (개념 10 + 터미널 실습 25 + TIL 5)
- **환경**: WSL2 Ubuntu (이미 사용 중이면 그대로)
- **자료**: The Linux Command Line(무료 책), `man`/`tldr`, OverTheWire Bandit (게임으로 연습)
- **TIL 카테고리**: `CS/`

---

- [ ] **Day 1 · 파일 시스템과 기본 명령** — `/`, `/etc`, `/var/log`, `/home`, `pwd/ls/cd/cp/mv/rm/mkdir`, 절대/상대 경로
  확인: `rm -rf`를 쓰기 전에 하는 확인 습관 3가지
- [ ] **Day 2 · 권한과 사용자** — `chmod`(숫자·기호), `chown`, `sudo`, 사용자/그룹, 실행 권한
  확인: `755`와 `644`는 각각 무슨 뜻인가?
- [ ] **Day 3 · 텍스트 보기와 검색** — `cat`, `less`, `head`, `tail -f`, `grep -rn`, 정규식 기초
- [ ] **Day 4 · 파이프와 리다이렉션** — `|`, `>`, `>>`, `2>&1`, `sort | uniq -c | sort -nr`, `wc`, `cut`, `awk`, `sed`
  실습: 로그에서 상위 에러 메시지 10개 뽑기
- [ ] **Day 5 · 파일 찾기** — `find`(이름·크기·수정시간), `xargs`, `locate`
- [ ] **Day 6 · 프로세스 관리** — `ps aux`, `top/htop`, `kill`, `jobs/bg/fg`, `nohup`, `tmux`
  확인: SIGTERM과 SIGKILL의 차이는?
- [ ] **Day 7 · 네트워크** — `curl`, `ss -tulnp`, `ping`, `dig`, `ssh` 키 생성과 접속, `scp`
  확인: 포트가 열려 있는지 확인하는 방법 2가지
- [ ] **Day 8 · 환경 변수와 쉘 설정** — `export`, `PATH`, `.bashrc` vs `.profile`, alias, `.env` 다루기
- [ ] **Day 9 · 쉘 스크립트** — 변수, `if`, `for`, 함수, 인자 `$1 $@`, `set -euo pipefail`
- [ ] **Day 10 · 서비스와 스케줄** — `systemd`(`systemctl status`), `journalctl`, `cron` / **미니**: 매일 로그를 압축·정리하는 스크립트를 cron에 등록

---

## 이 정도면 점검 끝

- [ ] 파이프 조합으로 로그 분석 한 줄을 만든다
- [ ] 권한 오류(`Permission denied`)의 원인을 스스로 찾는다
- [ ] 서버에서 프로세스/포트/디스크 사용량(`df -h`, `du -sh`)을 확인한다
- [ ] 안전한 쉘 스크립트 템플릿을 갖고 있다

## 자주 나오는 면접 질문

- 서버가 느릴 때 어떤 순서로 확인하나? (`top` → `free -h` → `df -h` → `ss` …)
- 프로세스와 스레드의 차이?
- 하드 링크와 심볼릭 링크의 차이?
