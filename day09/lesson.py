# -*- coding: utf-8 -*-
"""
Day 9: Day 9
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：Setup和Teardown"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：Setup和Teardown")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Pytest提供多种setup/teardown方式:
    1. 函数级别: setup_method/teardown_method
    2. 类级别: setup_class/teardown_class
    3. 模块级别: setup_module/teardown_module
    """
    # 模块级别
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def setup_module():
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[Module] 模块开始")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def teardown_module():
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Module] 模块结束")
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestWithSetup:
        """演示setup/teardown"""
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def setup_class():
            """类级别：整个类开始前执行一次"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Class] 测试类开始")
            cls.shared_resource = "共享资源"
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def teardown_class():
            """类级别：整个类结束后执行一次"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Class] 测试类结束")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def setup_method():
            """方法级别：每个测试方法前执行"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Method] 测试方法开始")
            self.test_data = "测试数据"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def teardown_method():
            """方法级别：每个测试方法后执行"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Method] 测试方法结束")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_one():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  执行test_one: {self.test_data}, {self.shared_resource}")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert True
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_two():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  执行test_two: {self.test_data}, {self.shared_resource}")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert True


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：Fixture基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：Fixture基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Fixture是Pytest最强大的特性，用于:
    - 准备测试数据
    - 初始化测试环境
    - 清理测试资源
    """
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def sample_data():
        """简单的fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[Fixture] 创建sample_data")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return {"name": "test", "value": 123}
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_using_fixture():
        """使用fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  使用fixture: {sample_data}")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert sample_data["name"] == "test"
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert sample_data["value"] == 123
    # Fixture可以返回任意类型
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def database_connection():
        """模拟数据库连接"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[Fixture] 连接数据库")
        conn = {"status": "connected", "id": 1}
        yield conn  # yield之前的代码是setup，之后的是teardown
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Fixture] 关闭数据库连接")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_query():
        """使用数据库连接"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  使用连接: {database_connection}")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert database_connection["status"] == "connected"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：Fixture作用域"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：Fixture作用域")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Fixture作用域 (scope参数):
    - function: 每个测试函数 (默认)
    - class: 每个测试类
    - module: 每个模块
    - package: 每个包
    - session: 整个测试会话
    """
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(scope="function")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def func_scope():
        """函数级别"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[Function Scope] 创建")
        yield "function"
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Function Scope] 销毁")
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(scope="class")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def class_scope():
        """类级别"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[Class Scope] 创建")
        yield "class"
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Class Scope] 销毁")
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(scope="module")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def module_scope():
        """模块级别"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[Module Scope] 创建")
        yield "module"
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Module Scope] 销毁")
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestScopes:
        """测试不同作用域"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_1():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  test_1: {func_scope}, {class_scope}, {module_scope}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_2():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  test_2: {func_scope}, {class_scope}, {module_scope}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：Fixture参数化"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：Fixture参数化")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(params=["chrome", "firefox", "safari"])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def browser():
        """参数化fixture"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return request.param
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_browser_support():
        """每个参数都会运行一次"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n  测试浏览器: {browser}")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert browser in ["chrome", "firefox", "safari"]
    # 多个参数组合
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(params=[
        ("admin", "123456"),
        ("user", "password"),
        ("guest", "guest"),
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def credentials():
        """多组登录凭证"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return request.param
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_login_with_credentials():
        """每组凭证都会运行一次"""
        username, password = credentials
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n  测试登录: {username}/{password}")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert len(username) > 0
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert len(password) > 0


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：Fixture依赖"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：Fixture依赖")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def first():
        """第一个fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n[First] 执行")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "first"
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def second():
        """依赖first的fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Second] 执行")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return f"second({first})"
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def third():
        """依赖second的fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Third] 执行")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return f"third({second})"
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_fixture_chain():
        """测试fixture链"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  结果: {third}")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "first" in third
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "second" in third
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "third" in third


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：使用conftest.py"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：使用conftest.py")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    conftest.py用于存放共享的fixture:
    1. 同一目录下的测试文件共享
    2. 子目录继承父目录的conftest.py
    3. 可以有多层conftest.py
    目录结构示例:
    project/
    ├── conftest.py          # 全局fixture
    ├── test_module1.py
    └── subpackage/
        ├── conftest.py      # 子包fixture
        └── test_module2.py
    """
    # 在当前目录创建conftest.py文件
    conftest_content = '''
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import pytest
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture(scope="session")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def global_config():
        """全局配置fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\\n[Global] 加载全局配置")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return {
            "env": "test",
            "base_url": "http://localhost:8080"
        }
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def api_client():
        """API客户端"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\\n[API Client] 创建")
        client = {"base_url": global_config["base_url"], "headers": {}}
        yield client
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[API Client] 销毁")
    '''
    # 创建conftest.py
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open("conftest.py", "w", encoding="utf-8") as f:
        f.write(conftest_content)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n已创建conftest.py")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_use_conftest_fixture():
        """使用conftest.py中的fixture"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n  全局配置: {global_config}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  API客户端: {api_client}")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert global_config["env"] == "test"
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "base_url" in api_client


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """第七部分：内置Fixture"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第七部分：内置Fixture")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_builtin_fixtures():
        """使用内置fixture"""
        # tmp_path: 临时目录
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n  临时目录: {tmp_path}")
        temp_file = tmp_path / "test.txt"
        temp_file.write_text("hello")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert temp_file.read_text() == "hello"
        # capsys: 捕获输出
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("被捕获的输出")
        captured = capsys.readouterr()
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "被捕获的输出" in captured.out
        # monkeypatch: 临时修改
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import os
        monkeypatch.setenv("TEST_VAR", "test_value")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert os.getenv("TEST_VAR") == "test_value"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """实战任务：编写带Fixture的测试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：编写带Fixture的测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为下面的API类编写测试，使用fixture
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class SimpleAPI:
        """简单API类"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.base_url = base_url
            self.token = None
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login():
            """登录获取token"""
            if username == "admin" and password == "123":
                self.token = "fake_token_123"
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": True, "token": self.token}
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"success": False, "error": "认证失败"}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_user():
            """获取用户信息"""
            if not self.token:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"error": "未登录"}
            if user_id == 1:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"id": 1, "name": "Alice"}
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"error": "用户不存在"}
    # 请在这里编写fixture和测试用例
    # 提示：
    # 1. 创建api fixture，初始化SimpleAPI
    # 2. 创建authenticated_api fixture，返回已登录的API实例
    # 3. 编写测试用例测试各种场景


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section9():
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
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def api():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return SimpleAPI("http://localhost:8080")
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def authenticated_api():
        api.login("admin", "123")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return api
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestSimpleAPI:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_success():
            result = api.login("admin", "123")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is True
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "token" in result
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_failure():
            result = api.login("admin", "wrong")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is False
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_user_without_auth():
            result = api.get_user(1)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "error" in result
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_user_with_auth():
            result = authenticated_api.get_user(1)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["id"] == 1
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["name"] == "Alice"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_nonexistent_user():
            result = authenticated_api.get_user(999)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "error" in result
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section10():
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
    1. Setup/Teardown:
       - setup_method/teardown_method (方法级别)
       - setup_class/teardown_class (类级别)
       - setup_module/teardown_module (模块级别)
    2. Fixture:
       - @pytest.fixture装饰器
       - yield实现setup和teardown
       - scope参数控制作用域
    3. Fixture高级:
       - params参数化
       - fixture可以相互依赖
       - conftest.py共享fixture
    4. 内置Fixture:
       - tmp_path: 临时目录
       - capsys: 捕获输出
       - monkeypatch: 临时修改
    验证标准：能写出带fixture的测试用例
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section11():
    """第十一部分：conftest.py深入使用（补充）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第十一部分：conftest.py深入使用（补充）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # ---- 1. conftest.py是什么 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. conftest.py核心概念:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    conftest.py 是 Pytest 的特殊文件:
    - 不需要 import，Pytest 自动加载
    - 可以定义 fixture 供同目录及子目录的测试文件使用
    - 可以存在多个，每个目录都可以有自己的 conftest.py
    - 用于共享测试配置、fixture、hook函数

    项目结构示例:
    project/
    ├── conftest.py          # 根级 - 全局fixture (如driver初始化)
    ├── tests/
    │   ├── conftest.py      # tests级 - 通用测试fixture
    │   ├── test_login/
    │   │   ├── conftest.py  # 模块级 - 登录相关fixture
    │   │   └── test_login.py
    │   └── test_home/
    │       ├── conftest.py  # 模块级 - 首页相关fixture
    │       └── test_home.py
    """)

    # ---- 2. 多层级conftest示例 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. 多层级conftest共享fixture:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    # ===== 根目录 conftest.py =====
    import pytest

    @pytest.fixture(scope='session')
    def app_config():
        '''整个测试会话共享的配置'''
        return {
            'base_url': 'http://api.example.com',
            'timeout': 30,
            'platform': 'Android'
        }

    @pytest.fixture(scope='session')
    def driver(app_config):
        '''整个测试会话共享的driver'''
        # 初始化Appium driver
        print(f"初始化driver, 平台: {app_config['platform']}")
        driver = "模拟的driver对象"
        yield driver
        # teardown: 关闭driver
        print("关闭driver")

    # ===== tests/conftest.py =====
    import pytest

    @pytest.fixture(autouse=True)
    def log_test_info(request):
        '''自动记录每个测试的开始和结束'''
        print(f"\\n>>> 开始测试: {request.node.name}")
        yield
        print(f"<<< 结束测试: {request.node.name}")

    @pytest.fixture
    def test_data():
        '''通用测试数据'''
        return {'username': 'test_user', 'password': '123456'}

    # ===== tests/test_login/conftest.py =====
    import pytest

    @pytest.fixture
    def login_page(driver):
        '''登录页面对象 - 仅登录测试模块可用'''
        print("进入登录页面")
        return "LoginPage对象"
    """)

    # ---- 3. conftest.py中的Hook函数 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("3. conftest.py中的Hook函数:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    # 在conftest.py中定义hook，自定义Pytest行为:

    # Hook 1: 测试失败时自动截图
    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        report = outcome.get_result()
        if report.when == 'call' and report.failed:
            # 获取driver fixture
            driver = item.funcargs.get('driver')
            if driver:
                # 截图保存
                screenshot_path = f'screenshots/{item.name}.png'
                driver.save_screenshot(screenshot_path)
                print(f"截图已保存: {screenshot_path}")

    # Hook 2: 自定义命令行参数
    def pytest_addoption(parser):
        parser.addoption(
            '--env',
            default='test',
            help='运行环境: test/staging/prod'
        )
        parser.addoption(
            '--platform',
            default='Android',
            help='测试平台: Android/iOS'
        )

    # 将命令行参数转为fixture
    @pytest.fixture(scope='session')
    def env(request):
        return request.config.getoption('--env')

    # 使用: pytest --env=staging --platform=iOS
    """)

    # ---- 4. fixture的参数化与组合 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. fixture的参数化与组合:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    # fixture参数化 - 一个fixture产生多组数据
    @pytest.fixture(params=[
        {'username': 'admin', 'password': 'admin123'},
        {'username': 'user1', 'password': 'pass123'},
        {'username': 'guest', 'password': 'guest'},
    ], ids=['管理员账号', '普通用户', '访客账号'])
    def user_credentials(request):
        '''参数化的用户凭证'''
        return request.param

    # 测试函数会运行3次，每次使用不同的凭证
    def test_login(user_credentials):
        print(f"测试登录: {user_credentials['username']}")

    # fixture组合 - 多个fixture协作
    @pytest.fixture
    def logged_in_user(driver, test_data):
        '''组合driver和test_data，返回已登录状态'''
        # 使用test_data登录
        print(f"登录用户: {test_data['username']}")
        return {'driver': driver, 'user': test_data['username']}

    # 使用组合fixture
    def test_user_profile(logged_in_user):
        print(f"测试用户主页: {logged_in_user['user']}")
    """)

    # ---- 5. 最佳实践 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("5. conftest.py最佳实践:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    ✓ 根目录conftest.py: 放全局fixture (driver, config, logging)
    ✓ 模块目录conftest.py: 放模块专属fixture (page对象)
    ✓ 使用scope控制fixture生命周期 (session > module > class > function)
    ✓ autouse=True 只用于确实需要全局生效的fixture
    ✓ 给fixture加清晰的docstring
    ✗ 不要在conftest.py中写测试函数
    ✗ 不要在conftest.py中import测试文件
    ✗ 不要把所有fixture都堆在根conftest.py中
    """)

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
        print("1. 第一部分：Setup和Teardown")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：Fixture基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：Fixture作用域")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：Fixture参数化")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：Fixture依赖")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：使用conftest.py")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 第七部分：内置Fixture")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 实战任务：编写带Fixture的测试")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("10. 今日学习要点总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("11. 补充：conftest.py深入使用")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("12. 实战任务")
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
        if choice == "9":
            section9()
        if choice == "10":
            section10()
        if choice == "11":
            section11()
        elif choice == "12":
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
