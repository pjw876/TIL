---
start: 2026-10-15
perday: 1
---
# 03. SQL 로드맵 (11일)

- **목표**: 분석 쿼리를 막힘없이 쓰고, 인덱스/실행계획을 읽어 느린 쿼리를 개선
- **하루**: 90분 (주제 2개 × 45분)
- **환경**: PostgreSQL (Docker로 띄워도 좋음 → 06-Docker와 연결)
- **자료**: SQLBolt, 프로그래머스 SQL 고득점 Kit, PostgreSQL 공식 문서
- **TIL 카테고리**: `SQL/`

---

## Day별 계획

- [x] **Day 1** — SELECT 기본 + 집계
  - **SELECT 기본**: `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, `LIKE`, `IN`, `BETWEEN`
    확인: 실행 순서(FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)를 말할 수 있나?
  - **집계**: `COUNT/SUM/AVG/MIN/MAX`, `GROUP BY`, `HAVING`
    확인: `WHERE`와 `HAVING`의 차이는?
- [ ] **Day 2** — JOIN 기초 + JOIN 심화
  - **JOIN 기초**: `INNER`, `LEFT JOIN`
    확인: `LEFT JOIN` 후 `WHERE`에 오른쪽 테이블 조건을 걸면 왜 INNER처럼 동작하나?
  - **JOIN 심화**: `SELF JOIN`, `CROSS JOIN`, `FULL OUTER`, 다대다 관계와 중복 행 폭증
- [ ] **Day 3** — 서브쿼리 + NULL, CASE, 함수
  - **서브쿼리**: 스칼라/인라인뷰, `IN` vs `EXISTS`
  - **NULL, CASE, 함수**: `COALESCE`, `NULLIF`, `CASE WHEN`, 문자열/날짜 함수
    확인: `NULL = NULL`이 왜 참이 아닌가?
- [ ] **Day 4** — 복습 + 윈도우 함수 1
  - **복습**: 프로그래머스 SQL Lv.2~3 5문제
  - **윈도우 함수 1**: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PARTITION BY`
- [ ] **Day 5** — 윈도우 함수 2 + CTE
  - **윈도우 함수 2**: `LAG/LEAD`, 누적합 `SUM() OVER (ORDER BY ...)`, 이동평균
  - **CTE**: `WITH`로 쿼리 가독성 개선, 서브쿼리를 CTE로 리팩터링
- [ ] **Day 6** — 재귀 CTE + 집합 연산
  - **재귀 CTE**: 조직도/카테고리 트리 조회
  - **집합 연산**: `UNION [ALL]`, `INTERSECT`, `EXCEPT`
- [ ] **Day 7** — 조건부 집계/피벗 + 복습 + 미니
  - **조건부 집계/피벗**: `SUM(CASE WHEN ...)`, `FILTER`
  - **복습 + 미니**: 주문 데이터로 **월별 코호트 리텐션 쿼리** 작성
- [ ] **Day 8** — DDL과 제약조건 + 트랜잭션
  - **DDL과 제약조건**: `PK/FK/UNIQUE/CHECK`, 정규화 1~3NF
    확인: 정규화를 깨고 일부러 중복 저장(반정규화)하는 경우는?
  - **트랜잭션**: ACID, 격리 수준(Read Committed / Repeatable Read), 데드락 직접 재현
- [ ] **Day 9** — 인덱스 + 실행 계획
  - **인덱스**: B-Tree 원리, 복합 인덱스 컬럼 순서, 커버링 인덱스
    확인: `(a, b)` 인덱스가 `WHERE b = ?`에 안 타는 이유는?
  - **실행 계획**: `EXPLAIN ANALYZE` 읽기, Seq Scan vs Index Scan, 행 수 추정 오차
- [ ] **Day 10** — 튜닝 안티패턴 + pgvector 맛보기
  - **튜닝 안티패턴**: `SELECT *`, 컬럼에 함수 적용 시 인덱스 무효, N+1, 불필요한 `DISTINCT`
  - **pgvector 맛보기**: 벡터 컬럼, `<=>` 코사인 거리, HNSW/IVFFlat 인덱스
    연결: RAG 벡터DB가 결국 인덱스 문제라는 점을 정리
- [ ] **Day 11** — 최종 미니
  - **최종 미니**: 가상 쇼핑몰 데이터 10만 행 생성 → 분석 쿼리 10개 → **인덱스 추가 전/후 `EXPLAIN` 비교**를 TIL로

---

## 이 정도면 점검 끝

- [ ] 윈도우 함수와 CTE로 "카테고리별 Top N", "전월 대비 증감" 쿼리를 바로 짠다
- [ ] `EXPLAIN ANALYZE`를 보고 병목을 한 문장으로 설명한다
- [ ] 복합 인덱스 설계 이유를 말로 설명한다
- [ ] 트랜잭션 격리 수준 차이를 예시로 설명한다

## 자주 나오는 면접 질문

- INNER JOIN과 LEFT JOIN의 차이? 결과 행 수가 늘어나는 경우는?
- 인덱스를 걸었는데 안 타는 이유 3가지?
- 정규화/반정규화 트레이드오프?
- 트랜잭션 격리 수준별로 생기는 이상 현상(Dirty/Non-repeatable/Phantom)?
