# ============================================
# 题目11：推导式
# 知识点：列表推导式 / 字典推导式 / 集合推导式 / 生成器表达式
# ============================================

# --- 列表推导式基本语法 ---
# [表达式 for 变量 in 可迭代对象 if 条件]

print("=== 列表推导式 ===")
# 普通写法
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)

# 推导式写法（更简洁）
squares = [i ** 2 for i in range(1, 6)]
print(squares)              # [1, 4, 9, 16, 25]

# 带条件的推导式
evens = [i for i in range(20) if i % 2 == 0]
print(evens)                # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 字符串操作
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)

# 过滤列表
names = ["Alice", "Bob", "", "Charlie", "", "Dave"]
non_empty = [name for name in names if name]    # 过滤空字符串
print(non_empty)

# --- 带 if-else 的推导式（三元表达式）---
print("\n=== 带 if-else 的推导式 ===")
nums = [-3, -2, -1, 0, 1, 2, 3]
# 负数变0，其他保留
result = [x if x > 0 else 0 for x in nums]
print(result)               # [0, 0, 0, 0, 1, 2, 3]

# 标记奇偶
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 7)]
print(labels)

# --- 嵌套推导式 ---
print("\n=== 嵌套推导式 ===")
# 二维列表展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)                 # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建二维矩阵
grid = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in grid:
    print(row)

# --- 字典推导式 ---
print("\n=== 字典推导式 ===")
# {键表达式: 值表达式 for 变量 in 可迭代对象}
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)         # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 键值互换
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)             # {1: 'a', 2: 'b', 3: 'c'}

# 带条件过滤
scores = {"张三": 55, "李四": 82, "王五": 91, "赵六": 67}
pass_scores = {name: s for name, s in scores.items() if s >= 60}
print(pass_scores)

# 统计字符频率
text = "hello world"
char_count = {c: text.count(c) for c in set(text) if c != " "}
print(char_count)

# --- 集合推导式 ---
print("\n=== 集合推导式 ===")
# {表达式 for 变量 in 可迭代对象}
unique_squares = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(unique_squares)       # {0, 1, 4, 9}，自动去重

# --- 生成器表达式（节省内存）---
print("\n=== 生成器表达式 ===")
# (表达式 for 变量 in 可迭代对象)
# 与列表推导式的区别：不立即计算所有值，按需生成

gen = (x**2 for x in range(1, 6))
print(gen)                  # <generator object>，不是列表

# 逐个取出
for val in gen:
    print(val, end=" ")
print()

# 生成器表达式用于函数调用（最常见用法）
total = sum(x**2 for x in range(1, 101))  # 不需要额外括号
print(f"1到100平方和：{total}")

# any() 和 all() 配合生成器表达式
nums = [2, 4, 6, 7, 8]
print(any(n % 2 != 0 for n in nums))   # True，有奇数
print(all(n > 0 for n in nums))         # True，全是正数

# --- 实用案例 ---
print("\n=== 实用案例 ===")
# 找出所有 3 位回文数
palindromes = [n for n in range(100, 1000) if str(n) == str(n)[::-1]]
print(f"3位回文数个数：{len(palindromes)}")
print(f"前10个：{palindromes[:10]}")
