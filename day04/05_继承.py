# -*- coding: utf-8 -*-
"""
05 - 继承

要解决的问题：
    两个类有 80% 代码一样，剩下 20% 不同 —— 别复制粘贴！
    把相同部分写在"父类"，不同部分写在"子类"。
"""


# ============================================================
# 1. 最基本的继承
# ============================================================
# 父类（基类）：所有"页面"都需要的通用能力
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        print(f"   find({locator})")
        return f"<element {locator}>"

    def click(self, locator):
        self.find(locator)
        print("   click()")

    def type(self, locator, text):
        self.find(locator)
        print(f"   type({text!r})")


# 子类：写法 class 子类(父类)
# LoginPage 自动拥有 BasePage 的所有方法，不用重写
class LoginPage(BasePage):
    pass     # 暂时啥都没加，先看看效果


page = LoginPage(driver="<chrome>")
page.click(("id", "login"))      # 直接用了父类的 click


# ============================================================
# 2. 子类加自己的东西
# ============================================================
class LoginPage2(BasePage):
    # 子类有自己的 __init__：要记得调父类的，否则父类的初始化逻辑就丢了
    def __init__(self, driver):
        super().__init__(driver)              # 把 driver 交给父类的 __init__
        self.username = ("id", "user")        # 自己加的属性
        self.password = ("id", "pwd")
        self.submit   = ("id", "login")

    # 自己的业务方法，内部复用父类提供的能力
    def login(self, user, pwd):
        print(f"\n[LoginPage2] 登录 {user} / {pwd}")
        self.type(self.username, user)         # 用父类的 type
        self.type(self.password, pwd)
        self.click(self.submit)                # 用父类的 click


LoginPage2(driver="<chrome>").login("admin", "123456")


# ============================================================
# 3. 方法重写（override）—— 子类用自己的版本替换父类的同名方法
# ============================================================
class MobileLoginPage(LoginPage2):
    # 同名方法：调用 mobile_page.login(...) 时，会用这个版本
    def login(self, user, pwd):
        print("\n[Mobile] 先收起软键盘")
        # 如果还想用父类那段逻辑，用 super().方法名(...) 调
        super().login(user, pwd)
        print("[Mobile] 等待 Native 跳转")


MobileLoginPage(driver="<appium>").login("admin", "123456")


# ============================================================
# 4. 容易出错的几个点
# ============================================================
# (a) 子类 __init__ 一旦定义，就要主动 super().__init__(...)
class Wrong(BasePage):
    def __init__(self):
        # 没调 super().__init__()，driver 永远不会被设置
        self.locator = ("id", "x")


w = Wrong()
try:
    w.click(w.locator)   # 内部 self.driver 会怎样？这里只是打印没出事，
                         # 但真用 driver 时就崩了
except AttributeError as e:
    print("出错了:", e)


# (b) super() 能调到"上一层父类"。多层继承的链条会一层层往上找
class A:
    def hi(self): print("A.hi")
class B(A):
    def hi(self):
        super().hi()
        print("B.hi")
class C(B):
    def hi(self):
        super().hi()
        print("C.hi")

print()
C().hi()
# 输出顺序：A.hi -> B.hi -> C.hi


# ============================================================
# 心法
# ============================================================
# 什么时候用继承？
#   ✓ 子类"是一种"父类：LoginPage 是一种 Page、Dog 是一种 Animal
#   ✗ 只是为了"想复用几行代码"硬继承 —— 用组合（持有另一个对象）更好
#
# 在测试框架里，继承最经典的用法就是：
#   BasePage (通用)
#     ├── LoginPage
#     ├── HomePage
#     └── ProductPage  ...
# 通用能力（find/click/type/截图/日志）放父类，
# 页面专属逻辑（login/search/checkout）放各自子类。
# ============================================================
