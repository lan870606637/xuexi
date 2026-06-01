# -*- coding: utf-8 -*-
"""
07 - 主动抛异常 (raise) 与 异常链 (raise ... from)

raise 让你"主动"抛出异常 —— 用来做参数校验、状态检查。
raise ... from 让"包装后的高层异常"保留"原始的低层异常"，
            排错时一眼能看到根因。
"""

# ============================================================
# 1. raise —— 主动抛异常
# ============================================================
# 最常见用途：参数校验
def login(username, password):
    if not isinstance(username, str):
        raise TypeError(f"username 必须是字符串，得到 {type(username).__name__}")
    if len(password) < 6:
        raise ValueError("密码长度不能少于 6 位")
    print(f"  正在登录: {username}")


# 试一下
test_cases = [
    ("admin", "123456"),     # 正常
    (123,     "123456"),     # 类型错
    ("admin", "12"),         # 密码太短
]

for u, p in test_cases:
    print(f"\n参数: {u!r}, {p!r}")
    try:
        login(u, p)
    except (TypeError, ValueError) as e:
        print(f"  ✗ [{type(e).__name__}] {e}")


# ============================================================
# 2. 重抛 —— 接住之后"再抛一遍"
# ============================================================
# 想"在这一层先做点事（记日志/截图），但不消化掉异常"
def click(locator):
    print(f"  尝试点击 {locator}")
    try:
        # 假装找元素失败
        raise FileNotFoundError("元素 element 不存在")
    except FileNotFoundError:
        print("  → 截图保存到 screenshots/click_fail.png")
        raise            # ← 把原异常原封不动再抛出去
                         #   不写 raise 就意味着"消化掉了"


print("\n--- 重抛 ---")
try:
    click(("id", "login"))
except FileNotFoundError as e:
    print(f"  上层接到: {e}")


# ============================================================
# 3. 包装 —— 把低层异常"翻译"成业务层异常
# ============================================================
# 场景：底层抛 ConnectionError，但调用方根本不应该关心"网络细节"，
#       我们想给它抛一个"测试框架异常"

class TestFrameworkError(Exception):
    """框架顶层异常"""

def fetch_user(user_id):
    """假装是底层 HTTP 调用"""
    raise ConnectionError("DNS 解析失败")


def get_user_info(user_id):
    try:
        return fetch_user(user_id)
    except ConnectionError as e:
        # 不带 from 的话，原始异常的"根因信息"就丢了
        # 用 from e 把原异常挂到 __cause__ 上，traceback 会一起打印
        raise TestFrameworkError("获取用户失败") from e


print("\n--- 异常链 ---")
try:
    get_user_info(123)
except TestFrameworkError as e:
    print(f"  上层异常: {e}")
    print(f"  根因 (__cause__): {e.__cause__}")
    print(f"  根因类型: {type(e.__cause__).__name__}")


# ============================================================
# 4. raise ... from None —— 故意"抹掉"原异常
# ============================================================
# 偶尔有需求：原始异常信息太乱/有敏感数据，不想暴露给调用方
def safe_get(d, key):
    try:
        return d[key]
    except KeyError:
        # 不想暴露 KeyError 的细节，干脆给个干净的 ValueError
        raise ValueError(f"配置缺少必需的项: {key}") from None


print("\n--- 抹掉原异常 ---")
try:
    safe_get({"host": "x"}, "port")
except ValueError as e:
    print(f"  {e}")
    print(f"  __cause__: {e.__cause__}")    # None


# ============================================================
# 实战小例子：带重试的"安全点击"
# ============================================================
import random

class ElementNotFoundError(Exception):
    pass


def find_element_unstable(locator):
    """模拟一个不稳定的查找：70% 失败"""
    if random.random() < 0.7:
        raise ElementNotFoundError(f"未找到 {locator}")
    return f"<elem {locator}>"


def safe_click(locator, retries=3):
    """带重试的点击：失败重试 retries 次，仍失败则抛出包装异常"""
    last_error = None
    for i in range(1, retries + 1):
        try:
            elem = find_element_unstable(locator)
            print(f"   第 {i} 次: 找到了 {elem}，点击成功")
            return
        except ElementNotFoundError as e:
            print(f"   第 {i} 次: 失败 - {e}")
            last_error = e
    # 全部重试失败，抛出包装异常，保留最后一次的原因
    raise TestFrameworkError(
        f"点击 {locator} 重试 {retries} 次仍失败"
    ) from last_error


print("\n--- 重试 + 异常链 ---")
random.seed(0)         # 让结果可复现
try:
    safe_click(("id", "submit"))
except TestFrameworkError as e:
    print(f"  ✗ {e}")
    print(f"    根因: {e.__cause__}")


# ============================================================
# 三句话总结：
#   raise X("...")              主动抛
#   raise                       原样重抛（接住后又抛出去）
#   raise X("...") from origin  抛新异常，但保留原因（异常链）
# ============================================================
