# ============================================
# 题目18：生成器与迭代器
# 知识点：yield / 生成器函数 / 生成器表达式 / 自定义迭代器
# ============================================

# --- 迭代器协议 ---
# 迭代器需要实现：__iter__() 和 __next__()

print("=== 手动模拟迭代 ===")
lst = [1, 2, 3]
it = iter(lst)          # 获取迭代器
print(next(it))         # 1
print(next(it))         # 2
print(next(it))         # 3
# print(next(it))       # 会抛出 StopIteration

# --- 自定义迭代器 ---
print("\n=== 自定义迭代器 ===")
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self             # 返回自身

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 信号：没有更多元素了
        self.current -= 1
        return self.current + 1

for n in CountDown(5):
    print(n, end=" ")
print()

# --- 生成器函数（用 yield）---
print("\n=== 生成器函数 ===")
def count_down(start):
    while start > 0:
        yield start             # 暂停并返回值，下次从这里继续
        start -= 1

gen = count_down(5)
print(type(gen))                # <class 'generator'>

for n in gen:
    print(n, end=" ")
print()

# yield 执行细节
def demo_yield():
    print("第一次 yield 前")
    yield 1
    print("第一次和第二次 yield 之间")
    yield 2
    print("第二次 yield 后")

g = demo_yield()
print(next(g))      # 打印"第一次 yield 前"，返回 1
print(next(g))      # 打印"第一次和第二次...", 返回 2

# --- 无限生成器 ---
print("\n=== 无限生成器 ===")
def natural_numbers(start=1):
    while True:
        yield start
        start += 1

gen = natural_numbers()
for _ in range(5):
    print(next(gen), end=" ")
print()

# --- 斐波那契生成器 ---
print("\n=== 斐波那契数列 ===")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])  # 前10个斐波那契数

# --- 生成器表达式 ---
print("\n=== 生成器表达式 ===")
# 列表推导式：立即计算全部，占内存
lst = [x**2 for x in range(10)]    # 立即生成 [0, 1, 4, 9, ...]

# 生成器表达式：按需计算，省内存
gen = (x**2 for x in range(10))    # 不立即计算

# 对大数据很重要
import sys
big_list = [x**2 for x in range(100000)]
big_gen = (x**2 for x in range(100000))
print(f"列表大小：{sys.getsizeof(big_list):,} 字节")
print(f"生成器大小：{sys.getsizeof(big_gen):,} 字节")

# --- yield from（委托生成器）---
print("\n=== yield from ===")
def chain(*iterables):
    for it in iterables:
        yield from it           # 等价于：for x in it: yield x

for item in chain([1, 2], "abc", (3, 4)):
    print(item, end=" ")
print()

# --- 生成器的 send()（双向通信）---
print("\n=== send() ===")
def accumulator():
    total = 0
    while True:
        value = yield total     # 暂停，返回 total，并等待接收 value
        if value is None:
            break
        total += value

acc = accumulator()
print(next(acc))        # 启动生成器，到第一个 yield，返回 0
print(acc.send(10))     # 发送 10，total = 10，返回 10
print(acc.send(20))     # 发送 20，total = 30，返回 30
print(acc.send(5))      # total = 35

# --- itertools 工具 ---
print("\n=== itertools ===")
import itertools

# 无限计数
counter = itertools.count(1, 2)  # 从1开始，步长2
print(list(itertools.islice(counter, 5)))   # [1, 3, 5, 7, 9]

# 循环
cycler = itertools.cycle(["A", "B", "C"])
print([next(cycler) for _ in range(7)])  # ['A','B','C','A','B','C','A']

# 重复
print(list(itertools.repeat(42, 4)))    # [42, 42, 42, 42]

# 连接
print(list(itertools.chain([1, 2], [3, 4], [5])))  # [1,2,3,4,5]

# 组合
print(list(itertools.combinations([1, 2, 3], 2)))  # 从3个中取2个

# 全排列
print(list(itertools.permutations([1, 2, 3], 2)))
