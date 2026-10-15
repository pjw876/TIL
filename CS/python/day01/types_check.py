"""자료형별 mutable / immutable 점검

각 자료형에 대해 "제자리 수정"을 시도하고, 객체 id가 유지되는지 / 에러가 나는지 확인한다.
"""


def check(name, obj, modify):
    before = id(obj)
    try:
        modify(obj)
    except Exception as e:
        print(f"{name:10} 수정 불가 → {type(e).__name__}: {e}")
        return
    print(f"{name:10} 수정 가능 (id 유지: {id(obj) == before})")


# --- mutable ---
check("list", [1, 2], lambda x: x.append(3))
check("dict", {"a": 1}, lambda x: x.update(b=2))
check("set", {1, 2}, lambda x: x.add(3))
check("bytearray", bytearray(b"ab"), lambda x: x.append(99))

# --- immutable ---
def set_item(x):
    x[0] = 9

check("tuple", (1, 2), set_item)
check("str", "hi", set_item)
check("bytes", b"ab", set_item)
check("frozenset", frozenset({1}), lambda x: x.add(2))

# int, float, str 은 "+=" 하면 새 객체가 됨
n = 10
before = id(n)
n += 1
print(f"{'int':10} += 후 id 유지: {id(n) == before}")

s = "hi"
before = id(s)
s += "!"
print(f"{'str':10} += 후 id 유지: {id(s) == before}")

lst = [1]
before = id(lst)
lst += [2]
print(f"{'list':10} += 후 id 유지: {id(lst) == before}")

# 1. tuple 안의 list 는 수정 가능하다
t = ([1, 2], 3)
t[0].append(99)
print(t)   # ([1, 2, 99], 3) — 에러 없음
# 이유: tuple 이 고정하는 것은 "각 칸이 가리키는 대상"이다.
#       칸이 가리키는 list 객체 자체는 mutable 이라 내용을 고칠 수 있다.

# 2. t[0] = [0] 이 에러인 이유
try:
    t[0] = [0]
except TypeError as e:
    print("TypeError:", e)
# 이유: 칸(화살표)을 다른 객체로 바꿔 끼우는 것이라서, tuple 은 이를 허용하지 않는다.

# 3. dict 의 key 로 list 를 쓰면
d = {}
d[(1, 2)] = "ok"     # tuple 은 가능
try:
    d[[1, 2]] = "no"
except TypeError as e:
    print("TypeError:", e)   # unhashable type: 'list'
# 이유: dict 의 key 는 hash 값이 변하지 않아야 찾을 수 있다.
#       list 는 내용이 바뀔 수 있어서 hash 를 만들 수 없다(unhashable).
#       그래서 key 로는 str, int, tuple 같은 immutable 만 쓸 수 있다.

# 실행 결과
# list       수정 가능 (id 유지: True)
# dict       수정 가능 (id 유지: True)
# set        수정 가능 (id 유지: True)
# bytearray  수정 가능 (id 유지: True)
# tuple      수정 불가 → TypeError: 'tuple' object does not support item assignment
# str        수정 불가 → TypeError: 'str' object does not support item assignment
# bytes      수정 불가 → TypeError: 'bytes' object does not support item assignment
# frozenset  수정 불가 → AttributeError: 'frozenset' object has no attribute 'add'
# int        += 후 id 유지: False   (새 객체)
# str        += 후 id 유지: False   (새 객체)
# list       += 후 id 유지: True    (제자리 수정)
# ([1, 2, 99], 3)
# TypeError: 'tuple' object does not support item assignment
# TypeError: unhashable type: 'list'
