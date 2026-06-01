# ============================================
# 题目21：数字运算与 math / random 模块
# 知识点：运算符 / 内置函数 / math / random
# ============================================

import math
import random

# --- Python 数字运算 ---
print("=== 基本运算 ===")
print(10 + 3)           # 13，加
print(10 - 3)           # 7，减
print(10 * 3)           # 30，乘
print(10 / 3)           # 3.333...，真除（结果是浮点）
print(10 // 3)          # 3，整除（向下取整）
print(10 % 3)           # 1，取模（余数）
print(2 ** 10)          # 1024，幂运算

print(-7 // 2)          # -4，向下取整（注意！不是 -3）
print(-7 % 2)           # 1（Python 的取模：结果与除数同号）

# --- 内置数字函数 ---
print("\n=== 内置函数 ===")
print(abs(-42))         # 42，绝对值
print(abs(-3.14))       # 3.14

print(round(3.14159, 2))    # 3.14，四舍五入
print(round(3.5))           # 4（Python 3 使用银行家舍入）
print(round(2.5))           # 2（四舍六入五成双）

print(max(1, 5, 3, 9, 2))   # 9
print(min(1, 5, 3, 9, 2))   # 1
print(sum([1, 2, 3, 4, 5])) # 15

print(divmod(17, 5))        # (3, 2)，同时返回商和余数

# 进制转换
print(bin(255))             # 0b11111111
print(oct(255))             # 0o377
print(hex(255))             # 0xff
print(int("ff", 16))        # 255，16进制字符串转整数
print(int("11111111", 2))   # 255，二进制字符串转整数

# --- 浮点数注意事项 ---
print("\n=== 浮点精度 ===")
print(0.1 + 0.2)            # 0.30000000000000004
print(0.1 + 0.2 == 0.3)     # False！

# 解决方案：round 或 decimal
print(round(0.1 + 0.2, 10) == round(0.3, 10))  # True

import decimal
a = decimal.Decimal("0.1")
b = decimal.Decimal("0.2")
print(a + b)                # 0.3（精确）
print(a + b == decimal.Decimal("0.3"))  # True

# --- math 模块 ---
print("\n=== math 模块 ===")
print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828459045
print(math.inf)             # 正无穷
print(math.nan)             # 非数字

# 数学函数
print(math.sqrt(16))        # 4.0，平方根
print(math.pow(2, 10))      # 1024.0，幂（返回浮点）
print(math.log(100, 10))    # 2.0，以10为底的对数
print(math.log2(8))         # 3.0，以2为底
print(math.log(math.e))     # 1.0，自然对数

# 三角函数
angle = math.pi / 4         # 45度
print(f"sin(45°) = {math.sin(angle):.4f}")  # 0.7071
print(f"cos(45°) = {math.cos(angle):.4f}")  # 0.7071
print(f"tan(45°) = {math.tan(angle):.4f}")  # 1.0000
print(f"degrees: {math.degrees(angle)}")    # 45.0
print(f"radians: {math.radians(45):.4f}")  # 0.7854

# 向上/向下取整
print(math.floor(3.7))      # 3，向下取整
print(math.ceil(3.1))       # 4，向上取整
print(math.trunc(3.7))      # 3，截断小数（朝0方向）
print(math.trunc(-3.7))     # -3

# 其他
print(math.factorial(5))    # 120，阶乘
print(math.gcd(48, 18))     # 6，最大公约数
print(math.isnan(float('nan')))  # True
print(math.isinf(math.inf))     # True

# --- random 模块 ---
print("\n=== random 模块 ===")
random.seed(42)             # 设置种子，保证可重复

print(random.random())      # [0.0, 1.0) 的随机浮点数
print(random.uniform(1, 10))   # [1, 10] 的随机浮点数
print(random.randint(1, 6))    # [1, 6] 的随机整数（掷骰子）
print(random.randrange(0, 10, 2))  # 从 range 中随机选

# 从序列中随机选择
fruits = ["苹果", "香蕉", "橙子", "葡萄", "芒果"]
print(random.choice(fruits))        # 随机选1个
print(random.choices(fruits, k=3))  # 有放回地选3个
print(random.sample(fruits, k=3))   # 不放回地选3个（不重复）

# 随机打乱
nums = list(range(1, 11))
random.shuffle(nums)
print(nums)

# 正态分布
samples = [random.gauss(mu=170, sigma=10) for _ in range(5)]
print([round(s, 1) for s in samples])
