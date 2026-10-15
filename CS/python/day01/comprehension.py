"""Day 2 · 제어흐름과 컴프리헨션"""
import sys

N = 10**6
lst = [x for x in range(N)]
gen = (x for x in range(N))
print("list:", sys.getsizeof(lst), "bytes")
print("gen :", sys.getsizeof(gen), "bytes")
# list 는 값을 전부 만들어 저장, gen 은 "만드는 방법"만 갖고 하나씩 계산한다.
# 참고: getsizeof 는 요소 객체 자체의 크기는 포함하지 않는다.

# --- list / dict / set 컴프리헨션 ---
nums = [1, 2, 3, 4, 5, 6]
squares = [n * n for n in nums]                      # [1, 4, 9, 16, 25, 36]
even_squares = [n * n for n in nums if n % 2 == 0]   # 조건절: [4, 16, 36]
labels = ["짝" if n % 2 == 0 else "홀" for n in nums]  # 조건식은 for 앞에
sq_dict = {n: n * n for n in nums}                   # {1: 1, 2: 4, ...}
mod_set = {n % 3 for n in nums}                      # {0, 1, 2} — 중복 제거
print(squares, even_squares, labels, sq_dict, mod_set, sep="\n")

# 중첩 컴프리헨션
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [v for row in matrix for v in row]            # [1, 2, 3, 4, 5, 6]
board = [[0] * 3 for _ in range(3)]                  # 3x3, 줄마다 별개 리스트
board[0][0] = 1
print(flat, board)                                   # board 의 한 줄만 바뀜

# for 루프 버전과 같은 결과
result = []
for n in nums:
    if n % 2 == 0:
        result.append(n * n)
assert result == even_squares

# --- 제너레이터는 한 번 소비하면 끝 ---
g = (x for x in range(5))
print(sum(g))   # 10
print(sum(g))   # 0 — 이미 다 소비해서 비어 있음
# 여러 번 쓰려면 list 로 만들거나 매번 새 제너레이터를 만든다.

# 실행 결과
# list: 8448728 bytes    ← 100만 개 값을 전부 저장
# gen : 192 bytes        ← 만드는 방법만 저장 (약 4만 배 작음)
# [1, 4, 9, 16, 25, 36]
# [4, 16, 36]
# ['홀', '짝', '홀', '짝', '홀', '짝']
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# {0, 1, 2}
# [1, 2, 3, 4, 5, 6] [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# 10
# 0                      ← 제너레이터는 한 번 소비하면 비어 있음
