# -*- coding: utf-8 -*-
"""
Day 11: Day 11
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：常用插件介绍"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：常用插件介绍")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    常用Pytest插件:
    1. pytest-html: 生成HTML报告
       pip install pytest-html
       pytest --html=report.html
    2. pytest-cov: 代码覆盖率
       pip install pytest-cov
       pytest --cov=src --cov-report=html
    3. pytest-xdist: 并行执行
       pip install pytest-xdist
       pytest -n auto  # 自动检测CPU核心数
    4. pytest-ordering: 控制测试顺序
       pip install pytest-ordering
       # 【装饰器 @pytest】
       # 作用: 在不修改原函数的情况下，添加额外功能
       # 原理: 接收函数作为参数，返回新函数
       @pytest.mark.run(order=1)
    5. pytest-rerunfailures: 失败重试
       pip install pytest-rerunfailures
       pytest --reruns 3 --reruns-delay 1
    6. pytest-assume: 软断言
       pip install pytest-assume
       pytest.assume(x == 1)
    7. allure-pytest: 生成Allure报告
       pip install allure-pytest
       pytest --alluredir=./allure-results
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：测试顺序控制"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：测试顺序控制")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 使用pytest-ordering插件控制顺序
    # 安装: pip install pytest-ordering
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import pytest_ordering
        HAS_ORDERING = True
    except ImportError:
        HAS_ORDERING = False
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("提示: 安装pytest-ordering可使用顺序控制: pip install pytest-ordering")
    if HAS_ORDERING:
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.run(order=1)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_first():
            """第一个执行"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n  第一个测试")
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.run(order=3)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_last():
            """最后执行"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n  最后一个测试")
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.run(order=2)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_middle():
            """中间执行"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n  中间测试")
    # 使用依赖关系 (pytest-dependency)
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import pytest_dependency
        HAS_DEPENDENCY = True
    except ImportError:
        HAS_DEPENDENCY = False
    if HAS_DEPENDENCY:
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.dependency()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login():
            """登录测试"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert True
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.dependency(depends=["test_login"])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_access_resource():
            """访问资源 - 依赖登录"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert True


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：软断言"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：软断言")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import pytest_assume
        HAS_ASSUME = True
    except ImportError:
        HAS_ASSUME = False
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("提示: 安装pytest-assume可使用软断言: pip install pytest-assume")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_hard_assert():
        """硬断言 - 失败立即停止"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 1 == 1
        # assert 1 == 2  # 如果取消注释，后面的代码不会执行
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 2 == 2
    if HAS_ASSUME:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_soft_assert():
            """软断言 - 失败继续执行"""
            pytest.assume(1 == 1)
            pytest.assume(1 == 2, "这个会失败但继续执行")
            pytest.assume(2 == 2)
            # 最后汇总所有失败


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：失败重试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：失败重试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 使用pytest-rerunfailures
    # 安装: pip install pytest-rerunfailures
    # 运行: pytest --reruns 3 --reruns-delay 1
    flaky_counter = 0
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_flaky():
        """不稳定的测试 - 可能失败"""
        global flaky_counter
        flaky_counter += 1
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n  第{flaky_counter}次尝试")
        # 前2次失败，第3次成功
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert flaky_counter >= 3


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：测试钩子函数 (Hooks)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：测试钩子函数 (Hooks)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    钩子函数在conftest.py中定义，用于自定义测试行为
    这里列出常用钩子供参考
    """
    # 这些钩子需要在conftest.py中定义
    hooks_demo = '''
    # conftest.py
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import pytest
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_configure():
        """配置钩子：测试会话开始前调用"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\\n[Hook] 测试会话开始配置")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_sessionstart():
        """会话开始钩子"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Hook] 测试会话开始")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_sessionfinish():
        """会话结束钩子"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("[Hook] 测试会话结束")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_collection_modifyitems():
        """修改收集到的测试项"""
        # 可以在这里修改测试顺序或添加标记
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"[Hook] 收集到 {len(items)} 个测试")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_runtest_setup():
        """每个测试前的setup钩子"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"[Hook] 准备执行: {item.name}")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_runtest_teardown():
        """每个测试后的teardown钩子"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"[Hook] 执行完毕: {item.name}")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_runtest_makereport():
        """生成测试报告钩子"""
        if call.when == "call":
            if call.excinfo is not None:
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"[Hook] 测试失败: {item.name}")
            else:
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"[Hook] 测试通过: {item.name}")
    '''
    # 保存到文件供参考
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open("hooks_demo.py", "w", encoding="utf-8") as f:
        f.write(hooks_demo)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n钩子函数示例已保存到 hooks_demo.py")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：自定义插件"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：自定义插件")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    创建自定义pytest插件:
    1. 创建conftest.py或独立包
    2. 定义fixture和钩子
    3. 注册到pytest
    """
    custom_plugin = '''
    # myplugin.py - 自定义插件示例
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import pytest
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestDataPlugin:
        """测试数据插件"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.config = config
            self.test_data = {}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def pytest_configure():
            """配置时加载测试数据"""
            self.test_data = {
                "users": ["admin", "user", "guest"],
                "environments": ["dev", "test", "prod"]
            }
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def pytest_generate_tests():
            """动态生成测试"""
            if "test_user" in metafunc.fixturenames:
                metafunc.parametrize("test_user", self.test_data.get("users", []))
    # 注册插件
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_configure():
        config.pluginmanager.register(TestDataPlugin(config), "test_data_plugin")
    '''
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open("custom_plugin_demo.py", "w", encoding="utf-8") as f:
        f.write(custom_plugin)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("自定义插件示例已保存到 custom_plugin_demo.py")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """第七部分：测试报告"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第七部分：测试报告")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    生成测试报告的方式:
    1. 终端报告 (默认)
       pytest -v
    2. HTML报告
       pip install pytest-html
       pytest --html=report.html --self-contained-html
    3. JUnit XML报告
       pytest --junitxml=report.xml
    4. Allure报告 (推荐)
       pip install allure-pytest
       pytest --alluredir=./allure-results
       allure serve ./allure-results
    5. 覆盖率报告
       pip install pytest-cov
       pytest --cov=src --cov-report=html
    """
    # Allure标记示例
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import allure
        HAS_ALLURE = True
    except ImportError:
        HAS_ALLURE = False
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("提示: 安装allure-pytest可生成精美报告: pip install allure-pytest")
    if HAS_ALLURE:
        # 【装饰器 @allure】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @allure.feature("用户管理")
        # 【装饰器 @allure】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @allure.story("用户登录")
        # 【装饰器 @allure】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @allure.severity(allure.severity_level.CRITICAL)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_allure_login():
            """Allure报告示例"""
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with allure.step("输入用户名"):
                username = "admin"
                allure.attach(username, "用户名")
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with allure.step("输入密码"):
                password = "123456"
                allure.attach(password, "密码")
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with allure.step("点击登录"):
                result = "登录成功"
                allure.attach(result, "结果")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result == "登录成功"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """第八部分：命令行选项"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第八部分：命令行选项")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_addoption():
        """添加自定义命令行选项"""
        parser.addoption(
            "--env",
            action="store",
            default="test",
            help="测试环境: dev/test/prod"
        )
        parser.addoption(
            "--browser",
            action="store",
            default="chrome",
            help="浏览器: chrome/firefox/safari"
        )
    # 在conftest.py中定义后，可以这样使用:
    # pytest --env=prod --browser=firefox
    # 在测试中获取选项
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def env():
        """获取环境配置"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return request.config.getoption("--env")
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def browser():
        """获取浏览器配置"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return request.config.getoption("--browser")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section9():
    """实战任务：创建测试套件"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：创建测试套件")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为下面的ECommerce类创建完整的测试套件，包括:
    1. 使用参数化测试各种场景
    2. 添加适当的标记
    3. 使用fixture准备测试数据
    4. 考虑使用软断言
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ECommerce:
        """电商系统"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.products = {
                1: {"name": "iPhone", "price": 999, "stock": 10},
                2: {"name": "iPad", "price": 799, "stock": 5},
            }
            self.cart = {}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_product():
            """获取商品信息"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.products.get(product_id)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def add_to_cart():
            """添加商品到购物车"""
            product = self.get_product(product_id)
            if not product:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "error": "商品不存在"}
            if product["stock"] < quantity:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "error": "库存不足"}
            if quantity <= 0:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "error": "数量必须大于0"}
            if product_id in self.cart:
                self.cart[product_id] += quantity
            else:
                self.cart[product_id] = quantity
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"success": True, "message": "已添加到购物车"}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cart_total():
            """获取购物车总价"""
            total = 0
            for product_id, quantity in self.cart.items():
                product = self.get_product(product_id)
                if product:
                    total += product["price"] * quantity
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return total
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def checkout():
            """结算"""
            if not self.cart:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "error": "购物车为空"}
            # 扣减库存
            for product_id, quantity in self.cart.items():
                self.products[product_id]["stock"] -= quantity
            total = self.get_cart_total()
            self.cart.clear()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"success": True, "total": total, "message": "结算成功"}
    # 请在这里编写测试套件


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section10():
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
    def ecommerce():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return ECommerce()
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.fixture
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def ecommerce_with_items():
        ecommerce.add_to_cart(1, 2)  # iPhone x 2
        ecommerce.add_to_cart(2, 1)  # iPad x 1
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return ecommerce
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.smoke
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestECommerce:
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("product_id,expected_name", [
            (1, "iPhone"),
            (2, "iPad"),
            (999, None),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_product():
            product = ecommerce.get_product(product_id)
            if expected_name:
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert product["name"] == expected_name
            else:
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert product is None
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("product_id,quantity,expected_success", [
            (1, 1, True),
            (1, 10, True),
            (1, 11, False),  # 库存不足
            (1, 0, False),   # 数量无效
            (999, 1, False), # 商品不存在
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_add_to_cart():
            result = ecommerce.add_to_cart(product_id, quantity)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] == expected_success
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_cart_total():
            # iPhone x 2 = 1998, iPad x 1 = 799, 总计 = 2797
            total = ecommerce_with_items.get_cart_total()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert total == 2797
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_checkout_empty_cart():
            result = ecommerce.checkout()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is False
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "购物车为空" in result["error"]
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_checkout_success():
            result = ecommerce_with_items.checkout()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is True
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["total"] == 2797
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert len(ecommerce_with_items.cart) == 0
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section11():
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
    1. 常用插件:
       - pytest-html: HTML报告
       - pytest-cov: 代码覆盖率
       - pytest-xdist: 并行执行
       - pytest-rerunfailures: 失败重试
       - allure-pytest: Allure报告
    2. 测试控制:
       - pytest-ordering: 测试顺序
       - pytest-dependency: 测试依赖
       - pytest-assume: 软断言
    3. 钩子函数:
       - pytest_configure: 配置
       - pytest_sessionstart/finish: 会话开始/结束
       - pytest_collection_modifyitems: 修改测试项
       - pytest_runtest_setup/teardown: 测试前后
       - pytest_runtest_makereport: 生成报告
    4. 自定义选项:
       - pytest_addoption: 添加命令行选项
       - request.config.getoption: 获取选项
    验证标准：能使用插件生成测试报告
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section12():
    """第十二部分：Allure报告详解（补充）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第十二部分：Allure报告详解（补充）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # ---- 1. Allure安装与基本使用 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. Allure安装与基本使用:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    安装:
    pip install allure-pytest

    # 还需安装Allure命令行工具:
    # Windows: scoop install allure (或下载zip解压配置环境变量)
    # Mac: brew install allure

    运行测试并生成报告数据:
    pytest --alluredir=./allure-results

    生成HTML报告并打开:
    allure serve ./allure-results

    生成静态HTML报告:
    allure generate ./allure-results -o ./allure-report --clean
    """)

    # ---- 2. Allure装饰器详解 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. Allure常用装饰器:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import allure

    # @allure.feature - 功能模块 (一级分类)
    # @allure.story  - 用户故事 (二级分类)
    # @allure.title  - 测试用例标题
    # @allure.step   - 测试步骤
    # @allure.severity - 严重程度

    @allure.feature('用户管理')           # 功能模块
    @allure.story('用户登录')             # 用户故事
    @allure.title('测试正常登录流程')      # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 严重程度
    def test_login():
        with allure.step('步骤1: 打开登录页'):
            print('打开登录页')

        with allure.step('步骤2: 输入用户名和密码'):
            username = 'admin'
            password = '123456'
            print(f'输入: {username}/{password}')

        with allure.step('步骤3: 点击登录按钮'):
            print('点击登录')

        with allure.step('步骤4: 验证登录成功'):
            assert True, '登录成功'
    """)

    # ---- 3. 严重程度级别 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("3. 严重程度级别 (severity):")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    allure.severity_level.BLOCKER  - 阻塞: 功能完全不可用
    allure.severity_level.CRITICAL - 严重: 核心功能受影响
    allure.severity_level.NORMAL   - 普通: 一般功能问题 (默认)
    allure.severity_level.MINOR    - 次要: 不影响主要功能
    allure.severity_level.TRIVIAL  - 轻微: UI或文案问题

    # 可以在命令行按严重程度过滤运行:
    # pytest --allure-severities=critical,blocker
    """)

    # ---- 4. 添加附件（截图/日志） ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. 添加附件 (截图/日志):")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import allure

    # 方式1: 添加截图 (Appium/Selenium测试常用)
    def take_screenshot(driver, name='screenshot'):
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    # 方式2: 添加文本附件
    allure.attach(
        '这是日志内容',
        name='测试日志',
        attachment_type=allure.attachment_type.TEXT
    )

    # 方式3: 添加文件附件
    allure.attach.file(
        './logs/test.log',
        name='完整日志',
        attachment_type=allure.attachment_type.TEXT
    )

    # 方式4: 测试失败时自动截图 (conftest.py中)
    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        report = outcome.get_result()
        if report.when == 'call' and report.failed:
            driver = item.funcargs.get('driver')
            if driver:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f'失败截图_{item.name}',
                    attachment_type=allure.attachment_type.PNG
                )
    """)

    # ---- 5. 完整示例 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("5. 完整Allure测试示例:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import allure
    import pytest

    @allure.epic('电商App')
    @allure.feature('购物车')
    class TestShoppingCart:

        @allure.story('添加商品')
        @allure.title('测试添加单个商品到购物车')
        @allure.severity(allure.severity_level.CRITICAL)
        def test_add_item(self, driver):
            with allure.step('搜索商品'):
                # search_page.search('iPhone')
                pass
            with allure.step('点击添加到购物车'):
                # product_page.add_to_cart()
                pass
            with allure.step('验证购物车数量'):
                assert True  # cart_page.get_count() == 1

        @allure.story('删除商品')
        @allure.title('测试从购物车删除商品')
        @allure.severity(allure.severity_level.NORMAL)
        @pytest.mark.parametrize('product', ['iPhone', 'iPad'])
        def test_remove_item(self, driver, product):
            allure.dynamic.title(f'测试删除{product}')
            with allure.step(f'添加{product}到购物车'):
                pass
            with allure.step(f'删除{product}'):
                pass
            with allure.step('验证购物车为空'):
                assert True
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
        print("1. 第一部分：常用插件介绍")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：测试顺序控制")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：软断言")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：失败重试")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：测试钩子函数 (Hooks)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：自定义插件")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 第七部分：测试报告")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 第八部分：命令行选项")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 实战任务：创建测试套件")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("10. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("11. 今日学习要点总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("12. 补充：Allure报告详解")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("13. 实战任务")
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
        if choice == "12":
            section12()
        elif choice == "13":
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
