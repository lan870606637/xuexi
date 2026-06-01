# ============================================
# 题目12：lambda 与高阶函数
# 知识点：lambda / map / filter / sorted / reduce
# ============================================

from functools import reduce

# --- lambda 表达式 ---
# lambda 参数: 返回值表达式（只能有一个表达式）

print("=== lambda 基础 ===")
# 普通函数
def square(x):
    return x * x

# 等价的 lambda
square_l = lambda x: x * x

print(square(5))            # 25
print(square_l(5))          # 25

# 多个参数
add = lambda a, b: a + b
print(add(3, 4))            # 7

# 带条件
is_even = lambda x: x % 2 == 0
print(is_even(4))           # True
print(is_even(7))           # False

# --- lambda 最常见的用法：作为排序的 key ---
print("\n=== lambda 用于排序 ===")
students = [
    {"name": "张三", "score": 85, "age": 20},
    {"name": "李四", "score": 92, "age": 22},
    {"name": "王五", "score": 78, "age": 19},
    {"name": "赵六", "score": 92, "age": 21},
]

# 按成绩排序
by_score = sorted(students, key=lambda s: s["score"])
for st in by_score:
    print(f"{st['name']}: {st['score']}")

# 按成绩降序，成绩相同按年龄升序
by_multi = sorted(students, key=lambda s: (-s["score"], s["age"]))
print("\n成绩降序（相同按年龄升序）：")
for st in by_multi:
    print(f"{st['name']}: {st['score']}，{st['age']}岁")

# --- map()：对每个元素做相同操作 ---
print("\n=== map() ===")
nums = [1, 2, 3, 4, 5]

# 每个数平方
squared = list(map(lambda x: x**2, nums))
print(squared)              # [1, 4, 9, 16, 25]

# 字符串处理
words = ["hello", "world", "python"]
upper = list(map(str.upper, words))     # 可以直接传方法
print(upper)

# 两个列表对应元素相加
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)                 # [11, 22, 33]

# --- filter()：过滤元素 ---
print("\n=== filter() ===")
nums = range(1, 11)

# 只保留偶数
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                # [2, 4, 6, 8, 10]

# 过滤空字符串
names = ["Alice", "", "Bob", None, "Charlie", ""]
valid = list(filter(None, names))  # filter(None, ...) 过滤假值
print(valid)                # ['Alice', 'Bob', 'Charlie']

# 过滤负数
mixed = [-3, -1, 0, 2, 4, -5, 6]
positives = list(filter(lambda x: x > 0, mixed))
print(positives)            # [2, 4, 6]

# --- reduce()：累积计算 ---
print("\n=== reduce() ===")
nums = [1, 2, 3, 4, 5]

# 求积
product = reduce(lambda a, b: a * b, nums)
print(f"连乘：{product}")   # 120

# 求最大值（演示原理，实际用 max()）
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(f"最大值：{maximum}") # 5

# 带初始值
total = reduce(lambda a, b: a + b, nums, 100)
print(f"从100开始累加：{total}")  # 115

# --- sorted() 的高级用法 ---
print("\n=== sorted 高级用法 ===")
words = ["banana", "fig", "apple", "cherry", "date"]

# 按长度排序
print(sorted(words, key=len))

# 按最后一个字母排序
print(sorted(words, key=lambda w: w[-1]))

# 忽略大小写排序
mixed_case = ["Banana", "apple", "Cherry", "date"]
print(sorted(mixed_case, key=str.lower))

# --- 链式使用 ---
print("\n=== 链式使用 ===")
data = [5, -3, 8, -1, 2, -7, 4]

# 取出正数，平方，从大到小排
result = sorted(
    map(lambda x: x**2, filter(lambda x: x > 0, data)),
    reverse=True
)
print(result)               # [64, 25, 16, 4]

# 用列表推导式等价实现（更清晰）
result2 = sorted([x**2 for x in data if x > 0], reverse=True)
print(result2)
