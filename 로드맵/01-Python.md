---
start: 2026-10-15
perday: 1
---
# 01. Python 로드맵 (14일)

- **목표**: 문법을 아는 수준에서 "실무 코드를 짜고 테스트하고 비동기로 돌리는" 수준까지
- **하루**: 2시간 (주제 2개 × 학습·실습 50분 + TIL 10분)
- **자료**: 공식 문서(docs.python.org/ko/3), 점프 투 파이썬(복습용), Fluent Python(발췌), FastAPI 공식 튜토리얼
- **TIL 카테고리**: `CS/`

---

## Day별 계획

- [ ] **Day 1** — 언어 핵심 ①
  - 자료형과 mutable/immutable: `id()`로 객체 동일성 확인, list/tuple/dict/set 연산 시간복잡도 표 만들기
    확인: 함수 기본 인자에 `[]`를 쓰면 왜 위험한가?
  - 제어흐름과 컴프리헨션: list/dict/set 컴프리헨션, 제너레이터 표현식 비교
    확인: `[x for ...]`와 `(x for ...)`의 메모리 차이를 `sys.getsizeof`로 보여 줄 수 있나?
- [ ] **Day 2** — 언어 핵심 ②
  - 함수: `*args`, `**kwargs`, 키워드 전용 인자, 일급 객체, 클로저
    확인: 클로저가 변수를 "캡처"한다는 말은 무슨 뜻인가?
  - 이터레이터와 제너레이터: `__iter__`/`__next__`, `yield`, 대용량 파일을 한 줄씩 스트리밍
    확인: 제너레이터가 리스트보다 유리한 상황과 불리한 상황은?
- [ ] **Day 3** — 언어 핵심 ③
  - 데코레이터: 실행시간 측정, 재시도(retry) 데코레이터 작성, `functools.wraps`
    확인: `@wraps`를 빼면 어떤 문제가 생기나?
  - 예외 처리: `try/except/else/finally`, 커스텀 예외, `raise ... from`
    확인: 너무 넓은 `except Exception`이 왜 문제인가?
- [ ] **Day 4** — 복습 + 객체지향 시작
  - 복습 + 미니: 로그 파일을 읽어 에러 줄만 집계하는 스크립트 (제너레이터 사용)
  - 클래스 기본: 인스턴스/클래스 변수, `__repr__`, `__eq__`, `__hash__`
    확인: 클래스 변수에 리스트를 두면 생기는 문제는?
- [ ] **Day 5** — 객체지향
  - 상속, MRO, ABC: `super()`, 다중상속 MRO 출력, `abc.ABC`로 인터페이스 정의
    확인: 상속 대신 합성(composition)을 쓰는 이유는?
  - dataclass와 Enum: `@dataclass(frozen=True, slots=True)`, `Enum` 사용
- [ ] **Day 6** — 타입 · 검증
  - 타입 힌트: `Optional`, `Union`, `Generic`, `Protocol`, mypy 또는 pyright 돌려 보기
    확인: 타입 힌트는 런타임에 강제되나?
  - pydantic: `BaseModel` 검증, 설정 관리(`BaseSettings`)
    연결: LLM 구조화 출력(JSON schema)이 pydantic 모델과 어떻게 이어지는지 정리
- [ ] **Day 7** — 컨텍스트 매니저 + 미니
  - 컨텍스트 매니저: `with`, `__enter__/__exit__`, `contextlib.contextmanager`
  - 복습 + 미니: pydantic 설정 로더 + 컨텍스트 매니저로 만든 타이머
- [ ] **Day 8** — 실무 도구 ①
  - 모듈과 패키지: import 동작 방식, `__init__.py`, 순환 import 해결, `pyproject.toml`
  - 가상환경과 의존성: `venv`, `uv` 또는 `poetry`, 버전 고정
    확인: `requirements.txt`와 lock 파일의 차이는?
- [ ] **Day 9** — 실무 도구 ②
  - 파일 I/O: `pathlib`, JSON, CSV, 인코딩(utf-8) 문제
  - 로깅: `logging` 레벨, 포매터, 핸들러, JSON 구조화 로그
    확인: `print` 대신 로깅을 쓰는 이유 3가지
- [ ] **Day 10** — pytest
  - pytest 기초: `assert`, fixture, `parametrize`
  - pytest 심화: `monkeypatch`/`mock`, 외부 API 모킹, 커버리지 측정
- [ ] **Day 11** — 복습 + 동시성 시작
  - 복습 + 미니: `typer` 또는 `argparse` CLI + 테스트 5개
  - GIL, 스레드, 프로세스: I/O 바운드와 CPU 바운드를 각각 `threading`/`multiprocessing`으로 실험
    확인: GIL이 있는데 스레드가 왜 I/O 작업엔 도움이 되나?
- [ ] **Day 12** — asyncio
  - asyncio 기초: `async/await`, 이벤트 루프, `asyncio.gather`
  - asyncio 실전: `httpx.AsyncClient`로 URL 20개 동시 호출, `Semaphore`로 동시성 제한, timeout
- [ ] **Day 13** — asyncio 심화 + 성능
  - asyncio 심화: Task 취소, 예외 전파, `TaskGroup`, 비동기 제너레이터
    확인: `await`를 빼먹으면 어떻게 되는가?
  - 성능 측정: `timeit`, `cProfile`, `tracemalloc`로 병목 찾기
- [ ] **Day 14** — FastAPI + 최종 미니 프로젝트
  - FastAPI 맛보기: 라우팅, pydantic 요청/응답 모델, 비동기 엔드포인트, `/docs` 확인
  - 최종 미니 프로젝트: **LLM API 비동기 배치 호출기**
    요구: 동시성 제한 + 재시도(데코레이터) + 구조화 로그 + pytest 테스트 + 타입 힌트

---

## 이 정도면 점검 끝

- [ ] 제너레이터, 데코레이터, 컨텍스트 매니저를 직접 짜서 설명할 수 있다
- [ ] 타입 힌트 + pydantic으로 입력 검증을 구성할 수 있다
- [ ] pytest로 외부 호출을 모킹한 테스트를 쓸 수 있다
- [ ] asyncio로 동시 요청 + 동시성 제한 + 타임아웃을 구현할 수 있다
- [ ] `async`가 왜 빠른지 (이벤트 루프, I/O 대기) 말로 설명할 수 있다

## 자주 나오는 면접 질문

- GIL이란? 멀티스레딩이 의미 있는 경우는?
- 데코레이터와 클로저의 관계는?
- 제너레이터와 이터레이터의 차이?
- `async`와 스레드의 차이? 언제 무엇을 쓰나?
- mutable 기본 인자 버그를 설명해 보세요.
