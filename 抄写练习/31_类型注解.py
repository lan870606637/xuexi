# ============================================
# 题目31：类型注解（Type Hints）
# 知识点：变量注解 / 函数注解 / typing 模块 / 泛型
# ============================================

from typing import (
    List, Dict, Tuple, Set, Optional, Union,
    Callable, Any, TypeVar, Generic
)

# Python 3.10+ 可以用内置类型：list, dict, tuple, set
# 而不需要从 typing 导入大写版本

# --- 变量注解 ---
print("=== 变量注解 ===")
name: str = "张三"
age: int = 25
score: float = 92.5
is_student: bool = True
data: list = []

# 注解只是提示，运行时不强制检查
x: int = "这不是整数"    # Python 不会报错！
print(x)

# --- 函数注解 ---
print("\n=== 函数注解 ===")
def greet(name: str) -> str:
    return f"你好，{name}！"

def add(a: int, b: int) -> int:
    return a + b

def process(text: str, repeat: int = 1) -> list[str]:
    return [text] * repeat

print(greet("张三"))
print(add(3, 5))
print(process("hi", 3))

# 查看函数注解
print(f"\ngreet 的注解：{greet.__annotations__}")

# --- Optional（可能是 None）---
print("\n=== Optional ===")
def find_user(user_id: int) -> Optional[str]:   # 等价于 Union[str, None]
    users = {1: "张三", 2: "李四"}
    return users.get(user_id)                    # 可能返回 None

user = find_user(1)
print(user)         # 张三

user = find_user(99)
print(user)         # None

# 处理 Optional
if user is not None:
    print(user.upper())
else:
    print("用户不存在")

# Python 3.10+ 可以用 str | None 代替 Optional[str]
def get_name(uid: int) -> str | None:
    users = {1: "张三"}
    return users.get(uid)

# --- Union（多种类型）---
print("\n=== Union ===")
def parse(value: Union[int, str]) -> str:   # 接受 int 或 str
    if isinstance(value, int):
        return f"整数：{value}"
    return f"字符串：{value}"

print(parse(42))
print(parse("hello"))

# Python 3.10+ 写法
def parse2(value: int | str | float) -> str:
    return str(value)

# --- 集合类型注解 ---
print("\n=== 集合注解 ===")
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

def get_scores(students: dict[str, float]) -> dict[str, str]:
    return {name: "通过" if score >= 60 else "不通过"
            for name, score in students.items()}

def unpack_point(point: tuple[float, float]) -> tuple[float, float]:
    x, y = point
    return x, y

scores = {"张三": 85.0, "李四": 55.0}
print(get_scores(scores))

# --- Callable（可调用对象）---
print("\n=== Callable ===")
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

print(apply_twice(lambda x: x + 1, 5))  # 7
print(apply_twice(lambda x: x * 2, 3))  # 12

# --- TypeVar（泛型变量）---
print("\n=== TypeVar ===")
T = TypeVar("T")

def first(lst: list[T]) -> T:           # 输入和输出类型相同
    return lst[0]

print(first([1, 2, 3]))                 # int 类型
print(first(["a", "b", "c"]))           # str 类型

def identity(value: T) -> T:
    return value

# --- 实用案例：带注解的数据处理 ---
print("\n=== 实用案例 ===")
def parse_students(raw_data: list[dict[str, Any]]) -> list[dict[str, str | int | float]]:
    result = []
    for item in raw_data:
        result.append({
            "name": str(item["name"]),
            "age": int(item["age"]),
            "score": float(item["score"]),
        })
    return result

raw = [
    {"name": "张三", "age": "20", "score": "85.5"},
    {"name": "李四", "age": 22, "score": 92},
]
parsed = parse_students(raw)
for s in parsed:
    print(f"  {s['name']}, {s['age']}岁, {s['score']}分")

# --- 运行时类型检查（类型注解不会自动检查）---
print("\n=== 运行时检查 ===")
def strict_add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"期望 int，收到 {type(a).__name__} 和 {type(b).__name__}")
    return a + b

print(strict_add(1, 2))         # 3
try:
    strict_add(1.5, 2)          # 报错
except TypeError as e:
    print(f"错误：{e}")

# 提示：如需运行时类型检查，可用第三方库 pydantic 或 beartype
