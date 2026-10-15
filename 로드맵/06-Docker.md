---
start: 2026-11-04
perday: 1
---
# 06. Docker 로드맵 (10일)

- **목표**: 내 서비스(FastAPI + DB)를 컨테이너로 말아서 어디서든 똑같이 실행
- **하루**: 50분 (개념 10 + 실습 35 + TIL 5)
- **선행**: 05-Linux Day 1~7, 01-Python Day 14(FastAPI)
- **자료**: Docker 공식 Get Started, Dockerfile best practices 문서
- **TIL 카테고리**: `CS/`

---

- [ ] **Day 1 · 컨테이너 개념과 기본 명령** — 컨테이너 vs VM, `run`, `ps`, `logs`, `exec`, `stop/rm`, 이미지 `pull`
  확인: 컨테이너가 VM보다 가벼운 이유는? (커널 공유, namespace/cgroup)
- [ ] **Day 2 · Dockerfile 기초** — `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD` vs `ENTRYPOINT`, FastAPI 앱 첫 이미지 빌드
- [ ] **Day 3 · 레이어와 캐시** — 레이어 구조, 명령 순서로 캐시 적중시키기(의존성 먼저 COPY), `.dockerignore`
  확인: 코드 한 줄 수정에 매번 pip install이 도는 이유와 해결책?
- [ ] **Day 4 · 이미지 줄이기** — 멀티스테이지 빌드, `slim`/`alpine` 선택 기준, 이미지 크기 전/후 비교
- [ ] **Day 5 · 볼륨** — 볼륨 vs 바인드 마운트, DB 데이터 보존, 컨테이너 삭제 후 데이터 확인
- [ ] **Day 6 · 네트워크** — 포트 매핑 `-p`, 브리지 네트워크, 컨테이너 이름으로 통신
- [ ] **Day 7 · Docker Compose 기초** — `compose.yaml`로 FastAPI + Postgres 한 번에 `up`
- [ ] **Day 8 · Compose 심화** — `healthcheck`, `depends_on: condition`, `.env`, 프로필, 개발/운영 설정 분리
- [ ] **Day 9 · 보안과 배포** — non-root 사용자, 시크릿을 이미지에 넣지 않기, 이미지 스캔(`docker scout`/`trivy`), 레지스트리 push/pull
- [ ] **Day 10 · 최종 미니** — **RAG API(FastAPI + pgvector) 컨테이너화**: `docker compose up` 한 줄로 실행되는 README 작성

---

## 이 정도면 점검 끝

- [ ] 이미지/컨테이너/볼륨/네트워크를 그림으로 설명한다
- [ ] 빌드 캐시를 고려해 Dockerfile을 작성한다
- [ ] compose로 앱 + DB 환경을 재현한다
- [ ] 비밀번호·API 키를 이미지에 굽지 않는 방법을 안다

## 자주 나오는 면접 질문

- 이미지와 컨테이너의 차이?
- `CMD`와 `ENTRYPOINT` 차이?
- 컨테이너가 죽으면 데이터는? 어떻게 보존하나?
- 도커 이미지가 큰 이유와 줄이는 방법?
