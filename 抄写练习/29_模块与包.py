# ============================================
# 题目29：模块与包
# 知识点：import / from...import / 常用标准库 / __name__
# ============================================

# --- 导入方式 ---
import os                           # 导入整个模块
import sys                          # 导入整个模块
from pathlib import Path            # 从模块中导入特定内容
from datetime import datetime, date # 导入多个
import json as j                    # 起别名
from os.path import join, exists    # 从子模块导入

# --- os 模块（操作系统接口）---
print("=== os 模块 ===")
print(f"当前目录：{os.getcwd()}")
print(f"目录分隔符：{os.sep}")
print(f"换行符：{repr(os.linesep)}")
print(f"CPU核心数：{os.cpu_count()}")

# 环境变量
path_env = os.environ.get("PATH", "未设置")
print(f"PATH 长度：{len(path_env)}")

# 路径操作
p = os.path.join("folder", "subfolder", "file.txt")
print(f"\n拼接路径：{p}")
print(f"目录名：{os.path.dirname(p)}")
print(f"文件名：{os.path.basename(p)}")
print(f"分割：{os.path.splitext('test.py')}")   # ('test', '.py')
print(f"绝对路径：{os.path.abspath('test.py')}")

# 列出目录
current_dir = os.getcwd()
items = os.listdir(current_dir)
print(f"\n当前目录项目数：{len(items)}")
# 只显示 .py 文件
py_files = [f for f in items if f.endswith(".py")]
print(f"Python 文件：{py_files[:5]}")

# --- pathlib（现代路径操作，推荐）---
print("\n=== pathlib ===")
p = Path(".")                       # 当前目录
print(f"绝对路径：{p.resolve()}")
print(f"是目录：{p.is_dir()}")

# 构建路径（用 / 拼接，非常直观）
config_path = Path.home() / ".config" / "app" / "settings.json"
print(f"配置路径：{config_path}")

# 路径属性
script = Path(__file__)             # 当前脚本路径
print(f"\n当前脚本：{script}")
print(f"文件名：{script.name}")
print(f"后缀：{script.suffix}")
print(f"父目录：{script.parent}")

# 遍历目录
py_count = len(list(Path(".").glob("*.py")))
print(f"当前目录 .py 文件数：{py_count}")

# --- sys 模块 ---
print("\n=== sys 模块 ===")
print(f"Python 版本：{sys.version}")
print(f"平台：{sys.platform}")
print(f"最大整数：{sys.maxsize}")
print(f"模块搜索路径（前3个）：")
for p in sys.path[:3]:
    print(f"  {p}")

# --- json 模块（已设别名）---
print("\n=== json 模块 ===")
data = {"name": "张三", "scores": [85, 92, 78]}
json_str = j.dumps(data, ensure_ascii=False)
print(json_str)
obj = j.loads(json_str)
print(obj)

# --- __name__ 的作用 ---
print("\n=== __name__ ===")
print(f"__name__ = {__name__}")
# 直接运行时：__name__ == '__main__'
# 被导入时：__name__ == 模块文件名（不含.py）
# 标准写法：
if __name__ == "__main__":
    print("作为主程序运行")
    # 测试代码放这里，被 import 时不执行

# --- 常用标准库速览 ---
print("\n=== 常用标准库 ===")
# os, sys, pathlib    文件系统和系统操作
# json, csv, pickle   数据序列化
# datetime, time      日期和时间
# math, random        数学和随机数
# re                  正则表达式
# collections         容器数据类型
# itertools           迭代器工具
# functools           函数工具（reduce, lru_cache...）
# contextlib          上下文管理器工具
# threading, asyncio  并发
# subprocess          运行子进程
# logging             日志
# argparse            命令行参数
# unittest            测试
# http, urllib        HTTP
# hashlib             哈希

# --- string 模块常量 ---
import string
print(string.ascii_letters)         # 所有字母
print(string.ascii_lowercase)       # 小写字母
print(string.ascii_uppercase)       # 大写字母
print(string.digits)                # 数字
print(string.punctuation)           # 标点
print(string.whitespace)            # 空白字符

# --- hashlib（哈希）---
print("\n=== hashlib ===")
import hashlib
text = "Hello, Python!"
md5 = hashlib.md5(text.encode()).hexdigest()
sha256 = hashlib.sha256(text.encode()).hexdigest()
print(f"MD5:    {md5}")
print(f"SHA256: {sha256}")
