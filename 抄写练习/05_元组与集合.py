# ============================================
# 题目05：元组与集合
# 知识点：tuple 不可变序列 / set 无序不重复集合
# ============================================

# ====== 元组 tuple ======
print("====== 元组 ======")

# --- 创建元组 ---
point = (3, 4)
rgb = (255, 128, 0)
single = (42,)              # 单元素元组，必须加逗号
empty_tuple = ()

print(point, rgb)
print(type(single))         # <class 'tuple'>
print(type((42)))           # <class 'int'>，不加逗号是整数！

# --- 访问元组 ---
print("\n=== 元组访问 ===")
print(rgb[0])               # 255
print(rgb[-1])              # 0
print(rgb[0:2])             # (255, 128)

# --- 解包（非常常用）---
print("\n=== 元组解包 ===")
x, y = point
print(f"x={x}, y={y}")

r, g, b = rgb
print(f"R={r}, G={g}, B={b}")

# 带星号的解包
first, *rest = (1, 2, 3, 4, 5)
print(f"first={first}, rest={rest}")

*init, last = (1, 2, 3, 4, 5)
print(f"init={init}, last={last}")

a, *middle, z = (1, 2, 3, 4, 5)
print(f"a={a}, middle={middle}, z={z}")

# --- 元组常用方法 ---
print("\n=== 元组方法 ===")
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))        # 统计 2 的个数：3
print(nums.index(3))        # 3 的下标：2
print(len(nums))            # 长度：6

# --- 元组与列表互转 ---
print("\n=== 互转 ===")
lst = list(point)           # 元组 -> 列表
lst.append(0)               # 可以修改
tpl = tuple(lst)            # 列表 -> 元组
print(tpl)

# --- 为什么用元组 ---
# 1. 比列表更快、更省内存
# 2. 可以作为字典的键（列表不行）
# 3. 表达"不应该修改"的语义
coords = {(0, 0): "原点", (1, 0): "右", (0, 1): "上"}
print(coords[(0, 0)])


# ====== 集合 set ======
print("\n====== 集合 ======")

# --- 创建集合 ---
fruits = {"苹果", "香蕉", "橙子", "苹果"}  # 自动去重
print(fruits)               # 无序，每次输出顺序可能不同
print(type(fruits))         # <class 'set'>

empty_set = set()           # 创建空集合，不能用 {}（那是空字典）
nums_set = set([1, 2, 2, 3, 3, 3])  # 从列表创建，自动去重
print(nums_set)

# --- 增删元素 ---
print("\n=== 集合增删 ===")
fruits.add("葡萄")           # 添加单个元素
print(fruits)

fruits.discard("香蕉")       # 删除，不存在不报错
fruits.discard("榴莲")       # 不存在，安全删除
print(fruits)

fruits.remove("橙子")        # 删除，不存在会报错
print(fruits)

popped = fruits.pop()        # 随机弹出一个元素
print(f"弹出：{popped}")

# --- 集合运算（最有用的地方）---
print("\n=== 集合运算 ===")
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(f"A ∪ B = {A | B}")        # 并集：所有元素
print(f"A ∩ B = {A & B}")        # 交集：共有元素
print(f"A - B = {A - B}")        # 差集：A 中有但 B 没有
print(f"A △ B = {A ^ B}")        # 对称差集：只在一个集合中

# 也可以用方法调用
print(A.union(B))           # 并集
print(A.intersection(B))    # 交集
print(A.difference(B))      # 差集
print(A.symmetric_difference(B))  # 对称差集

# --- 子集与超集 ---
print("\n=== 子集超集 ===")
small = {1, 2, 3}
big = {1, 2, 3, 4, 5}
print(small.issubset(big))       # True，small 是 big 的子集
print(big.issuperset(small))     # True，big 是 small 的超集
print(small.isdisjoint({6, 7}))  # True，没有共同元素

# --- 去重小技巧 ---
print("\n=== 列表去重 ===")
data = [1, 3, 2, 3, 1, 4, 2, 5]
unique = list(set(data))    # 去重（顺序不保证）
print(unique)

