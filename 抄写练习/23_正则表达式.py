# ============================================
# 题目23：正则表达式
# 知识点：re 模块 / 基本模式 / 分组 / 替换 / 常用场景
# ============================================

import re

# --- 正则基本语法速查 ---
# .     匹配任意单个字符（除换行符）
# ^     字符串开头
# $     字符串结尾
# *     0次或多次
# +     1次或多次
# ?     0次或1次
# {n}   恰好n次
# {n,m} n到m次
# []    字符类，如 [abc] [a-z] [0-9]
# [^]   否定字符类，如 [^abc]
# |     或，如 cat|dog
# ()    分组
# \d    数字 [0-9]
# \D    非数字
# \w    字母/数字/下划线 [a-zA-Z0-9_]
# \W    非单词字符
# \s    空白字符（空格、制表符等）
# \S    非空白
# \b    单词边界

# --- 四个主要函数 ---
print("=== re.search() ===")
# search：在字符串中搜索，找到第一个匹配
text = "我的手机号是 138-1234-5678，备用号码 159-8765-4321"
match = re.search(r"\d{3}-\d{4}-\d{4}", text)
if match:
    print(f"找到：{match.group()}")
    print(f"位置：{match.start()} - {match.end()}")

print("\n=== re.match() ===")
# match：只从字符串开头匹配
print(re.match(r"\d+", "123abc"))   # 匹配成功
print(re.match(r"\d+", "abc123"))   # None，开头不是数字

print("\n=== re.findall() ===")
# findall：找到所有匹配，返回列表
phones = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print(f"所有手机号：{phones}")

words = re.findall(r"\b[a-zA-Z]+\b", "Hello World 123 Python!")
print(f"所有英文单词：{words}")

print("\n=== re.finditer() ===")
# finditer：找到所有匹配，返回迭代器（节省内存）
for m in re.finditer(r"\d{3}-\d{4}-\d{4}", text):
    print(f"  找到 {m.group()} 在位置 {m.start()}")

print("\n=== re.sub() 替换 ===")
# sub：替换匹配的内容
cleaned = re.sub(r"\d{3}-\d{4}-\d{4}", "***-****-****", text)
print(cleaned)

# 使用函数作为替换
def mask_phone(m):
    phone = m.group()
    return phone[:3] + "-****-" + phone[-4:]

masked = re.sub(r"\d{3}-\d{4}-\d{4}", mask_phone, text)
print(masked)

print("\n=== re.split() 分割 ===")
# split：按模式分割字符串
data = "苹果,香蕉;橙子、葡萄 芒果"
fruits = re.split(r"[,;、\s]+", data)  # 按多种分隔符分割
print(fruits)

# --- 分组 ---
print("\n=== 分组 ===")
date_text = "今天是 2024-06-15，明天是 2024-06-16"
pattern = r"(\d{4})-(\d{2})-(\d{2})"   # 3个分组

match = re.search(pattern, date_text)
print(f"完整匹配：{match.group(0)}")    # 或 match.group()
print(f"年：{match.group(1)}")
print(f"月：{match.group(2)}")
print(f"日：{match.group(3)}")
print(f"所有组：{match.groups()}")

# 命名分组
pattern_named = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
m = re.search(pattern_named, date_text)
print(f"\n命名分组：年={m.group('year')}, 月={m.group('month')}, 日={m.group('day')}")
print(f"字典形式：{m.groupdict()}")

# findall 带分组 -> 返回元组列表
dates = re.findall(r"(\d{4})-(\d{2})-(\d{2})", date_text)
print(f"\n所有日期：{dates}")

# --- 编译正则（提高性能）---
print("\n=== 编译正则 ===")
phone_pattern = re.compile(r"\d{3}-\d{4}-\d{4}")  # 预编译
print(phone_pattern.findall(text))

# --- 修饰符 ---
print("\n=== 修饰符 ===")
text2 = "Hello\nWorld\nPython"

# re.IGNORECASE / re.I：忽略大小写
print(re.findall(r"hello", text2, re.IGNORECASE))   # ['Hello']

# re.MULTILINE / re.M：^ $ 匹配每行
print(re.findall(r"^\w+", text2, re.MULTILINE))     # 每行开头的词

# re.DOTALL / re.S：. 匹配换行符
match = re.search(r"Hello.World", text2, re.DOTALL)
print(match)

# --- 常用正则示例 ---
print("\n=== 常用正则 ===")
patterns = {
    "邮箱": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "中国手机": r"1[3-9]\d{9}",
    "IP地址": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "中文": r"[一-鿿]+",
    "纯数字": r"^\d+$",
}

test_strings = [
    "user@example.com",
    "13812345678",
    "192.168.1.100",
    "你好世界",
    "12345",
    "abc123",
]

for s in test_strings:
    for name, pattern in patterns.items():
        if re.search(pattern, s):
            print(f"  '{s}' 匹配：{name}")
            break
