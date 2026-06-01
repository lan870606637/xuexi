# ============================================
# 题目02：字符串常用方法
# 知识点：索引、切片、大小写、查找、替换、分割
# ============================================

s = "Hello, Python World!"

# --- 基本信息 ---
print("=== 基本信息 ===")
print(len(s))               # 长度：20
print(s[0])                 # 第一个字符：H
print(s[-1])                # 最后一个字符：!
print(s[7:13])              # 切片：Python

# --- 切片进阶 ---
print("\n=== 切片 ===")
print(s[:5])                # 前5个：Hello
print(s[7:])                # 从第7个到结尾
print(s[::2])               # 每隔一个取一个
print(s[::-1])              # 反转字符串

# --- 大小写 ---
print("\n=== 大小写 ===")
print(s.upper())            # 全大写
print(s.lower())            # 全小写
print(s.title())            # 每个单词首字母大写
print(s.swapcase())         # 大小写互换

# --- 查找与判断 ---
print("\n=== 查找与判断 ===")
print(s.find("Python"))     # 返回下标 7，找不到返回 -1
print(s.index("Python"))    # 返回下标 7，找不到报错
print(s.count("l"))         # 统计出现次数
print("Python" in s)        # True，成员运算
print(s.startswith("Hello"))# True
print(s.endswith("!"))      # True

# --- 替换 ---
print("\n=== 替换 ===")
print(s.replace("Python", "World"))     # 替换第一次出现
print(s.replace("l", "L", 1))          # 只替换第一个 l

# --- 分割与拼接 ---
print("\n=== 分割与拼接 ===")
words = s.split(" ")        # 按空格分割，返回列表
print(words)
csv_line = "a,b,c,d"
print(csv_line.split(","))  # 按逗号分割

joined = "-".join(["2024", "01", "01"])  # 拼接列表为字符串
print(joined)               # 2024-01-01

# --- 去除空白 ---
print("\n=== 去除空白 ===")
padded = "   hello   "
print(padded.strip())       # 去除两端空白
print(padded.lstrip())      # 只去左端
print(padded.rstrip())      # 只去右端

# --- 对齐与填充 ---
print("\n=== 对齐填充 ===")
word = "hi"
print(word.center(10, "*")) # ****hi****
print(word.ljust(10, "-"))  # hi--------
print(word.rjust(10, "-"))  # --------hi
print("42".zfill(5))        # 00042，用0填充

# --- 判断类型 ---
print("\n=== 判断字符类型 ===")
print("123".isdigit())      # True，全是数字
print("abc".isalpha())      # True，全是字母
print("abc123".isalnum())   # True，字母或数字
print("   ".isspace())      # True，全是空白
