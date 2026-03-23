# -*- coding: utf-8 -*-
"""
Day 16: Day 16
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：测试数据管理"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：测试数据管理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestDataManager:
        """
        测试数据管理器
        支持JSON、YAML、CSV格式的测试数据
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.data_dir = Path(data_dir)
            self.data_dir.mkdir(exist_ok=True)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def load_json():
            """加载JSON测试数据"""
            file_path = self.data_dir / filename
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, "r", encoding="utf-8") as f:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return json.load(f)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def save_json():
            """保存JSON测试数据"""
            file_path = self.data_dir / filename
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_test_cases():
            """
            获取测试用例数据
            参数:
                filename: 数据文件名
                filter_func: 过滤函数
            """
            data = self.load_json(filename)
            test_cases = data.get("test_cases", [])
            if filter_func:
                test_cases = [tc for tc in test_cases if filter_func(tc)]
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return test_cases
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_test_data_by_name():
            """根据名称获取测试数据"""
            test_cases = self.load_json(filename).get("test_cases", [])
            for case in test_cases:
                if case.get("name") == case_name:
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return case
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return None
    # 测试数据示例
    TEST_DATA_EXAMPLE = {
        "test_cases": [
            {
                "name": "正常登录",
                "username": "admin",
                "password": "123456",
                "expected": "success",
                "description": "使用正确的用户名密码登录"
            },
            {
                "name": "错误密码",
                "username": "admin",
                "password": "wrong",
                "expected": "fail",
                "expected_message": "密码错误",
                "description": "使用错误的密码登录"
            },
            {
                "name": "空用户名",
                "username": "",
                "password": "123456",
                "expected": "fail",
                "expected_message": "用户名不能为空",
                "description": "用户名为空"
            },
            {
                "name": "不存在用户",
                "username": "notexist",
                "password": "123456",
                "expected": "fail",
                "expected_message": "用户不存在",
                "description": "用户不存在"
            }
        ]
    }


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：断言封装"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：断言封装")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class AssertHelper:
        """
        断言辅助类
        封装常用断言，提供友好的错误信息
        """
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_true():
            """断言为真"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert condition, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_false():
            """断言为假"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert not condition, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_equal():
            """断言相等"""
            if message is None:
                message = f"期望值: {expected}, 实际值: {actual}"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert actual == expected, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_not_equal():
            """断言不相等"""
            if message is None:
                message = f"期望不等于: {expected}, 实际值: {actual}"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert actual != expected, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_in():
            """断言包含"""
            if message is None:
                message = f"期望包含: {member}, 实际: {container}"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert member in container, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_not_in():
            """断言不包含"""
            if message is None:
                message = f"期望不包含: {member}, 实际: {container}"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert member not in container, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_is_none():
            """断言为None"""
            if message is None:
                message = f"期望为None, 实际: {value}"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert value is None, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_is_not_none():
            """断言不为None"""
            if message is None:
                message = "期望不为None"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert value is not None, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_text_contains():
            """断言文本包含子串"""
            if message is None:
                message = f"期望文本包含: '{expected_substring}', 实际: '{actual_text}'"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert expected_substring in actual_text, message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_element_displayed():
            """断言元素显示"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert element.is_displayed(), message
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_element_enabled():
            """断言元素可用"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert element.is_enabled(), message


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：页面对象实现"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：页面对象实现")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class BasePage:
        """基础页面类"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.driver = driver
            self.assert_helper = AssertHelper()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_element():
            """查找元素"""
            by, value = locator
            # 实际: return self.driver.find_element(by, value)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            """点击"""
            element = self.find_element(locator)
            element.click()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            """输入"""
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_text():
            """获取文本"""
            element = self.find_element(locator)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return element.text
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class LoginPage(BasePage):
        """登录页面"""
        # 元素定位器
        USERNAME_INPUT = ("id", "com.example:id/username")
        PASSWORD_INPUT = ("id", "com.example:id/password")
        LOGIN_BUTTON = ("id", "com.example:id/login_button")
        ERROR_MESSAGE = ("id", "com.example:id/error_message")
        SUCCESS_MESSAGE = ("id", "com.example:id/success_message")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def input_username():
            """输入用户名"""
            self.send_keys(self.USERNAME_INPUT, username)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
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
            """点击登录"""
            self.click(self.LOGIN_BUTTON)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login():
            """完整登录流程"""
            self.input_username(username)
            self.input_password(password)
            self.click_login()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_error_message():
            """获取错误信息"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_text(self.ERROR_MESSAGE)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_success_message():
            """获取成功信息"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get_text(self.SUCCESS_MESSAGE)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_login_successful():
            """判断是否登录成功"""
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                success_msg = self.get_success_message()
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return "成功" in success_msg or "welcome" in success_msg.lower()
            except:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return False
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class HomePage(BasePage):
        """首页"""
        WELCOME_MESSAGE = ("id", "com.example:id/welcome_message")
        LOGOUT_BUTTON = ("id", "com.example:id/logout_button")
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
        def is_at_home_page():
            """是否在首页"""
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                welcome = self.get_welcome_text()
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return len(welcome) > 0
            except:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return False
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockElement:
        """模拟元素"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.by = by
            self.value = value
            self._text = ""
            self._displayed = True
            self._enabled = True
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
            self._text = ""
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
        def is_displayed():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._displayed
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_enabled():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._enabled


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：测试用例实现"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：测试用例实现")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestLogin:
        """
        登录测试类
        使用pytest框架
        """
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login_page():
            """登录页面对象"""
            # 实际: driver = DriverFactory.get_driver()
            driver = MockDriver()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return LoginPage(driver)
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_data_manager():
            """测试数据管理器"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return TestDataManager()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_success():
            """测试正常登录"""
            # 执行登录
            login_page.login("admin", "123456")
            # 验证结果
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert login_page.is_login_successful(), "登录应该成功"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_wrong_password():
            """测试错误密码"""
            login_page.login("admin", "wrong")
            error_msg = login_page.get_error_message()
            AssertHelper.assert_text_contains(error_msg, "密码")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_empty_username():
            """测试空用户名"""
            login_page.login("", "123456")
            error_msg = login_page.get_error_message()
            AssertHelper.assert_in("用户名", error_msg)
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("username,password,expected_error", [
            ("admin", "wrong", "密码"),
            ("", "123456", "用户名"),
            ("notexist", "123456", "不存在"),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_various_failures():
            """参数化测试各种失败场景"""
            login_page.login(username, password)
            error_msg = login_page.get_error_message()
            AssertHelper.assert_in(expected_error, error_msg)
    # 模拟Driver
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockDriver:
        pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：conftest.py配置"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：conftest.py配置")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    CONFTEST_CONTENT = '''
    # conftest.py
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import pytest
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from datetime import datetime
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from pathlib import Path
    # 全局fixture
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(scope="session")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def config_reader():
        """配置读取器"""
        # from...import - 从模块导入特定内容
        # 作用: 只导入需要的函数/类，不用写模块名前缀
        from utils.config_reader import ConfigReader
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return ConfigReader()
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(scope="session")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def driver():
        """WebDriver实例"""
        # from...import - 从模块导入特定内容
        # 作用: 只导入需要的函数/类，不用写模块名前缀
        from utils.driver_factory import DriverFactory
        driver = DriverFactory.get_driver()
        yield driver
        DriverFactory.quit_driver()
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_data_manager():
        """测试数据管理器"""
        # from...import - 从模块导入特定内容
        # 作用: 只导入需要的函数/类，不用写模块名前缀
        from utils.test_data_manager import TestDataManager
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return TestDataManager()
    # 钩子函数
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_runtest_makereport():
        """测试报告钩子"""
        outcome = yield
        rep = outcome.get_result()
        # 失败时截图
        if rep.when == "call" and rep.failed:
            driver = item.funcargs.get("driver")
            if driver:
                screenshot_dir = Path("screenshots")
                screenshot_dir.mkdir(exist_ok=True)
                filename = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                driver.get_screenshot_as_file(str(screenshot_dir / filename))
    # 命令行选项
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_addoption():
        parser.addoption(
            "--env", default="test", help="测试环境: dev/test/prod"
        )
        parser.addoption(
            "--platform", default="android", help="平台: android/ios"
        )
    '''
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("conftest.py示例:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(CONFTEST_CONTENT)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """实战任务：完成登录测试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：完成登录测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：完成完整的登录测试用例
    要求:
    1. 使用数据驱动测试
    2. 使用断言封装
    3. 失败时自动截图
    4. 生成测试报告
    """
    # 请完成下面的测试用例
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MyTestLogin:
        """
        完整的登录测试类
        要求:
        1. 从JSON文件读取测试数据
        2. 使用参数化运行所有测试用例
        3. 使用AssertHelper进行断言
        4. 添加详细的测试步骤日志
        """
        # 你的代码写在这里
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
    class MyTestLogin:
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login_page():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return LoginPage(driver)
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_data():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return test_data_manager.load_json("login_test_data.json")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_from_data():
            for case in test_data["test_cases"]:
                username = case["username"]
                password = case["password"]
                expected = case["expected"]
                login_page.login(username, password)
                if expected == "success":
                    AssertHelper.assert_true(
                        login_page.is_login_successful(),
                        f"{case['name']}: 登录应该成功"
                    )
                else:
                    error_msg = login_page.get_error_message()
                    AssertHelper.assert_in(
                        # get() - 安全获取字典值
                        # 语法: 字典.get(键, 默认值)
                        # 作用: 获取键对应的值，不存在返回默认值（不会报错）
                        case.get("expected_message", ""),
                        error_msg,
                        f"{case['name']}: 错误信息不匹配"
                    )
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("case", [
            {"username": "admin", "password": "123456", "expected": "success"},
            {"username": "admin", "password": "wrong", "expected": "fail"},
            {"username": "", "password": "123456", "expected": "fail"},
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_parametrized():
            login_page.login(case["username"], case["password"])
            if case["expected"] == "success":
                AssertHelper.assert_true(login_page.is_login_successful())
            else:
                error_msg = login_page.get_error_message()
                AssertHelper.assert_is_not_none(error_msg)
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
    1. 测试数据管理:
       - 分离测试数据和代码
       - 支持JSON/YAML/CSV
       - 数据驱动测试
    2. 断言封装:
       - 统一断言接口
       - 友好的错误信息
       - 支持元素断言
    3. 页面对象:
       - 完整封装页面操作
       - 返回页面对象支持链式调用
       - 提供验证方法
    4. 测试用例:
       - 使用pytest fixture
       - 参数化测试
       - 失败自动截图
    5. conftest.py:
       - 共享fixture
       - 钩子函数
       - 命令行选项
    验证标准：能跑通一个完整的登录测试用例
    """

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
        print("1. 第一部分：测试数据管理")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：断言封装")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：页面对象实现")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：测试用例实现")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：conftest.py配置")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务：完成登录测试")
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
