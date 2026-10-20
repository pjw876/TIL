"""폰켓몬 (프로그래머스 Lv.1 · 해시)

nums = 폰켓몬 종류 번호 list. 전체 마리 수의 절반만 가져갈 수 있다.
가져갈 때 종류가 최대 몇 가지가 될까?

단계 (한 단계씩 채우고 python3 pokemon.py 로 확인)
  1. 종류 모으기            → set(...)
  2. 종류가 몇 가지인지      → len(...)
  3. 가져갈 수 있는 마리 수  → 전체 마리 수 // 2
  4. 둘 중 작은 쪽이 답      → min(...)
"""


def solution(nums):
    kinds = set(nums)   # TODO 1단계: nums 의 중복을 없앤 set
    n_kinds = len(kinds)  # TODO 2단계: 종류 수 (kinds 의 개수)
    can_take = len(nums) // 2  # TODO 3단계: 가져갈 수 있는 마리 수
    answer = min(n_kinds, can_take)  # TODO 4단계: n_kinds 와 can_take 중 작은 쪽

    # 단계별로 값이 맞는지 보는 용도 (다 풀면 지워도 됨)
    print(f"  종류={kinds}, 종류 수={n_kinds}, 가져갈 수={can_take}, 답={answer}")
    return answer


cases = [
    ([3, 1, 2, 3], 2),
    ([3, 3, 3, 2, 2, 4], 3),
    ([3, 3, 3, 2, 2, 2], 2),
]

for nums, expected in cases:
    print(f"nums={nums}")
    got = solution(nums)
    print(("✅" if got == expected else "❌"), f"내 답={got}, 정답={expected}\n")
