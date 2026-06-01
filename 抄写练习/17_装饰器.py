# ============================================
# 题目17：装饰器
# 知识点：函数装饰器 / 参数化装饰器 / 类装饰器 / functools.wraps
# ============================================

import time
import functools

# --- 理解装饰器：先看闭包 ---
print("=== 先理解闭包 ===")
def make_multiplier(n):
    def multiply(x):
        return x * n           # multiply 引用了外层的 n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))               # 10
print(triple(5))               # 15

# --- 手动实现装饰器 ---
print("\n=== 手动装饰 ===")
def timer(func):               # 接受一个函数
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # 调用原函数
        end = time.time()
        print(f"{func.__name__} 耗时：{end - start:.6f}秒")
        return result
    return wrapper             # 返回包装后的函数

def slow_sum(n):
    return sum(range(n))

# 手动装饰
slow_sum = timer(slow_sum)
print(slow_sum(1000000))

# --- 用 @ 语法糖 ---
print("\n=== @ 语法 ===")
@timer                         # 等价于：greet = timer(greet)
def greet(name):
    print(f"你好，{name}！")
    return f"已问候 {name}"

result = greet("张三")
print(result)

# --- functools.wraps（保留原函数信息）---
print("\n=== functools.wraps ===")
def my_decorator(func):
    @functools.wraps(func)      # 保留 func 的 __name__ / __doc__
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__} 之前")
        result = func(*args, **kwargs)
        print(f"调用 {func.__name__} 之后")
        return result
    return wrapper

@my_decorator
def say_hello():
    """打招呼函数"""
    print("Hello!")

say_hello()
print(say_hello.__name__)       # say_hello（不是 wrapper）
print(say_hello.__doc__)        # 打招呼函数

# --- 参数化装饰器（装饰器工厂）---
print("\n=== 参数化装饰器 ===")
def repeat(times):              # 最外层：接收装饰器参数
    def decorator(func):        # 中间层：接收被装饰的函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # 最内层：实际执行
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)                      # 调用3次
def hi():
    print("Hi!")

hi()

@repeat(2)
def say(msg):
    print(f"说：{msg}")

say("你好")

# --- 多个装饰器叠加 ---
print("\n=== 多个装饰器 ===")
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic                         # 先 italic 后 bold（从下到上）
def text(content):
    return content

print(text("Python"))           # <b><i>Python</i></b>

# --- 类装饰器 ---
print("\n=== 类装饰器 ===")
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
            print(f"计算 {args}")
        else:
            print(f"缓存命中 {args}")
        return self.cache[args]

@Cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print(fibonacci(6))             # 第二次直接取缓存

# --- 实用装饰器：日志记录 ---
print("\n=== 日志装饰器 ===")
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[LOG] 调用 {func.__name__}({all_args})")
        try:
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} 返回 {result!r}")
            return result
        except Exception as e:
            print(f"[LOG] {func.__name__} 抛出 {type(e).__name__}: {e}")
            raise
    return wrapper

@logger
def divide(a, b):
    return a / b

divide(10, 2)
try:
    divide(10, 0)
except ZeroDivisionError:
    pass
