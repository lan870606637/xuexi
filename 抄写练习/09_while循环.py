# ============================================
# 题目09：while 循环
# 知识点：while / break / continue / while-else / 无限循环
# ============================================

# --- 基本 while 循环 ---
print("=== 基本 while ===")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# --- 倒计时 ---
print("\n=== 倒计时 ===")
n = 5
while n > 0:
    print(f"{n}...")
    n -= 1
print("发射！")

# --- 累加 ---
print("\n=== 用 while 累加 ===")
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"1到100的和：{total}")   # 5050

# --- break（提前退出）---
print("\n=== while + break ===")
secret = 42
guess = 0
attempts = 0
guesses = [10, 55, 42, 30]   # 模拟用户输入序列

for g in guesses:
    guess = g
    attempts += 1
    if guess == secret:
        print(f"猜对了！答案是 {secret}，用了 {attempts} 次")
        break
    elif guess < secret:
        print(f"{guess} 太小了")
    else:
        print(f"{guess} 太大了")

# --- continue（跳过本次）---
print("\n=== while + continue ===")
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue            # 跳过3的倍数
    print(n, end=" ")
print()

# --- while...else ---
print("\n=== while...else ===")
items = [3, 7, 2, 8, 1]
target = 6
i = 0
while i < len(items):
    if items[i] == target:
        print(f"找到 {target}，在下标 {i}")
        break
    i += 1
else:
    print(f"{target} 不在列表中")  # 未被 break 时执行

# --- 无限循环（用 break 控制）---
print("\n=== 无限循环模拟 ===")
commands = ["open", "save", "quit"]   # 模拟命令序列
index = 0
while True:
    cmd = commands[index]
    index += 1
    print(f"执行命令：{cmd}")
    if cmd == "quit":
        print("程序退出")
        break

# --- 实用案例：数位分解 ---
print("\n=== 数位分解 ===")
num = 12345
digits = []
while num > 0:
    digits.append(num % 10)  # 取个位
    num //= 10               # 去掉个位
digits.reverse()
print(digits)               # [1, 2, 3, 4, 5]

# --- 实用案例：辗转相除法（求最大公约数）---
print("\n=== 最大公约数 ===")
a, b = 48, 18
while b != 0:
    a, b = b, a % b
print(f"最大公约数：{a}")    # 6

# --- while 实现 do-while 效果 ---
print("\n=== 模拟 do-while ===")
count = 0
while True:
    count += 1
    print(f"第 {count} 次执行")
    if count >= 3:
        break
