"""Day 2 해시 개념 직접 치면서 공부하기

사용법
1. 각 함수의 `pass  # TODO` 를 지우고 직접 코드를 쓴다 (힌트는 독스트링 참고)
2. python3 concept_practice.py 실행 → ✅ / ❌ 로 확인
   - 검사는 입력을 여러 개 넣어서 하기 때문에 정답 값을 그대로 써서는 통과할 수 없다
3. 막히면 개념 설명 다시 보기, 그래도 모르면 물어보기
"""
from collections import Counter
import time


def run(name, fn, cases):
    """cases: [(args 튜플, 기대값), ...]  모두 맞아야 ✅"""
    for args, expected in cases:
        try:
            got = fn(*args)
        except Exception as e:  # 아직 안 채웠거나 버그
            print(f"❌ {name}: 입력 {args} 에서 에러 → {type(e).__name__}: {e}")
            return
        if got != expected:
            print(f"❌ {name}: 입력 {args} → 내 답={got!r}, 기대={expected!r}")
            return
    print(f"✅ {name}")


# ─────────────────────────────────────────────
# 1. set : 중복 제거, 있는지 확인
# ─────────────────────────────────────────────
def unique(nums):
    """nums 의 중복을 없앤 set 을 반환.  힌트: set(...)"""
    return set(nums)


def has(nums, x):
    """nums 에 x 가 있는지 True/False.  set 으로 바꿔서 in 으로 확인해 보기"""
    return x in nums# TODO


def kinds(nums):
    """nums 에 서로 다른 값이 몇 종류인지.  힌트: len + set"""
    return len(set(nums))# TODO


run("1-1 unique", unique, [(([1, 2, 3, 2, 1],), {1, 2, 3}), (([5, 5],), {5}), (([],), set())])
run("1-2 has", has, [(([1, 2, 3], 3), True), (([1, 2, 3], 9), False), (([], 1), False)])
run("1-3 kinds", kinds, [(([1, 1, 2, 3],), 3), (([7, 7, 7],), 1), (([],), 0)])


# ─────────────────────────────────────────────
# 2. dict : 키 → 값
# ─────────────────────────────────────────────
def to_dict(names, scores):
    """names[i] → scores[i] 로 짝지은 dict.  힌트: dict(zip(a, b)) 또는 for + d[키] = 값"""
    return dict(zip(names, scores))# TODO


def score_of(d, name):
    """d 에 name 이 없으면 에러 대신 0 을 반환.  힌트: d.get(키, 기본값)"""
    return d.get(name, 0)  # TODO


def set_score(d, name, score):
    """d[name] 을 score 로 추가/수정한 뒤 d 를 반환.  힌트: d[키] = 값"""
    d[name] = score
    return d  # TODO


run("2-1 to_dict", to_dict, [((["a", "b"], [1, 2]), {"a": 1, "b": 2}), (([], []), {})])
run("2-2 score_of", score_of, [(({"a": 1}, "a"), 1), (({"a": 1}, "z"), 0), (({}, "q"), 0)])
run("2-3 set_score", set_score, [(({"a": 1}, "b", 5), {"a": 1, "b": 5}), (({"a": 1}, "a", 9), {"a": 9})])


def pair_up(a, b):
    """a, b 를 같은 위치끼리 묶은 (a값, b값) tuple 의 list 를 반환.  힌트: list(zip(a, b))
    zip 은 list 가 아니라 한 번 쓰면 사라지는 '이터레이터'를 돌려준다 → list(...) 로 감싸야 보인다"""
    return list(zip(a,b))  # TODO


def total_of_pairs(a, b):
    """a[i] * b[i] 를 전부 더한 값 (내적).  힌트: for x, y in zip(a, b) 또는 sum(x * y for ...)"""
    return sum(x * y for x, y in zip(a, b))  # TODO


run("2-4 pair_up", pair_up, [(([1, 2], ["a", "b"]), [(1, "a"), (2, "b")]), (([1, 2, 3], ["a"]), [(1, "a")]), (([], []), [])])
run("2-5 total_of_pairs", total_of_pairs, [(([1, 2, 3], [4, 5, 6]), 32), (([2], [5]), 10), (([], []), 0)])


# ─────────────────────────────────────────────
# 3. Counter : 몇 번 나왔나
# ─────────────────────────────────────────────
def count_chars(s):
    """글자별 개수 Counter 를 반환.  힌트: Counter(...)"""
    return Counter(s)  # TODO


def count_of(s, ch):
    """s 에서 ch 가 몇 번 나오는지 (없으면 0).  Counter 는 없는 키도 0 이 나온다"""
    return Counter(s)[ch]  # TODO


def top_char(s):
    """가장 많이 나온 글자 1개.  힌트: .most_common(1)[0][0]  (동점이면 먼저 나온 것)"""
    return Counter(s).most_common(1)[0][0]  # TODO


def left_over(participant, completion):
    """participant 중 completion 에 없는 사람 1명의 이름을 반환 (동명이인 가능).
    힌트: Counter 끼리 빼기 → 남은 키 꺼내기  ('완주하지 못한 선수' 핵심 아이디어)"""
    return list(Counter(participant) - Counter(completion))[0]  # TODO


run("3-1 count_chars", lambda s: dict(count_chars(s)), [(("hello",), {"h": 1, "e": 1, "l": 2, "o": 1}), (("",), {})])
run("3-2 count_of", count_of, [(("hello", "l"), 2), (("hello", "z"), 0), (("aaa", "a"), 3)])
run("3-3 top_char", top_char, [(("hello",), "l"), (("aabbb",), "b")])
run("3-4 left_over", left_over, [
    ((["a", "b", "b"], ["b", "a"]), "b"),
    ((["x", "y"], ["y"]), "x"),
    ((["m", "m", "n"], ["n", "m"]), "m"),
])


# ─────────────────────────────────────────────
# 4. 키로 쓸 수 있는 것: tuple 은 가능, list 는 불가
# ─────────────────────────────────────────────
def index_by_point(points):
    """points = [(x, y, 이름), ...] → {(x, y): 이름} 으로.  좌표(tuple)를 키로 쓴다"""
    #d = {}
    #for x, y, name in points:
    #    d[(x, y)] = name
    #return d  # TODO
    return {(x, y):name for x, y, name in points}


run("4-1 index_by_point", index_by_point, [
    (([(1, 2, "A"), (3, 4, "B")],), {(1, 2): "A", (3, 4): "B"}),
    (([],), {}),
])


# ─────────────────────────────────────────────
# 5. 미니 문제: 두 수의 합 — 해시로 O(n)
# ─────────────────────────────────────────────
def two_sum(arr, target):
    """arr 에서 합이 target 인 두 수의 '인덱스'를 [i, j] (i < j) 로 반환. 답은 항상 1개.
    힌트: seen = {} 에 {값: 인덱스} 를 저장하며 한 번만 순회.
          현재 값 x 에 대해 (target - x) 가 seen 에 있으면 정답."""
    seen = {}
    for i, x in enumerate(arr):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return None    # TODO


run("5 two_sum", two_sum, [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([1, 5, 9, 14], 23), [2, 3]),
])


# ─────────────────────────────────────────────
# 6. 속도 직접 재 보기 (list vs set)
# ─────────────────────────────────────────────
N = 100_000
lst = list(range(N))
st = None  # TODO  lst 를 set 으로 바꿔 보자 (set(lst))

if st is not None:
    start = time.perf_counter()
    for _ in range(1000):
        (N - 1) in lst
    t_list = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(1000):
        (N - 1) in st
    t_set = time.perf_counter() - start

    print(f"list: {t_list:.5f}s / set: {t_set:.5f}s → {t_list / t_set:.0f}배 차이")
    # 질문: 왜 이렇게 차이가 날까? 한 줄로 TIL 에 적어 보기
