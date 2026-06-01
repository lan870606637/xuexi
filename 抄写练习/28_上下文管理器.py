# ============================================
# 题目28：上下文管理器
# 知识点：with 语句 / __enter__ __exit__ / contextlib
# ============================================

import time
import contextlib
import os

# --- 为什么需要上下文管理器 ---
# 保证"配对操作"一定执行：
# 打开文件 -> 关闭文件
# 获取锁 -> 释放锁
# 开始事务 -> 提交/回滚事务

# --- 基本文件操作（最常见的 with）---
print("=== 文件 with ===")
# 用 with，文件一定会关闭（即使发生异常）
with open("temp.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("第二行\n")
# 这里文件已自动关闭
print(f"文件是否关闭：{f.closed}")   # True

with open("temp.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

os.remove("temp.txt")

# --- 实现上下文管理器（类方式）---
print("=== 自定义上下文管理器（类）===")
class Timer:
    def __init__(self, name=""):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        print(f"[{self.name}] 开始计时")
        return self                     # 赋给 as 后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] 耗时：{self.elapsed*1000:.2f}ms")
        # 返回 True 会抑制异常，False/None 会让异常传播
        return False

with Timer("计算") as t:
    result = sum(range(1000000))
    print(f"结果：{result}")

print(f"外部访问耗时：{t.elapsed*1000:.2f}ms")

# --- 异常抑制 ---
print("\n=== 异常处理 ===")
class SuppressErrors:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exceptions):
            print(f"  已抑制异常：{exc_type.__name__}: {exc_val}")
            return True     # 抑制异常
        return False        # 让异常传播

with SuppressErrors(ValueError, TypeError):
    int("not a number")     # ValueError 被抑制
    print("这行不会执行")

print("继续执行...")

# --- 用 contextlib.contextmanager（推荐方式）---
print("\n=== contextlib.contextmanager ===")
@contextlib.contextmanager
def timer(name=""):
    start = time.perf_counter()
    print(f"[{name}] 开始")
    try:
        yield                           # with 块在这里执行
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{name}] 耗时：{elapsed*1000:.2f}ms")

with timer("排序"):
    data = list(range(10000, 0, -1))
    data.sort()

# --- contextlib.suppress ---
print("\n=== contextlib.suppress ===")
with contextlib.suppress(FileNotFoundError):
    os.remove("不存在的文件.txt")   # 不会报错
print("安全执行完毕")

# --- 多个 with ---
print("\n=== 多个上下文管理器 ===")
# 嵌套写法（旧写法）
# with open("a.txt", "w") as a:
#     with open("b.txt", "w") as b:
#         pass

# 单行写法（推荐）
with open("a.txt", "w", encoding="utf-8") as a, \
     open("b.txt", "w", encoding="utf-8") as b:
    a.write("文件A")
    b.write("文件B")

for fname in ["a.txt", "b.txt"]:
    with open(fname, "r", encoding="utf-8") as f:
        print(f"{fname}: {f.read()}")
    os.remove(fname)

# --- 实用案例：数据库事务模拟 ---
print("\n=== 数据库事务 ===")
@contextlib.contextmanager
def transaction(db_name):
    print(f"[{db_name}] 开始事务")
    try:
        yield db_name
        print(f"[{db_name}] 提交事务")     # 没有异常才提交
    except Exception as e:
        print(f"[{db_name}] 回滚事务：{e}")  # 异常时回滚
        raise

try:
    with transaction("users_db") as db:
        print(f"  在 {db} 中插入数据...")
        print(f"  在 {db} 中更新数据...")
        # raise ValueError("模拟错误")    # 取消注释测试回滚
        print(f"  操作完成")
except ValueError:
    pass

# --- 可重用的上下文管理器 ---
print("\n=== 临时目录 ===")
import tempfile
import shutil

@contextlib.contextmanager
def temp_directory():
    tmpdir = tempfile.mkdtemp()
    print(f"创建临时目录：{tmpdir}")
    try:
        yield tmpdir
    finally:
        shutil.rmtree(tmpdir)
        print(f"删除临时目录：{tmpdir}")

with temp_directory() as tmpdir:
    filepath = os.path.join(tmpdir, "test.txt")
    with open(filepath, "w") as f:
        f.write("临时文件内容")
    print(f"临时文件存在：{os.path.exists(filepath)}")

print(f"退出后临时目录存在：{os.path.exists(tmpdir)}")
