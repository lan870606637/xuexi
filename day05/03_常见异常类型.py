# -*- coding: utf-8 -*-
"""
03 - 必须认识的 7 个常见异常

看到 Traceback 的最后一行，先看冒号前的"类型名"。
认识下面这 7 个，能覆盖 90% 的日常报错。
"""

# ============================================================
# 1. ValueError —— 类型对，但值不对
# ============================================================
# int() 能接受 "123" 但不能接受 "abc" —— 值不合法
try:
    int("abc")
except ValueError as e:
    print("[ValueError] ", e)


# ============================================================
# 2. TypeError —— 类型本身不对
# ============================================================
# 字符串和整数不能直接相加
try:
    result = "abc" + 5
except TypeError as e:
    print("[TypeError]  ", e)


# ============================================================
# 3. KeyError —— 字典里没有这个 key
# ============================================================
data = {"name": "Tom", "age": 18}
try:
    print(data["email"])
except KeyError as e:
    # 注意：e 打印出来是 'email' （带引号），因为它是 key 本身
    print("[KeyError]   ", "没有 key:", e)


# ============================================================
# 4. IndexError —— 列表/元组下标越界
# ============================================================
lst = [1, 2, 3]
try:
    print(lst[10])
except IndexError as e:
    print("[IndexError] ", e)


# ============================================================
# 5. AttributeError —— 对象没这个属性/方法
# ============================================================
s = "hello"
try:
    s.append("!")          # str 没有 append 方法（list 才有）
except AttributeError as e:
    print("[AttributeErr]", e)


# ============================================================
# 6. ZeroDivisionError —— 除以零
# ============================================================
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("[ZeroDivErr] ", e)


# ============================================================
# 7. FileNotFoundError —— 文件找不到
# ============================================================
try:
    with open("根本不存在的文件.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print("[FileNotFound]", e)


# ============================================================
# 还有几个测试场景常见的（属于上面这些的子类或扩展）：
# ------------------------------------------------------------
# TimeoutError                  —— 超时
# ConnectionError               —— 网络断开
# PermissionError               —— 没权限读写
# json.JSONDecodeError          —— JSON 解析失败
# requests.exceptions.HTTPError —— HTTP 4xx/5xx
# selenium 里:
#     NoSuchElementException    —— 元素找不到
#     TimeoutException          —— 等元素超时
#     StaleElementReference     —— 元素引用失效（页面刷新过）
# ============================================================


# ============================================================
# 异常的继承关系（重要！）
# ------------------------------------------------------------
# 所有异常都继承自 BaseException
#     └── Exception          ← 几乎所有"业务异常"都在这棵树上
#             ├── ValueError
#             ├── TypeError
#             ├── LookupError
#             │       ├── KeyError
#             │       └── IndexError
#             ├── ArithmeticError
#             │       └── ZeroDivisionError
#             ├── OSError
#             │       ├── FileNotFoundError
#             │       ├── PermissionError
#             │       └── TimeoutError
#             └── ...
#
# 所以  except Exception  能接住几乎所有的业务异常，
#     但接不住 KeyboardInterrupt（Ctrl+C）和 SystemExit —— 这两个是
#     BaseException 直接子类，专门设计成"不该被业务代码吞掉"。
# ============================================================

print("\n小诀窍：报错时记下'类型名'，搜引擎一查就知道大概是什么问题")
