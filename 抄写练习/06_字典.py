# ============================================
# 题目06：字典
# 知识点：增删改查 / 遍历 / 嵌套 / 常用方法
# ============================================

# --- 创建字典 ---
person = {"name": "张三", "age": 25, "city": "北京"}
empty = {}
from_keys = dict.fromkeys(["a", "b", "c"], 0)   # 从键列表创建

print("=== 创建字典 ===")
print(person)
print(from_keys)            # {'a': 0, 'b': 0, 'c': 0}

# --- 访问值 ---
print("\n=== 访问值 ===")
print(person["name"])           # 张三，键不存在会报 KeyError
print(person.get("age"))        # 25
print(person.get("email"))      # None，键不存在返回 None
print(person.get("email", "未填写"))  # 键不存在返回默认值

# --- 增加与修改 ---
print("\n=== 增改 ===")
person["email"] = "zhangsan@example.com"  # 新键赋值 = 添加
person["age"] = 26                         # 已有键赋值 = 修改
print(person)

person.update({"city": "上海", "phone": "138xxxx"})  # 批量更新
print(person)

# --- 删除 ---
print("\n=== 删除 ===")
removed = person.pop("phone")       # 删除并返回值
print(f"删除了：{removed}")
print(person)

del person["email"]                 # 删除键值对
print(person)

last = person.popitem()             # 删除并返回最后插入的键值对
print(f"删除了：{last}")

# --- 遍历字典（重要）---
print("\n=== 遍历 ===")
scores = {"语文": 88, "数学": 95, "英语": 72}

# 遍历键
for key in scores:
    print(key, end="  ")
print()

# 遍历值
for value in scores.values():
    print(value, end="  ")
print()

# 遍历键值对（最常用）
for key, value in scores.items():
    print(f"{key}：{value}分")

# --- 常用方法 ---
print("\n=== 常用方法 ===")
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())             # dict_keys(['a', 'b', 'c'])
print(d.values())           # dict_values([1, 2, 3])
print(d.items())            # dict_items([('a', 1), ...])
print(list(d.keys()))       # 转成普通列表

print("a" in d)             # True，检查键是否存在
print(1 in d.values())      # True，检查值是否存在
print(len(d))               # 3

# --- setdefault ---
print("\n=== setdefault ===")
config = {"host": "localhost"}
config.setdefault("port", 3306)     # 键不存在时才设置默认值
config.setdefault("host", "remote") # 键已存在，不修改
print(config)

# --- 嵌套字典 ---
print("\n=== 嵌套字典 ===")
students = {
    "S001": {"name": "小红", "score": 92},
    "S002": {"name": "小明", "score": 85},
    "S003": {"name": "小李", "score": 78},
}

# 访问嵌套值
print(students["S001"]["name"])     # 小红

# 遍历嵌套字典
for sid, info in students.items():
    print(f"{sid}: {info['name']} - {info['score']}分")

# 找出最高分学生
best = max(students.values(), key=lambda x: x["score"])
print(f"最高分：{best['name']} {best['score']}分")

# --- 字典合并（Python 3.9+）---
print("\n=== 字典合并 ===")
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
merged = a | b              # 合并，b 覆盖 a 的同名键
print(merged)               # {'x': 1, 'y': 99, 'z': 3}
