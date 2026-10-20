"""Day 2 스택 개념 직접 치면서 공부하기

사용법
1. 각 함수의 `pass  # TODO` 를 지우고 직접 코드를 쓴다 (힌트는 독스트링 참고)
2. python3 stack_practice.py 실행 → ✅ / ❌ 로 확인
   - 검사는 입력을 여러 개 넣어서 하기 때문에 정답 값을 그대로 써서는 통과할 수 없다
3. 막히면 개념 설명 다시 보기, 그래도 모르면 물어보기

스택 도구 (파이썬 list)
  stack.append(x)   넣기      O(1)   반환 None
  stack.pop()       꺼내기    O(1)   꺼낸 값 반환 (빈 스택이면 IndexError)
  stack[-1]         맨 위 보기 O(1)  지우지 않음 (빈 스택이면 IndexError)
  not stack         비었나?   True / False
"""


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
# 1. 기본 동작: 넣기 / 꺼내기 / 맨 위 보기
# ─────────────────────────────────────────────
def push_all(items):
    """[문제] 빈 스택에 items 의 값을 앞에서부터 하나씩 차례로 넣어라.
    [입력] items: list
    [반환] 다 넣은 뒤의 스택(list)
    [예]   push_all([1, 2, 3]) → [1, 2, 3]   (3 이 맨 위)
           push_all([])        → []
    [힌트] stack = [] 을 만들고, for 로 돌며 stack.append(x)"""
    # stack = []
    # for item in items:
    #     stack.append(item)  # TODO
    stack = [item for item in items ]
    return stack


def top_of(stack):
    """[문제] 스택의 맨 위 값이 뭔지 알려 줘라. 값은 지우지 말고 보기만 한다.
    [입력] stack: list (맨 끝이 맨 위)
    [반환] 맨 위 값. 스택이 비어 있으면 None
    [예]   top_of([1, 2, 3]) → 3
           top_of([])        → None
    [힌트] 빈 스택에 stack[-1] 을 하면 IndexError → 먼저 비었는지 확인"""
    return stack[-1] if stack else None   # TODO


def pop_two(stack):
    """[문제] 스택에서 값을 2번 꺼내서, 꺼낸 순서대로 (첫 번째, 두 번째) 로 돌려줘라.
    [입력] stack: list (원소가 2개 이상. 맨 끝이 맨 위)
    [반환] (먼저 꺼낸 값, 그다음 꺼낸 값) tuple
    [예]   pop_two([1, 2, 3]) → (3, 2)   (3 이 맨 위라서 먼저 나옴)
           pop_two([5, 9])    → (9, 5)
    [힌트] stack.pop() 을 두 번. 나중에 넣은 게 먼저 나온다"""
    return stack.pop(), stack.pop()  # TODO


run("1-1 push_all", push_all, [(([1, 2, 3],), [1, 2, 3]), (([],), [])])
run("1-2 top_of", top_of, [(([1, 2, 3],), 3), (([],), None), (([7],), 7)])
run("1-3 pop_two", pop_two, [(([1, 2, 3],), (3, 2)), (([5, 9],), (9, 5))])


# ─────────────────────────────────────────────
# 2. 스택으로 뒤집기 (나중에 넣은 게 먼저 나온다)
# ─────────────────────────────────────────────
def reverse_str(s):
    """[문제] 문자열 s 의 글자 순서를 거꾸로 뒤집어라. 스택을 써서 풀 것 (s[::-1] 금지).
    [입력] s: 문자열 (빈 문자열 가능)
    [반환] 뒤집힌 문자열
    [예]   reverse_str("abc") → "cba"
           reverse_str("")    → ""
    [힌트] 글자를 전부 stack 에 넣은 뒤, 스택이 빌 때까지 pop() 한 글자를 이어 붙이기
           (나중에 넣은 글자가 먼저 나오니까 자연스럽게 뒤집힌다)"""
    chars = list(s)
    stack = [chars.pop() for _ in range(len(chars))]  # TODO
    return "".join(stack)


run("2 reverse_str", reverse_str, [(("abc",), "cba"), (("",), ""), (("a",), "a"), (("hello",), "olleh")])


# ─────────────────────────────────────────────
# 3. 같은 숫자는 싫어 (프로그래머스 Lv.1 의 핵심)
# ─────────────────────────────────────────────
def remove_consecutive(arr):
    """[문제] arr 에서 '바로 옆에 같은 숫자가 연속으로' 나오면 하나만 남기고 지워라.
             원래 순서는 그대로 유지한다. (떨어져 있는 같은 숫자는 지우지 않는다)
    [입력] arr: 숫자 list (빈 list 가능)
    [반환] 연속 중복을 제거한 list
    [예]   [1, 1, 3, 3, 0, 1, 1] → [1, 3, 0, 1]
           (1,1 → 1 / 3,3 → 3 / 0 / 1,1 → 1.  앞의 1 과 뒤의 1 은 떨어져 있어서 둘 다 남는다)
           [4, 4, 4, 3, 3]       → [4, 3]
           [1, 2, 1, 2]          → [1, 2, 1, 2]   (연속 중복 없음)
    [힌트] 결과를 담을 answer(스택)를 만들고 arr 를 앞에서부터 본다.
           answer 가 비었거나, answer 의 맨 위가 지금 숫자와 '다르면' append"""
    stack = []
    # for nums in arr:
    #     if stack and nums == stack[-1]:
    #         stack.pop()
    #     stack.append(nums)
    for num in arr:
        if not stack or stack[-1] != num:
            stack.append(num)
    return stack  # TODO


run("3 remove_consecutive", remove_consecutive, [
    (([1, 1, 3, 3, 0, 1, 1],), [1, 3, 0, 1]),
    (([4, 4, 4, 3, 3],), [4, 3]),
    (([5],), [5]),
    (([],), []),
    (([1, 2, 1, 2],), [1, 2, 1, 2]),
])


# ─────────────────────────────────────────────
# 4. 올바른 괄호 (프로그래머스 Lv.2 의 핵심)
# ─────────────────────────────────────────────
def is_valid(s):
    """[문제] 괄호 문자열 s 가 '올바른 괄호'인지 판단해라.
             올바른 괄호 = 모든 '(' 가 뒤에 오는 ')' 와 하나씩 짝이 맞고, 짝이 안 남는 것.
             '(' 가 먼저 열려야 ')' 로 닫을 수 있다.
    [입력] s: '(' 와 ')' 로만 이루어진 문자열 (빈 문자열 가능, 빈 문자열은 올바른 것으로 본다)
    [반환] 올바르면 True, 아니면 False
    [예]   "()()"   → True
           "(())()" → True
           ")()("   → False   (처음부터 ')' 가 먼저 나옴)
           "(()("   → False   (끝에 짝 없는 '(' 가 남음)
           ""       → True
    [힌트] '(' 면 스택에 쌓고, ')' 면 맨 위 '(' 하나를 꺼내서 짝을 맞춘다.
      - ')' 가 왔는데 스택이 비었다 → 짝 없는 ')' → False
      - 다 끝났는데 스택에 남았다   → 짝 없는 '(' → False
      - 다 끝났고 스택이 비었다     → True"""
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else :
            if not stack:
                return False
            stack.pop()
    
    return not stack


run("4 is_valid", is_valid, [
    (("()()",), True),
    (("(())()",), True),
    ((")()(",), False),
    (("(()(",), False),
    (("(",), False),
    ((")",), False),
    (("",), True),
])
