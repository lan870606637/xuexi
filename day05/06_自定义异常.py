# -*- coding: utf-8 -*-
"""
06 - 自定义异常

为什么要自定义异常？
    内置的 ValueError、TypeError 太"通用"了 ——
    一段代码里出现 ValueError，可能是 100 种原因之一。
    自定义异常让"什么错"一目了然，调用方也能精确地捕获你想让它处理的错。

写法极其简单：继承一下 Exception 就完事。
"""

# ============================================================
# 1. 最简单的自定义异常
# ============================================================
class TestFrameworkError(Exception):
    """测试框架的基础异常 —— 所有自定义异常都继承它"""
    pass


# 派生几个更具体的（形成自己的异常体系）
class ElementNotFoundError(TestFrameworkError):
    """元素没找到"""
    pass


class TestDataError(TestFrameworkError):
    """测试数据格式错误"""
    pass


class APITimeoutError(TestFrameworkError):
    """接口请求超时"""
    pass


# 试用：跟内置异常用法完全一样
try:
    raise ElementNotFoundError("没找到登录按钮")
except ElementNotFoundError as e:
    print(f"[catch] {type(e).__name__}: {e}")


# ============================================================
# 2. 给异常加额外字段 —— 出错时多带点信息
# ============================================================
class ElementNotFoundError2(TestFrameworkError):
    """元素未找到（带详细信息）"""

    def __init__(self, locator, timeout=10):
        # 先把信息存到 self 上
        self.locator = locator
        self.timeout = timeout
        # 再调父类的 __init__，给一段人类可读的错误信息
        super().__init__(f"找不到元素 {locator}（已等 {timeout}s）")


# 用一下
print()
try:
    raise ElementNotFoundError2(("id", "login-btn"), timeout=30)
except ElementNotFoundError2 as e:
    print(f"[catch] {e}")
    # 还能取出我们存的字段
    print(f"        locator = {e.locator}")
    print(f"        timeout = {e.timeout}")


# ============================================================
# 3. 自定义异常 + 异常体系的真正威力 —— 分级捕获
# ============================================================
def find_element(locator):
    raise ElementNotFoundError(f"没找到 {locator}")

def call_api():
    raise APITimeoutError("接口 /login 超时")

def bad_data():
    raise TestDataError("用例缺少 password 字段")


# 写法 A：精确捕获某一类错
print("\n--- 只捕获元素错误 ---")
try:
    find_element(("id", "x"))
except ElementNotFoundError as e:
    print(f"  元素问题: {e}")
except TestFrameworkError as e:
    print(f"  其他框架问题: {e}")


# 写法 B：用"基类"一锅端
# 因为 ElementNotFound / TestData / APITimeout 都继承 TestFrameworkError
# 写一个 except TestFrameworkError 就能接住"这个框架抛出的任何异常"
print("\n--- 一锅端：除非是框架问题，否则让它崩 ---")
for fn in [find_element, call_api, bad_data]:
    try:
        fn(("id", "x")) if fn is find_element else fn()
    except TestFrameworkError as e:
        print(f"  框架问题 [{type(e).__name__}]: {e}")


# ============================================================
# 4. 什么时候该自定义异常？
# ------------------------------------------------------------
# 该自定义：
#   ✓ 写"框架/库"，希望用户能精确捕获你抛出的特定错误
#   ✓ 业务有清晰的错误分类（鉴权错 / 数据错 / 网络错）
#   ✓ 想给异常带额外字段（locator、retry_count、status_code...）
#
# 不该自定义：
#   ✗ 内置的 ValueError 已经能精确表达 → 直接用
#   ✗ 只在一处用一次 → 直接 raise ValueError("xxx") 就行
# ============================================================
