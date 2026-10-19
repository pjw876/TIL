"""two_sum 이 한 칸씩 어떻게 움직이는지 화면에 찍어 보기

사용법: 실행하기 전에 손으로 먼저 예측해 보고, 결과와 비교해 보자.
    python3 trace.py
"""


def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        need = target - x
        print(f"[{i}번째] 카드={x}, 필요한 짝={need}, 메모장={seen}")
        if need in seen:
            print(f"   → 메모장에 {need} 있음! 답: [{seen[need]}, {i}]")
            return [seen[need], i]
        seen[x] = i
        print(f"   → 없음. 메모장에 {x}: {i} 적음")


print("=== [3, 2, 4], target=6 ===")
two_sum([3, 2, 4], 6)

print()
print("=== [2, 7, 11, 15], target=9 ===")
two_sum([2, 7, 11, 15], 9)

print()
print("=== [3, 3], target=6 (같은 값 두 개) ===")
two_sum([3, 3], 6)
