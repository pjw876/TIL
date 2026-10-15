"""list vs set vs dict 연산 속도 비교 (시간복잡도 표 작성용)"""
import timeit

n = 100_000
number = 1000


def t(label, stmt, setup):
    sec = timeit.timeit(stmt, setup=setup, number=number)
    print(f"{label:22} {sec:.5f}s")


setup = f"lst = list(range({n})); st = set(lst); d = dict.fromkeys(lst)"

print(f"--- n={n}, {number}회 반복 ---")
t("list in (끝값)", f"{n - 1} in lst", setup)
t("set  in", f"{n - 1} in st", setup)
t("dict get", f"d.get({n - 1})", setup)
t("list append", "lst.append(1)", setup)
t("list pop()", "lst.append(1); lst.pop()", setup)
t("list insert(0)", "lst.insert(0, 1)", setup)
t("list pop(0)", "lst.insert(0, 1); lst.pop(0)", setup)
t("list index [i]", f"lst[{n // 2}]", setup)

# 정리 (평균 시간복잡도)
# | 연산            | list | set  | dict |
# |-----------------|------|------|------|
# | 인덱싱 [i]      | O(1) | -    | -    |
# | in / 검색       | O(n) | O(1) | O(1) |
# | append / add    | O(1) | O(1) | O(1) |
# | pop() (끝)      | O(1) | -    | -    |
# | pop(0)/insert(0)| O(n) | -    | -    |
# | get / 삭제      | O(n) | O(1) | O(1) |
# 이유: list 는 연속 배열이라 앞을 건드리면 뒤를 전부 밀어야 한다.
#       set/dict 는 해시 테이블이라 값을 해시로 바로 찾는다.

# 실행 결과 (n=100,000, 1000회 반복, 환경에 따라 숫자는 달라짐)
# list in (끝값)           0.52277s   ← O(n), 처음부터 끝까지 훑음
# set  in                0.00002s   ← O(1), 약 2만 배 빠름
# dict get               0.00003s   ← O(1)
# list append            0.00001s   ← O(1)
# list pop()             0.00002s   ← O(1)
# list insert(0)         0.02389s   ← O(n), 뒤 요소를 전부 한 칸씩 밀기
# list pop(0)            0.03160s   ← O(n), 뒤 요소를 전부 한 칸씩 당기기
# list index [i]         0.00001s   ← O(1)
# 결론: 자주 "있는지 확인"하면 set/dict, 앞에서 넣고 빼면 collections.deque 를 쓴다.
