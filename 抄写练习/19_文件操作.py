# ============================================
# 题目19：文件读写操作
# 知识点：open() / with / 读写模式 / JSON / CSV
# ============================================

import os
import json
import csv

# --- 写文件 ---
print("=== 写文件 ===")
# 'w' 写模式（覆盖），'a' 追加模式
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.writelines(["第三行\n", "第四行\n", "第五行\n"])

print("test.txt 写入完成")

# --- 读文件 ---
print("\n=== 读文件 ===")
# 读取全部内容
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("全部内容：")
    print(content)

# 读取成行列表
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()   # 每行末尾带 \n
    print(f"共 {len(lines)} 行")
    for line in lines:
        print(repr(line))   # 显示 \n

# 逐行读取（内存友好）
print("\n逐行读取：")
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() 去掉换行符

# --- 追加模式 ---
print("\n=== 追加模式 ===")
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("第六行（追加）\n")
    f.write("第七行（追加）\n")

with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())

# --- 文件指针操作 ---
print("=== 文件指针 ===")
with open("test.txt", "r", encoding="utf-8") as f:
    f.seek(0)               # 移到开头
    first_line = f.readline()
    print(f"第一行：{first_line.strip()}")
    print(f"当前位置：{f.tell()}")
    f.seek(0)               # 重置到开头
    content = f.read(6)     # 读取6个字节
    print(f"前6字节：{content!r}")

# --- JSON 文件 ---
print("\n=== JSON 文件 ===")
data = {
    "users": [
        {"id": 1, "name": "张三", "age": 25, "active": True},
        {"id": 2, "name": "李四", "age": 30, "active": False},
    ],
    "total": 2
}

# 写 JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("JSON 写入完成")

# 读 JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"读取到 {loaded['total']} 个用户")
for user in loaded["users"]:
    print(f"  {user['name']}，{user['age']}岁")

# JSON 字符串互转
json_str = json.dumps({"key": "value", "num": 42}, ensure_ascii=False)
print(f"\nJSON 字符串：{json_str}")
obj = json.loads(json_str)
print(f"解析后：{obj}")

# --- CSV 文件 ---
print("\n=== CSV 文件 ===")
headers = ["姓名", "年龄", "成绩", "城市"]
rows = [
    ["张三", 20, 85, "北京"],
    ["李四", 22, 92, "上海"],
    ["王五", 19, 78, "广州"],
]

# 写 CSV
with open("students.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
print("CSV 写入完成")

# 读 CSV
print("读取 CSV：")
with open("students.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)  # DictReader 将每行映射为字典
    for row in reader:
        print(f"  {row['姓名']}，{row['年龄']}岁，{row['成绩']}分，{row['城市']}")

# --- 文件与路径操作 ---
print("\n=== 路径操作 ===")
print(os.path.exists("test.txt"))       # True
print(os.path.isfile("test.txt"))       # True
print(os.path.isdir("."))               # True
print(os.path.getsize("test.txt"))      # 文件大小（字节）
print(os.path.abspath("test.txt"))      # 绝对路径

# os.path 拼接（跨平台安全）
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir, "subdir", "file.txt")
print(f"拼接路径：{filepath}")

# --- 清理测试文件 ---
for fname in ["test.txt", "data.json", "students.csv"]:
    if os.path.exists(fname):
        os.remove(fname)
        print(f"已删除：{fname}")
