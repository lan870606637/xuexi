# -*- coding: utf-8 -*-
"""
Day 10: Day 10
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：参数化测试基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：参数化测试基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize 可以让一个测试用例运行多组数据
    """
    # 基本用法
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("input,expected", [
        (1, 1),
        (2, 4),
        (3, 9),
        (4, 16),
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_square():
        """测试平方"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert input ** 2 == expected
    # 单个参数
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_greeting():
        """测试问候"""
        greeting = f"Hello, {name}!"
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert name in greeting
    # 多个参数
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("username,password,expected", [
        ("admin", "123456", True),
        ("admin", "wrong", False),
        ("user", "password", True),
        ("user", "", False),
        ("", "123456", False),
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_authentication():
        """测试认证"""
        # 模拟认证逻辑
        valid_users = {"admin": "123456", "user": "password"}
        result = valid_users.get(username) == password and username != ""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert result == expected


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：参数化高级用法"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：参数化高级用法")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 给参数化测试添加ID
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("a,b,result", [
        pytest.param(1, 1, 2, id="small_numbers"),
        pytest.param(100, 200, 300, id="large_numbers"),
        pytest.param(-1, 1, 0, id="negative_number"),
        pytest.param(0, 0, 0, id="zeros"),
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_add_with_ids():
        """带ID的参数化测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert a + b == result
    # 条件跳过某些参数
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("platform,version", [
        ("Android", 10),
        ("Android", 11),
        pytest.param("iOS", 14, marks=pytest.mark.skip(reason="iOS暂不支持")),
        ("Android", 12),
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_platform_support():
        """测试平台支持"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert platform in ["Android", "iOS"]
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert version >= 10
    # 标记某些参数为预期失败
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("browser,feature", [
        ("Chrome", "supported"),
        ("Firefox", "supported"),
        pytest.param("IE", "supported", 
                     marks=pytest.mark.xfail(reason="IE不支持此功能")),
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_browser_feature():
        """测试浏览器功能"""
        supported_browsers = ["Chrome", "Firefox"]
        if browser == "IE":
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert browser not in supported_browsers  # 预期失败
        else:
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert browser in supported_browsers


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：参数化与Fixture结合"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：参数化与Fixture结合")
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
    def database():
        """数据库fixture"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return {"connected": True, "data": []}
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("record", [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ])
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_insert_record():
        """测试插入记录"""
        database["data"].append(record)
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert record in database["data"]


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：间接参数化"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：间接参数化")
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
    def user():
        """根据参数创建用户"""
        user_type = request.param
        users = {
            "admin": {"role": "admin", "permissions": ["all"]},
            "user": {"role": "user", "permissions": ["read"]},
            "guest": {"role": "guest", "permissions": []},
        }
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return users.get(user_type, {"role": "unknown", "permissions": []})
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.parametrize("user,expected_permissions", [
        ("admin", ["all"]),
        ("user", ["read"]),
        ("guest", []),
    ], indirect=["user"])  # indirect表示user参数通过fixture解析
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_user_permissions():
        """测试用户权限"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert user["permissions"] == expected_permissions


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：自定义标记"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：自定义标记")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 在pytest.ini中定义标记 (需要创建pytest.ini文件)
    pytest_ini_content = '''
    [pytest]
    markers =
        smoke: 冒烟测试
        regression: 回归测试
        slow: 慢速测试
        integration: 集成测试
        unit: 单元测试
        api: API测试
        ui: UI测试
        critical: 关键测试
        flaky: 不稳定测试
    '''
    # 创建pytest.ini
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open("pytest.ini", "w", encoding="utf-8") as f:
        f.write(pytest_ini_content)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("已创建pytest.ini")
    # 使用自定义标记
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.smoke
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.critical
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_critical_login():
        """关键登录测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.regression
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.slow
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_full_regression():
        """完整回归测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.integration
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.api
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_api_integration():
        """API集成测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.flaky
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.skip(reason="不稳定，暂时跳过")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_flaky_feature():
        """不稳定的功能测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：标记组合和过滤"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：标记组合和过滤")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    运行指定标记的测试:
    # 只运行smoke测试
    pytest -m smoke
    # 运行smoke和critical
    pytest -m "smoke and critical"
    # 运行smoke或regression
    pytest -m "smoke or regression"
    # 排除slow测试
    pytest -m "not slow"
    # 复杂组合
    pytest -m "(smoke or critical) and not slow"
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """第七部分：动态生成测试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第七部分：动态生成测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def pytest_generate_tests():
        """
        钩子函数：动态生成测试参数
        在conftest.py中定义，这里仅作演示
        """
        # 如果测试函数有dynamic_param参数
        if "dynamic_param" in metafunc.fixturenames:
            # 动态生成参数
            values = [1, 2, 3, 4, 5]
            metafunc.parametrize("dynamic_param", values)
    # 注意：这个测试需要在conftest.py中定义钩子才能运行
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def _test_dynamic():
        """动态参数测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert dynamic_param > 0


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """实战任务：参数化测试实战"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：参数化测试实战")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为下面的Calculator类编写完整的参数化测试
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class Calculator:
        """计算器类"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def add():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return a + b
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def subtract():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return a - b
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def multiply():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return a * b
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def divide():
            if b == 0:
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise ValueError("除数不能为零")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return a / b
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def power():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return base ** exponent
    # 请在这里编写参数化测试
    # 提示：
    # 1. 为每个方法编写参数化测试
    # 2. 考虑边界值：0、负数、大数
    # 3. 为divide测试异常情况
    # 4. 使用pytest.raises测试异常


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
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestCalculator:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def setup_method():
            self.calc = Calculator()
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("a,b,expected", [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (-1, -1, -2),
            (100, 200, 300),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_add():
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert self.calc.add(a, b) == expected
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("a,b,expected", [
            (5, 3, 2),
            (0, 5, -5),
            (-1, -1, 0),
            (100, 50, 50),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_subtract():
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert self.calc.subtract(a, b) == expected
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("a,b,expected", [
            (2, 3, 6),
            (0, 100, 0),
            (-2, 3, -6),
            (-2, -3, 6),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_multiply():
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert self.calc.multiply(a, b) == expected
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("a,b,expected", [
            (6, 2, 3),
            (5, 2, 2.5),
            (0, 5, 0),
            (-6, 2, -3),
            (-6, -2, 3),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_divide():
            result = self.calc.divide(a, b)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result == pytest.approx(expected)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_divide_by_zero():
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with pytest.raises(ValueError, match="除数不能为零"):
                self.calc.divide(10, 0)
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.mark.parametrize("base,exponent,expected", [
            (2, 3, 8),
            (5, 0, 1),
            (2, -1, 0.5),
            (0, 5, 0),
        ])
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_power():
            result = self.calc.power(base, exponent)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result == pytest.approx(expected)
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
    1. 参数化测试:
       - @pytest.mark.parametrize
       - 单个参数、多个参数
       - 使用pytest.param添加ID
    2. 参数化高级:
       - 条件跳过某些参数
       - 标记预期失败
       - 与fixture结合
       - indirect参数化
    3. 自定义标记:
       - 在pytest.ini中定义
       - 使用marks装饰器
       - 命令行过滤标记
    4. 动态测试:
       - pytest_generate_tests钩子
       - 运行时生成参数
    验证标准：能写出带参数化的测试用例
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
        print("1. 第一部分：参数化测试基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：参数化高级用法")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：参数化与Fixture结合")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：间接参数化")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：自定义标记")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：标记组合和过滤")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 第七部分：动态生成测试")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 实战任务：参数化测试实战")
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
        if choice == "9":
            section9()
        if choice == "10":
            section10()
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
