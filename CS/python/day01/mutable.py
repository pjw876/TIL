"""Day 1 · 자료형과 mutable/immutable"""

# 1. 객체 동일성: id(), is, ==
a = [1, 2]
b = a
c = a.copy()
print(id(a) == id(b), a is c, a == c)

# 2. 기본 인자 함정
def add_bad(x, lst=[]):
    lst.append(x)
    return lst

def add_good(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst

print(add_bad(1), add_bad(2))    # [1, 2] [1, 2]
# 이유: 기본값 [] 는 함수를 "정의할 때" 한 번만 만들어진다.
#       호출할 때마다 같은 리스트를 공유하고, list 는 mutable 이라 append 가 쌓인다.
#       (두 결과가 둘 다 [1, 2] 인 것도 같은 리스트 하나를 가리키기 때문)
print(add_good(1), add_good(2))  # [1] [2] — 호출마다 새 리스트

# 실행 결과
# True False True     ← id(a)==id(b), a is c, a == c
# [1, 2] [1, 2]       ← add_bad: 기본값 리스트를 공유
# [1] [2]             ← add_good: 호출마다 새 리스트
