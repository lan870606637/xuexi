# ============================================
# 题目01：变量与数据类型
# 知识点：int / float / str / bool / None / 类型转换
# ============================================

# --- 整数 int ---
age = 25
year = 2024
negative = -10
big_number = 1_000_000      # 下划线分隔，增强可读性

print("=== 整数 ===")
print(age, year, negative, big_number)
print(type(age))            # <class 'int'>

# --- 浮点数 float ---
height = 1.75
pi = 3.14159
scientific = 2.5e3          # 科学计数法，等于 2500.0

print("\n=== 浮点数 ===")
print(height, pi, scientific)
print(type(pi))             # <class 'float'>

# --- 字符串 str ---
name = "张三"
greeting = '你好'
multiline = """
这是
多行字符串
"""

print("\n=== 字符串 ===")
print(name, greeting)
print(multiline)
print(type(name))           # <class 'str'>

# --- 布尔值 bool ---
is_student = True
is_adult = False

print("=== 布尔值 ===")
print(is_student, is_adult)
print(type(is_student))     # <class 'bool'>
print(True + True)          # 2，bool 可以参与数学运算
print(True * 10)            # 10

# --- None ---
result = None
print("\n=== None ===")
print(result)
print(type(result))         # <class 'NoneType'>
print(result is None)       # True，用 is 而不是 == 判断 None

# --- 类型转换 ---
print("\n=== 类型转换 ===")
x = "42"
print(int(x))               # 字符串转整数  -> 42
print(float(x))             # 字符串转浮点  -> 42.0
print(str(100))             # 整数转字符串  -> '100'
print(bool(0))              # 0 -> False
print(bool(""))             # 空字符串 -> False
print(bool("hello"))        # 非空字符串 -> True
print(bool(42))             # 非零整数 -> True

# --- 多重赋值 ---
print("\n=== 多重赋值 ===")
a, b, c = 1, 2, 3
print(a, b, c)

a, b = b, a                 # 一行交换两个变量
print(f"交换后：a={a}, b={b}")

x = y = z = 100             # 同时赋相同值
print(x, y, z)
