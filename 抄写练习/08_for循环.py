# ============================================
# 题目08：for 循环
# 知识点：range / 遍历 / enumerate / zip / break / continue
# ============================================

# --- 基本 for 循环 ---
print("=== 遍历列表 ===")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
for fruit in fruits:
    print(fruit)

# --- range() ---
print("\n=== range 循环 ===")
for i in range(5):          # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(1, 6):       # 1 2 3 4 5
    print(i, end=" ")
print()

for i in range(0, 10, 2):   # 0 2 4 6 8，步长为 2
    print(i, end=" ")
print()

for i in range(10, 0, -1):  # 10 9 8 ... 1，倒序
    print(i, end=" ")
print()

# --- enumerate（同时获取下标和值）---
print("\n=== enumerate ===")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

for index, fruit in enumerate(fruits, start=1):  # 下标从1开始
    print(f"{index}. {fruit}")

# --- zip（同时遍历多个序列）---
print("\n=== zip ===")
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}：{score}分（{grade}）")

# zip 以最短的为准
a = [1, 2, 3, 4]
b = ["a", "b", "c"]
for x, y in zip(a, b):     # 只有3对
    print(x, y)

# --- break 和 continue ---
print("\n=== break / continue ===")
# break：遇到目标立即停止
for i in range(10):
    if i == 5:
        print(f"找到了 {i}，停止搜索")
        break
    print(i, end=" ")
print()

# continue：跳过本次，继续下一次
for i in range(10):
    if i % 2 == 0:
        continue            # 跳过偶数
    print(i, end=" ")
print()

# --- for...else（循环正常结束时执行 else）---
print("\n=== for...else ===")
target = 7
for i in range(5):
    if i == target:
        print(f"找到 {target}")
        break
else:
    print(f"没有找到 {target}")  # 循环未被 break 时执行

# --- 嵌套循环 ---
print("\n=== 嵌套循环（乘法表）===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()

# --- 遍历字符串 ---
print("\n=== 遍历字符串 ===")
for char in "Python":
    print(char, end=" ")
print()

# --- 遍历字典 ---
print("\n=== 遍历字典 ===")
config = {"host": "localhost", "port": 3306, "db": "mydb"}
for key, value in config.items():
    print(f"  {key} = {value}")

# --- 实用案例：累加求和 ---
print("\n=== 累加求和 ===")
total = 0
for i in range(1, 101):    # 1 到 100 求和
    total += i
print(f"1到100的和：{total}")  # 5050

# --- 收集结果到列表 ---
print("\n=== 收集结果 ===")
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)              # [1, 4, 9, 16, 25]
