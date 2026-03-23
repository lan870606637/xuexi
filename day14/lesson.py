# -*- coding: utf-8 -*-
"""
Day 14: Day 14
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：POM简介"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：POM简介")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    POM (Page Object Model) 页面对象模式
    为什么使用POM？
    1. 代码复用 - 页面元素定位集中管理
    2. 维护方便 - 页面变化只需修改一处
    3. 可读性高 - 测试代码像自然语言
    4. 降低耦合 - 页面操作与测试逻辑分离
    POM结构:
    ├── pages/              # 页面对象
    │   ├── base_page.py    # 基础页面类
    │   ├── login_page.py   # 登录页面
    │   └── home_page.py    # 首页
    ├── tests/              # 测试用例
    │   └── test_login.py
    └── conftest.py         # 共享fixture
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：基础页面类 (BasePage)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：基础页面类 (BasePage)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class BasePage:
        """
        基础页面类
        所有页面对象都继承此类
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.driver = driver
            self.timeout = 10
        # ==================== 元素查找 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_element():
            """
            查找单个元素
            locator格式: ("id", "value") 或 ("xpath", "//...")
            """
            by, value = locator
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 查找元素: {by}={value}")
            # 实际代码: return self.driver.find_element(by, value)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_elements():
            """查找多个元素"""
            by, value = locator
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 查找多个元素: {by}={value}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return [MockElement(by, value)]
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wait_for_element():
            """显式等待元素"""
            timeout = timeout or self.timeout
            by, value = locator
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 等待元素: {by}={value}, 超时:{timeout}s")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_element_present():
            """判断元素是否存在"""
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                self.find_element(locator)
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return True
            except:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return False
        # ==================== 元素操作 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            """点击元素"""
            element = self.find_element(locator)
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 点击元素")
            element.click()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            """输入文本"""
            element = self.find_element(locator)
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 输入: {text}")
            element.clear()
            element.send_keys(text)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_text():
            """获取元素文本"""
            element = self.find_element(locator)
            text = element.text
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 获取文本: {text}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return text
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_attribute():
            """获取元素属性"""
            element = self.find_element(locator)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return element.get_attribute(attribute)
        # ==================== 手势操作 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def swipe_up():
            """向上滑动"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[BasePage] 向上滑动")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def swipe_down():
            """向下滑动"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[BasePage] 向下滑动")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def swipe_left():
            """向左滑动"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[BasePage] 向左滑动")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def swipe_right():
            """向右滑动"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[BasePage] 向右滑动")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def long_press():
            """长按"""
            element = self.find_element(locator)
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[BasePage] 长按元素 {duration}ms")
        # ==================== 等待 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wait():
            """固定等待"""
            # import - 导入模块
            # 作用: 引入其他模块的功能使用
            import time
            time.sleep(seconds)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def implicitly_wait():
            """隐式等待"""
            self.driver.implicitly_wait(seconds)
    # 模拟元素
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockElement:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.by = by
            self.value = value
            self._text = f"Text({value})"
        # 【装饰器 @property】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @property
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def text():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._text
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def clear():
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            self._text = text
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_attribute():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：具体页面对象"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：具体页面对象")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class LoginPage(BasePage):
        """
        登录页面
        封装登录相关的元素和操作
        """
        # 元素定位器 - 集中管理
        USERNAME_INPUT = ("id", "com.example:id/username")
        PASSWORD_INPUT = ("id", "com.example:id/password")
        LOGIN_BUTTON = ("id", "com.example:id/login_button")
        ERROR_MESSAGE = ("id", "com.example:id/error_message")
        REMEMBER_ME = ("id", "com.example:id/remember_me")
        FORGOT_PASSWORD = ("id", "com.example:id/forgot_password")
        # ==================== 页面操作 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def input_username():
            """输入用户名"""
            self.send_keys(self.USERNAME_INPUT, username)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self  # 支持链式调用
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def input_password():
            """输入密码"""
            self.send_keys(self.PASSWORD_INPUT, password)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_login():
            """点击登录按钮"""
            self.click(self.LOGIN_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_remember_me():
            """点击记住我"""
            self.click(self.REMEMBER_ME)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_forgot_password():
            """点击忘记密码"""
            self.click(self.FORGOT_PASSWORD)
            # 返回新页面
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ForgotPasswordPage(self.driver)
        # ==================== 业务流程 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login():
            """
            完整的登录流程
            支持链式调用: login_page.login("user", "pass")
            """
            self.input_username(username)
            self.input_password(password)
            self.click_login()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return HomePage(self.driver)  # 登录成功后跳转到首页
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login_with_remember():
            """带记住我的登录"""
            self.input_username(username)
            self.input_password(password)
            self.click_remember_me()
            self.click_login()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return HomePage(self.driver)
        # ==================== 验证方法 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_error_message():
            """获取错误提示"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_text(self.ERROR_MESSAGE)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_login_button_enabled():
            """登录按钮是否可用"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_attribute(self.LOGIN_BUTTON, "enabled") == "true"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_error_displayed():
            """错误信息是否显示"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.is_element_present(self.ERROR_MESSAGE)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class HomePage(BasePage):
        """首页"""
        # 元素定位器
        WELCOME_MESSAGE = ("id", "com.example:id/welcome_message")
        USERNAME_DISPLAY = ("id", "com.example:id/username_display")
        LOGOUT_BUTTON = ("id", "com.example:id/logout_button")
        MENU_BUTTON = ("id", "com.example:id/menu_button")
        # ==================== 页面操作 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_logout():
            """点击退出"""
            self.click(self.LOGOUT_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return LoginPage(self.driver)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_menu():
            """点击菜单"""
            self.click(self.MENU_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MenuPage(self.driver)
        # ==================== 验证方法 ====================
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_welcome_text():
            """获取欢迎文本"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_text(self.WELCOME_MESSAGE)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_displayed_username():
            """获取显示的用户名"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_text(self.USERNAME_DISPLAY)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_logged_in():
            """是否已登录"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.is_element_present(self.WELCOME_MESSAGE)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ForgotPasswordPage(BasePage):
        """忘记密码页"""
        EMAIL_INPUT = ("id", "com.example:id/email_input")
        SUBMIT_BUTTON = ("id", "com.example:id/submit_button")
        BACK_BUTTON = ("id", "com.example:id/back_button")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def input_email():
            """输入邮箱"""
            self.send_keys(self.EMAIL_INPUT, email)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_submit():
            """点击提交"""
            self.click(self.SUBMIT_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_back():
            """点击返回"""
            self.click(self.BACK_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return LoginPage(self.driver)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def reset_password():
            """重置密码流程"""
            self.input_email(email)
            self.click_submit()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MenuPage(BasePage):
        """菜单页"""
        PROFILE_OPTION = ("id", "com.example:id/menu_profile")
        SETTINGS_OPTION = ("id", "com.example:id/menu_settings")
        HELP_OPTION = ("id", "com.example:id/menu_help")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_profile():
            """点击个人资料"""
            self.click(self.PROFILE_OPTION)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ProfilePage(self.driver)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_settings():
            """点击设置"""
            self.click(self.SETTINGS_OPTION)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return SettingsPage(self.driver)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ProfilePage(BasePage):
        """个人资料页"""
        pass
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class SettingsPage(BasePage):
        """设置页"""
        pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：POM使用示例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：POM使用示例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_pom():
        """演示POM使用"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("POM使用示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # 模拟driver
        # 【类定义】
        # 语法: class 类名:
        # 作用: 创建对象模板，封装数据和方法
        class MockDriver:
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def implicitly_wait():
                pass
        driver = MockDriver()
        # 1. 传统写法 vs POM写法
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. 传统写法:")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  driver.find_element('id', 'username').send_keys('admin')")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  driver.find_element('id', 'password').send_keys('123')")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  driver.find_element('id', 'login_btn').click()")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. POM写法:")
        login_page = LoginPage(driver)
        login_page.login("admin", "123")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  一行代码完成登录！")
        # 2. 链式调用
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n3. 链式调用:")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  login_page.input_username('admin').input_password('123').click_login()")
        # 3. 页面流转
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n4. 页面流转:")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  home_page = login_page.login('admin', '123')")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  login_page = home_page.click_logout()")
        # 4. 验证方法
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n5. 验证方法:")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  error = login_page.get_error_message()")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  assert '错误' in error")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：POM最佳实践"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：POM最佳实践")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    BEST_PRACTICES = """
    POM最佳实践:
    1. 命名规范
       - 页面类名: XxxPage (如 LoginPage)
       - 元素定位器: 大写下划线 (如 USERNAME_INPUT)
       - 操作方法: 动词开头 (如 click_login)
       - 验证方法: is_xxx 或 get_xxx
    2. 元素定位
       - 集中管理在页面类顶部
       - 使用元组格式: ("id", "value")
       - 避免在测试用例中直接写定位器
    3. 操作方法
       - 每个操作一个方法
       - 返回self支持链式调用
       - 页面跳转返回新页面对象
    4. 错误处理
       - 在页面类中封装等待逻辑
       - 提供元素存在性检查方法
       - 封装常用验证方法
    5. 代码复用
       - 公共方法放在BasePage
       - 使用继承复用页面结构
       - 封装通用业务流程
    6. 测试用例
       - 只包含测试逻辑
       - 不包含元素定位
       - 读起来像自然语言
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(BEST_PRACTICES)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """实战任务：实现POM框架"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：实现POM框架")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为电商应用实现POM框架
    应用功能:
    - 商品列表页
    - 商品详情页
    - 购物车页
    - 结算页
    """
    # 请完成下面的页面类
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ProductListPage(BasePage):
        """
        商品列表页
        需要实现:
        1. 定义元素定位器 (搜索框、商品列表、筛选按钮等)
        2. 实现搜索商品方法
        3. 实现点击商品进入详情页方法
        4. 实现筛选商品方法
        """
        # 元素定位器
        # SEARCH_INPUT = ...
        # PRODUCT_LIST = ...
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def search_product():
            """搜索商品"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_product():
            """点击商品进入详情页"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def filter_by_category():
            """按分类筛选"""
            # 你的代码
            pass
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ProductDetailPage(BasePage):
        """
        商品详情页
        需要实现:
        1. 定义元素定位器 (商品名称、价格、加入购物车按钮等)
        2. 实现获取商品信息方法
        3. 实现加入购物车方法
        4. 实现选择规格方法
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_product_info():
            """获取商品信息"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def add_to_cart():
            """加入购物车"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def select_spec():
            """选择规格"""
            # 你的代码
            pass
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class CartPage(BasePage):
        """
        购物车页
        需要实现:
        1. 定义元素定位器 (商品列表、数量输入框、删除按钮、结算按钮等)
        2. 实现获取购物车商品列表方法
        3. 实现修改商品数量方法
        4. 实现删除商品方法
        5. 实现点击结算方法
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cart_items():
            """获取购物车商品列表"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def update_quantity():
            """修改商品数量"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def remove_item():
            """删除商品"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_checkout():
            """点击结算"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_total_price():
            """获取总价"""
            # 你的代码
            pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """参考答案（完成后对照）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("参考答案（完成后对照）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ProductListPage(BasePage):
        SEARCH_INPUT = ("id", "com.shop:id/search_input")
        SEARCH_BUTTON = ("id", "com.shop:id/search_button")
        PRODUCT_ITEMS = ("id", "com.shop:id/product_item")
        PRODUCT_NAME = ("id", "com.shop:id/product_name")
        FILTER_BUTTON = ("id", "com.shop:id/filter_button")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def search_product():
            self.send_keys(self.SEARCH_INPUT, keyword)
            self.click(self.SEARCH_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_product():
            products = self.find_elements(self.PRODUCT_ITEMS)
            if index < len(products):
                products[index].click()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ProductDetailPage(self.driver)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def filter_by_category():
            self.click(self.FILTER_BUTTON)
            # 选择分类...
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ProductDetailPage(BasePage):
        PRODUCT_NAME = ("id", "com.shop:id/product_name")
        PRODUCT_PRICE = ("id", "com.shop:id/product_price")
        ADD_TO_CART_BUTTON = ("id", "com.shop:id/add_to_cart")
        QUANTITY_INPUT = ("id", "com.shop:id/quantity_input")
        SPEC_OPTIONS = ("id", "com.shop:id/spec_option")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_product_info():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {
                "name": self.get_text(self.PRODUCT_NAME),
                "price": self.get_text(self.PRODUCT_PRICE)
            }
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def select_spec():
            specs = self.find_elements(self.SPEC_OPTIONS)
            for spec in specs:
                if spec.text == spec_name:
                    spec.click()
                    break
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def add_to_cart():
            self.send_keys(self.QUANTITY_INPUT, str(quantity))
            self.click(self.ADD_TO_CART_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class CartPage(BasePage):
        CART_ITEMS = ("id", "com.shop:id/cart_item")
        ITEM_NAME = ("id", "com.shop:id/item_name")
        ITEM_QUANTITY = ("id", "com.shop:id/item_quantity")
        ITEM_PRICE = ("id", "com.shop:id/item_price")
        REMOVE_BUTTON = ("id", "com.shop:id/remove_button")
        CHECKOUT_BUTTON = ("id", "com.shop:id/checkout_button")
        TOTAL_PRICE = ("id", "com.shop:id/total_price")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cart_items():
            items = []
            elements = self.find_elements(self.CART_ITEMS)
            for elem in elements:
                # append() - 列表末尾添加元素
                # 语法: 列表.append(元素)
                # 返回值: None（直接修改原列表）
                items.append({
                    "name": elem.find_element(*self.ITEM_NAME).text,
                    "quantity": elem.find_element(*self.ITEM_QUANTITY).text,
                    "price": elem.find_element(*self.ITEM_PRICE).text
                })
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return items
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def remove_item():
            items = self.find_elements(self.CART_ITEMS)
            for item in items:
                name = item.find_element(*self.ITEM_NAME).text
                if name == product_name:
                    item.find_element(*self.REMOVE_BUTTON).click()
                    break
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click_checkout():
            self.click(self.CHECKOUT_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return CheckoutPage(self.driver)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_total_price():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_text(self.TOTAL_PRICE)
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """今日学习要点总结"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("今日学习要点总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    1. POM概念:
       - 页面对象模式
       - 分离页面操作和测试逻辑
       - 提高代码可维护性
    2. BasePage:
       - 封装通用方法
       - 元素查找、操作、手势
       - 所有页面类继承BasePage
    3. 页面对象:
       - 集中管理元素定位器
       - 封装页面操作方法
       - 返回页面对象支持链式调用
       - 提供验证方法
    4. 最佳实践:
       - 命名规范
       - 元素定位集中管理
       - 支持链式调用
       - 页面流转返回新页面对象
    验证标准：能用POM重构之前的测试代码
    """
    # 运行演示
    if __name__ == "__main__":
        demo_pom()

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def practice_task():
    """实战任务"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请修改代码完成任务...")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def show_answer():
    """显示参考答案"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("参考答案")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请参考原文件中的答案部分")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def show_summary():
    """显示学习总结"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("学习总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请参考原文件中的总结部分")

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def main():
    """主菜单"""
    while True:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("Day {day_num}: 学习菜单")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("1. 第一部分：POM简介")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：基础页面类 (BasePage)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：具体页面对象")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：POM使用示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：POM最佳实践")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务：实现POM框架")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 今日学习要点总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 实战任务")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 参考答案")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 学习总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("0. 退出")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        
        choice = input("\n请选择 (0-9): ").strip()
        
        if choice == "1":
            section1()
        if choice == "2":
            section2()
        if choice == "3":
            section3()
        if choice == "4":
            section4()
        if choice == "5":
            section5()
        if choice == "6":
            section6()
        if choice == "7":
            section7()
        if choice == "8":
            section8()
        elif choice == "9":
            practice_task()
        elif choice == "8":
            show_answer()
        elif choice == "7":
            show_summary()
        elif choice == "0":
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n感谢学习！再见！")
            break
        else:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n无效选择，请重新输入")
        
        # input() - 获取用户输入
        # 语法: input(提示信息)
        # 返回值: 用户输入的字符串
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
