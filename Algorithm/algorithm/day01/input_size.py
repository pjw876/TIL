"""입력 크기 N → 허용 복잡도: 연산 횟수 계산표 (파이썬 1초 ≈ 10^7~10^8 연산 기준)"""
import math

LIMIT = 10**8  # 1초 안에 가능한 연산 수(넉넉한 상한)

complexities = {
    "O(log N)": lambda n: math.log2(n),
    "O(N)": lambda n: n,
    "O(N log N)": lambda n: n * math.log2(n),
    "O(N^2)": lambda n: n**2,
    "O(N^3)": lambda n: n**3,
    "O(2^N)": lambda n: 2**n if n <= 60 else float("inf"),
}

for n in (20, 500, 3_000, 100_000, 1_000_000):
    print(f"\nN = {n:,}")
    for name, f in complexities.items():
        ops = f(n)
        mark = "OK " if ops <= LIMIT else "X  "
        print(f"  {mark}{name:11} {ops:>14,.0f}")
