# ============================================
# 题目10：函数基础
# 知识点：定义 / 参数 / 返回值 / 作用域
# ============================================

# --- 定义和调用函数 ---
def greet():
    print("你好，世界！")

greet()                     # 调用函数

# --- 带参数的函数 ---
def greet_user(name):
    print(f"你好，{name}！")

greet_user("张三")
greet_user("李四")

# --- 带返回值的函数 ---
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# --- 返回多个值（实际上是元组）---
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])
print(f"最小值：{low}，最大值：{high}")

# --- 默认参数 ---
print("\n=== 默认参数 ===")
def power(base, exp=2):     # exp 默认为 2
    return base ** exp

print(power(3))             # 3^2 = 9
print(power(3, 3))          # 3^3 = 27
print(power(2, 10))         # 1024

# 注意：默认参数必须在非默认参数后面
# def wrong(a=1, b): ...  # 这是错的！

# --- 关键字参数 ---
print("\n=== 关键字参数 ===")
def create_profile(name, age, city="未知"):
    return f"{name}，{age}岁，来自{city}"

print(create_profile("张三", 25, "北京"))
print(create_profile(age=30, name="李四"))  # 关键字参数，顺序无所谓
print(create_profile("王五", city="上海", age=28))

# --- *args（可变位置参数）---
print("\n=== *args ===")
def sum_all(*args):
    print(f"收到参数：{args}")   # args 是元组
    return sum(args)

print(sum_all(1, 2, 3))         # 6
print(sum_all(1, 2, 3, 4, 5))   # 15

def first_last(*args):
    return args[0], args[-1]

print(first_last(10, 20, 30, 40))  # (10, 40)

# --- **kwargs（可变关键字参数）---
print("\n=== **kwargs ===")
def print_info(**kwargs):
    print(f"收到参数：{kwargs}")  # kwargs 是字典
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="张三", age=25, city="北京")

# --- 混合参数顺序 ---
print("\n=== 混合参数 ===")
def mixed(a, b, *args, key="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"key={key}")
    print(f"kwargs={kwargs}")

mixed(1, 2, 3, 4, 5, key="special", x=10, y=20)

# --- 作用域（LEGB规则）---
print("\n=== 作用域 ===")
x = "全局变量"

def outer():
    x = "外层变量"
    def inner():
        x = "内层变量"
        print(f"inner: {x}")
    inner()
    print(f"outer: {x}")

outer()
print(f"global: {x}")       # 全局变量不受影响

# --- global 和 nonlocal ---
print("\n=== global ===")
counter = 0
def increment():
    global counter          # 声明要修改全局变量
    counter += 1

increment()
increment()
increment()
print(f"counter: {counter}")   # 3

print("\n=== nonlocal ===")
def make_counter():
    count = 0
    def inc():
        nonlocal count      # 声明修改外层函数的变量
        count += 1
        return count
    return inc

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3

# --- 函数也是对象 ---
print("\n=== 函数是对象 ===")
def square(x):
    return x * x

fn = square             # 把函数赋值给变量
print(fn(5))            # 25

def apply(func, value): # 函数作为参数传递
    return func(value)

print(apply(square, 4)) # 16
