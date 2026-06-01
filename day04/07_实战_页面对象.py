# -*- coding: utf-8 -*-
"""
07 - 实战：用 OOP 写一个"登录页面对象"（POM 的雏形）

把今天学的东西全部用上：
    类、self、实例属性、类属性、继承、super、方法重写

目标：让"测试用例代码"看起来像中文 ——
    page = LoginPage(driver)
    page.login("admin", "123456")
    assert page.has_error_message() is False
"""


# ============================================================
# 第 1 层：通用基类 BasePage
#   - 把所有页面都要的"找元素 / 点击 / 输入 / 截图"放这里
#   - 以后想换 driver、加日志、加截图，只改这一个文件
# ============================================================
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        print(f"[BasePage] 接入 driver: {driver}")

    def find(self, locator):
        by, value = locator
        print(f"   find ({by}={value!r})")
        return f"<elem {value}>"

    def click(self, locator):
        self.find(locator)
        print("   → click")

    def type(self, locator, text):
        self.find(locator)
        print(f"   → type {text!r}")

    def text_of(self, locator):
        self.find(locator)
        # 这里返回一段模拟文本，真实代码里就是 element.text
        return "<模拟元素的文字>"

    def exists(self, locator):
        # 简化版：真实环境下 find 失败会抛异常，捕获后返回 False
        print(f"   exists? {locator}")
        return True


# ============================================================
# 第 2 层：登录页面 LoginPage
#   - 把"这个页面长什么样"集中放在 类属性
#   - 把"这个页面能做什么"写成方法
#   - 元素定位以后改了，只改这里一处，所有用例不用动
# ============================================================
class LoginPage(BasePage):
    # 这个页面的 URL
    URL = "/login"

    # 元素定位器集中放，命名清晰
    USERNAME_INPUT = ("id", "username")
    PASSWORD_INPUT = ("id", "password")
    SUBMIT_BUTTON  = ("id", "login-btn")
    ERROR_MESSAGE  = ("class", "error-msg")
    WELCOME_TITLE  = ("class", "welcome")

    # 业务行为（高层动作）
    def login(self, user, pwd):
        print(f"\n>>> 登录: {user} / {pwd}")
        self.type(self.USERNAME_INPUT, user)
        self.type(self.PASSWORD_INPUT, pwd)
        self.click(self.SUBMIT_BUTTON)

    def error_message(self):
        """返回页面上的错误提示文字"""
        return self.text_of(self.ERROR_MESSAGE)

    def has_error(self):
        """页面是否显示了错误？"""
        return self.exists(self.ERROR_MESSAGE)


# ============================================================
# 第 3 层：移动端登录页（演示"继承 + 方法重写"）
#   - 移动端跟 PC 端 90% 一样，只在 login 前后多两步
#   - 完全复用 LoginPage 的代码
# ============================================================
class MobileLoginPage(LoginPage):
    def login(self, user, pwd):
        print("[Mobile] 步骤A - 收起软键盘")
        super().login(user, pwd)       # 复用父类的整段 login
        print("[Mobile] 步骤B - 等待 Native 跳转")


# ============================================================
# 使用：测试代码读起来非常干净
# ============================================================
print("=" * 50)
print("场景 1：PC 端登录")
print("=" * 50)
page = LoginPage(driver="<chrome-driver>")
page.login("admin", "123456")
print("有错误吗?", page.has_error())

print("\n" + "=" * 50)
print("场景 2：移动端登录")
print("=" * 50)
mobile = MobileLoginPage(driver="<appium-driver>")
mobile.login("admin", "123456")


# ============================================================
# 体会一下设计的好处：
#
#   1. 测试代码看不到"find/click/type"这些细节
#      —— 全部被 BasePage 吃掉了
#   2. 元素 id 改了，只改 LoginPage 顶部的几行常量
#   3. 想给所有页面加"操作前自动截图"？
#      只改 BasePage.click 一处
#   4. 移动端跟 PC 端的差异，被局限在 MobileLoginPage 一个类
#
# 这就是后面 Day 14 要讲的 Page Object Model (POM) 的核心思想。
# ============================================================
