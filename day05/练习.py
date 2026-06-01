# -*- coding: utf-8 -*-
"""
Day 05 · 练习

完成下面 4 个 TODO，跑通后再对照文件末尾的参考答案。
"""

# ============================================================
# 题 1：安全转整数
# ------------------------------------------------------------
# 写一个函数 to_int(s, default=0)：
#   - 能转就返回 int
#   - 转不了就返回 default，不要让程序崩
#
# 示例：
#   to_int("123")    -> 123
#   to_int("abc")    -> 0
#   to_int("abc", -1) -> -1
# ============================================================

# TODO 1


# 测试
# print(to_int("123"))
# print(to_int("abc"))
# print(to_int("abc", -1))


# ============================================================
# 题 2：批量累加
# ------------------------------------------------------------
# 输入一个字符串列表 ["1", "22", "abc", "3"]，
# 返回元组 (成功累加的和, 失败的元素列表)
# 上面例子应返回:  (26, ["abc"])
# ============================================================

# TODO 2: def sum_safe(items): ...


# 测试
# print(sum_safe(["1", "22", "abc", "3", "5x"]))   # (26, ['abc', '5x'])


# ============================================================
# 题 3：自定义异常 + 校验函数
# ------------------------------------------------------------
# 1) 定义异常 LoginDataError，继承 Exception
# 2) 写函数 validate(data: dict)，校验失败就抛 LoginDataError：
#       - data 必须是 dict
#       - 必须有 username 和 password
#       - password 长度 >= 6
# 3) 写一段循环，用 try/except 调用 validate，把通过和失败都打印出来
# ============================================================

# TODO 3


# 测试
# test_cases = [
#     {"username": "admin", "password": "123456"},   # OK
#     {"username": "admin", "password": "12"},       # 太短
#     {"username": "admin"},                         # 缺 password
#     "not a dict",                                  # 类型错
# ]


# ============================================================
# 题 4：带重试的函数 + 异常链
# ------------------------------------------------------------
# 写一个装饰一般化的函数 do_with_retry(func, retries=3)：
#   - 重复执行 func()，成功就返回结果
#   - 全部失败时，抛 RuntimeError("操作失败")，
#     并把最后一次的真实异常用  raise ... from  挂上
#
# 测试时用一个"永远失败"的函数验证
# ============================================================

# TODO 4


# 测试
# def always_fail():
#     raise ValueError("一直失败")
#
# try:
#     do_with_retry(always_fail, retries=3)
# except RuntimeError as e:
#     print("外层异常:", e)
#     print("根因   :", e.__cause__)


# ============================================================
# ★★★ 参考答案 ★★★（写完再看！）
# ============================================================
ANSWER = '''
# ----- 题 1 -----
def to_int(s, default=0):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


# ----- 题 2 -----
def sum_safe(items):
    total = 0
    failed = []
    for s in items:
        try:
            total += int(s)
        except (ValueError, TypeError):
            failed.append(s)
    return total, failed


# ----- 题 3 -----
class LoginDataError(Exception):
    pass


def validate(data):
    if not isinstance(data, dict):
        raise LoginDataError(f"必须是 dict，得到 {type(data).__name__}")
    if "username" not in data:
        raise LoginDataError("缺少 username")
    if "password" not in data:
        raise LoginDataError("缺少 password")
    if len(data["password"]) < 6:
        raise LoginDataError("password 长度必须 >= 6")
    return True


for case in test_cases:
    try:
        validate(case)
        print("✓ 通过:", case)
    except LoginDataError as e:
        print("✗ 失败:", case, "->", e)


# ----- 题 4 -----
def do_with_retry(func, retries=3):
    last = None
    for i in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            print(f"  第 {i} 次失败: {e}")
            last = e
    raise RuntimeError("操作失败") from last
'''

# 想看答案就取消下面这行的注释
# print(ANSWER)
