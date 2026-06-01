# -*- coding: utf-8 -*-
"""
02 - try / except 的基本写法

完整结构：

    try:
        可能出错的代码
    except 异常类型 as 变量名:
        出错后的处理
"""

# ============================================================
# 1. 最简单的形式
# ============================================================
user_input = "abc"       # 模拟用户输入了一段非数字

try:
    n = int(user_input)
except ValueError as e:
    # as e 把"异常对象"赋给变量 e，方便看错误信息
    print(f"转换失败: {e}")
    n = 0                # 给个默认值兜底

print("n =", n)


# ============================================================
# 2. try 块里有多行，遇到第一处异常就跳到 except
# ============================================================
print("\n--- 多行 try ---")
try:
    print("第 1 行: 开始")
    print("第 2 行: 10 / 0 =", 10 / 0)   # ← 在这里炸了
    print("第 3 行: 我永远不会被执行")
except ZeroDivisionError as e:
    print(f"接住了: {e}")


# ============================================================
# 3. 异常对象 e 能做什么
# ============================================================
print("\n--- 异常对象长什么样 ---")
try:
    int("not a number")
except ValueError as e:
    print("类型:", type(e).__name__)     # ValueError
    print("信息:", str(e))                # invalid literal for int() ...
    print("args:", e.args)                # ('invalid literal for int() ...',)


# ============================================================
# 4. except 的"异常类型"决定能接住什么
# ============================================================
# 写 except ValueError 只能接 ValueError，其他类型的异常照样让它崩
print("\n--- 写错了类型 ---")
try:
    # 这是 ZeroDivisionError，不是 ValueError
    result = 10 / 0
except ValueError:        # 故意写错类型
    print("我接不到，因为类型不对")

# 如果上面真跑到 except 也不会进，但因为没接住，
# 整个程序会崩 —— 上面这段被我注释成 try 内部正常通过，所以演示一下


# 想"什么异常都接"，用 Exception（几乎能接所有常见异常）
print("\n--- 用 Exception 兜底 ---")
try:
    result = 10 / 0
except Exception as e:
    print(f"接到了 {type(e).__name__}: {e}")
# 但要小心：滥用 Exception 会把 bug 全部藏起来，见 README "心法"


# ============================================================
# 5. 实战感觉 —— 安全获取字典值
# ============================================================
config = {"host": "localhost", "port": 8080}

# 老方法：先 if-in 再取
if "username" in config:
    user = config["username"]
else:
    user = "anonymous"
print("\n方法 A:", user)

# 用异常的方法（不一定更好，看场景；这里只是熟悉语法）
try:
    user = config["username"]
except KeyError:
    user = "anonymous"
print("方法 B:", user)

# 其实最 Pythonic 的写法是用 .get()
user = config.get("username", "anonymous")
print("方法 C:", user)
# 经验：能用 .get() 就用 .get()，能用 if-in 就用 if-in，
# 真正"该用异常的场景"是后续的文件操作、网络请求等


# ============================================================
# 一句话总结：
#   try 包住"可能出错的几行"
#   except 写"接住的类型"和"接住后怎么办"
#   except 类型要尽量精确，别上来就用 Exception
# ============================================================
