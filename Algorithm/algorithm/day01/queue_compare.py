"""list.pop(0) vs deque.popleft() 속도 비교 (N을 키우며 O(n) vs O(1) 확인)"""
import time
from collections import deque


def measure(n):
    lst = list(range(n))
    dq = deque(range(n))

    s = time.perf_counter()
    while lst:
        lst.pop(0)
    t_list = time.perf_counter() - s

    s = time.perf_counter()
    while dq:
        dq.popleft()
    t_deque = time.perf_counter() - s
    return t_list, t_deque


print(f"{'N':>9} {'list.pop(0)':>13} {'deque.popleft()':>16} {'배수':>8}")
for n in (10_000, 50_000, 100_000, 200_000):
    a, b = measure(n)
    print(f"{n:>9,} {a:>12.4f}s {b:>15.4f}s {a / b:>7.1f}x")

# 정리
# list.pop(0)      : 앞을 빼면 뒤 원소를 전부 한 칸씩 당김 → 1번에 O(n), N번 반복하면 O(n²)
# deque.popleft()  : 양끝이 열린 이중 연결 구조 → 1번에 O(1), N번 반복해도 O(n)
