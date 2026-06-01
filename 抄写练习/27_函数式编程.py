# ============================================
# 题目27：函数式编程思想
# 知识点：纯函数 / 不可变 / 闭包 / 柯里化 / 函数组合
# ============================================

from functools import partial, reduce, lru_cache

# --- 纯函数：相同输入，永远相同输出，无副作用 ---
print("=== 纯函数 ===")
# 非纯函数（有副作用）
total = 0
def add_impure(x):
    global total
    total += x      # 修改了外部状态
    return total

# 纯函数
def add_pure(current_total, x):
    return current_total + x    # 不修改外部状态

print(add_pure(0, 5))   # 5
print(add_pure(5, 3))   # 8

# 函数式累加
nums = [1, 2, 3, 4, 5]
final = reduce(add_pure, nums, 0)
print(f"累加：{final}")         # 15

# --- 闭包（复习）---
print("\n=== 闭包 ===")
def make_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeting("Hello")
hi = make_greeting("Hi")
print(hello("张三"))     # Hello, 张三!
print(hi("李四"))        # Hi, 李四!

# 带状态的闭包
def make_counter(start=0, step=1):
    count = [start]     # 用列表包装，因为 closure 无法直接修改不可变量（Python 3 可用 nonlocal）
    def counter():
        val = count[0]
        count[0] += step
        return val
    return counter

c1 = make_counter()
c2 = make_counter(10, 2)
print([c1() for _ in range(5)])   # [0, 1, 2, 3, 4]
print([c2() for _ in range(5)])   # [10, 12, 14, 16, 18]

# --- partial：偏函数（固定部分参数）---
print("\n=== partial（偏函数）===")
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)      # 固定 exp=2
cube = partial(power, exp=3)        # 固定 exp=3

print(square(5))        # 25
print(cube(3))          # 27

# 实用示例
def log(level, message):
    print(f"[{level.upper()}] {message}")

info = partial(log, "info")
error = partial(log, "error")
warning = partial(log, "warning")

info("服务启动")
error("连接失败")
warning("内存不足")

# --- 函数组合 ---
print("\n=== 函数组合 ===")
def compose(*funcs):
    """从右到左组合函数：compose(f, g, h)(x) = f(g(h(x)))"""
    def composed(x):
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result
    return composed

def double(x): return x * 2
def add_one(x): return x + 1
def square(x): return x * x

# double(add_one(square(3))) = double(add_one(9)) = double(10) = 20
transform = compose(double, add_one, square)
print(transform(3))         # 20

# pipe：从左到右（更直观）
def pipe(*funcs):
    def piped(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return piped

process = pipe(square, add_one, double)
print(process(3))           # (3^2 + 1) * 2 = 20

# --- 记忆化（缓存）---
print("\n=== 记忆化 ===")
@lru_cache(maxsize=128)
def expensive_calc(n):
    print(f"  计算 {n}...")
    if n <= 1:
        return n
    return expensive_calc(n - 1) + expensive_calc(n - 2)

print("第一次调用：")
print(expensive_calc(10))   # 计算很多次
print("第二次调用：")
print(expensive_calc(10))   # 直接从缓存返回，不打印"计算..."

# lru_cache 信息
info = expensive_calc.cache_info()
print(f"缓存命中：{info.hits}，未命中：{info.misses}")

# --- 高阶函数链式处理数据 ---
print("\n=== 函数式数据处理 ===")
data = [
    {"name": "张三", "age": 25, "salary": 8000},
    {"name": "李四", "age": 30, "salary": 12000},
    {"name": "王五", "age": 22, "salary": 6000},
    {"name": "赵六", "age": 28, "salary": 9500},
    {"name": "小明", "age": 35, "salary": 15000},
]

# 命令式风格
result_imperative = []
for person in data:
    if person["age"] >= 25:
        result_imperative.append(person["salary"])
result_imperative.sort(reverse=True)

# 函数式风格
result_functional = sorted(
    map(lambda p: p["salary"],
        filter(lambda p: p["age"] >= 25, data)),
    reverse=True
)

print("命令式：", result_imperative)
print("函数式：", result_functional)

# 用推导式（Python 风格的"函数式"）
result_pythonic = sorted(
    [p["salary"] for p in data if p["age"] >= 25],
    reverse=True
)
print("推导式：", result_pythonic)

# 总工资
total = reduce(lambda acc, p: acc + p["salary"], data, 0)
print(f"总工资：{total}")
print(f"平均工资：{total / len(data):.0f}")
