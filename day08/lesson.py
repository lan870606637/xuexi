# -*- coding: utf-8 -*-
"""
Day 8: Day 8
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：Pytest简介和安装"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：Pytest简介和安装")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Pytest是Python最流行的测试框架，特点：
    1. 简单易用，无需类也能写测试
    2. 丰富的插件生态
    3. 强大的fixture机制
    4. 详细的失败报告
    安装命令:
        pip install pytest
    验证安装:
        pytest --version
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：第一个测试用例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：第一个测试用例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 最简单的测试 - 函数名以test_开头
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_addition():
        """测试加法"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 1 + 1 == 2
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_subtraction():
        """测试减法"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 5 - 3 == 2


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：断言 (assert)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：断言 (assert)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Pytest使用assert进行断言，比unittest更简单
    """
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_assert_types():
        """各种断言示例"""
        # 基本相等
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 1 + 1 == 2
        # 不相等
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 1 + 1 != 3
        # 大于/小于
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 5 > 3
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 3 < 5
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 5 >= 5
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 3 <= 5
        # 包含
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "hello" in "hello world"
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "xyz" not in "hello world"
        # 布尔值
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert not False
        # 类型判断
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert isinstance(123, int)
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert isinstance("hello", str)
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert isinstance([1, 2, 3], list)
        # 空值判断
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert None is None
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert [] is not None
        # 近似相等 (浮点数)
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert 0.1 + 0.2 == pytest.approx(0.3)
    # 需要导入pytest才能使用approx
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import pytest
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_float_comparison():
        """浮点数比较"""
        result = 0.1 + 0.2
        # 错误写法：assert result == 0.3  # 会失败！
        # 正确写法：
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert result == pytest.approx(0.3)
        # 也可以指定精度
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert result == pytest.approx(0.3, abs=1e-9)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：测试类组织"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：测试类组织")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestCalculator:
        """计算器测试类 - 类名以Test开头"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_add():
            """测试加法"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert 2 + 2 == 4
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_multiply():
            """测试乘法"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert 3 * 4 == 12
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_divide():
            """测试除法"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert 10 / 2 == 5
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestString:
        """字符串测试类"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_upper():
            """测试转大写"""
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "hello".upper() == "HELLO"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_split():
            """测试分割"""
            s = "hello world"
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert s.split() == ["hello", "world"]


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：测试失败和跳过"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：测试失败和跳过")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_expected_failure():
        """预期会失败的测试"""
        # 使用pytest.mark.xfail标记预期失败
        pytest.xfail("这个功能还没实现")
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.skip(reason="暂时跳过这个测试")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_skipped():
        """被跳过的测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert False  # 不会执行
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.skipif(True, reason="条件为真时跳过")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_conditional_skip():
        """条件跳过"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：标记和分组"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：标记和分组")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.smoke
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_smoke_test():
        """冒烟测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.regression
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_regression_test():
        """回归测试"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.smoke
    # 【装饰器 @pytest】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @pytest.mark.regression
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_both():
        """既是冒烟又是回归"""
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert True
    """
    运行指定标记的测试:
        pytest -m smoke          # 只运行smoke标记的测试
        pytest -m "not smoke"    # 排除smoke标记的测试
        pytest -m "smoke or regression"  # 运行任一标记的测试
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """第七部分：命令行运行"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第七部分：命令行运行")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    常用pytest命令:
    1. 运行所有测试:
        pytest
    2. 运行指定文件:
        pytest test_sample.py
    3. 运行指定类:
        pytest test_sample.py::TestCalculator
    4. 运行指定方法:
        pytest test_sample.py::TestCalculator::test_add
    5. 显示详细输出:
        pytest -v
    6. 显示打印信息:
        pytest -s
    7. 停止在第一个失败:
        pytest -x
    8. 生成HTML报告 (需安装pytest-html):
        pytest --html=report.html
    9. 只运行上次失败的:
        pytest --lf
    10. 先运行上次失败的，再运行其他的:
        pytest --ff
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """实战任务：编写测试用例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：编写测试用例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为下面的Login类编写测试用例
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class Login:
        """登录功能"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.users = {
                "admin": "123456",
                "user": "password"
            }
            self.logged_in_user = None
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login():
            """登录"""
            if not username or not password:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "message": "用户名或密码不能为空"}
            if username not in self.users:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "message": "用户不存在"}
            if self.users[username] != password:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": False, "message": "密码错误"}
            self.logged_in_user = username
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"success": True, "message": "登录成功"}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def logout():
            """登出"""
            if self.logged_in_user:
                user = self.logged_in_user
                self.logged_in_user = None
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {"success": True, "message": f"用户{user}已登出"}
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"success": False, "message": "没有用户登录"}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_logged_in():
            """检查是否已登录"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.logged_in_user is not None
    # 请在这里编写测试用例
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestLogin:
        """登录功能测试"""
        # 你的代码写在这里：
        # 提示：
        # 1. 使用pytest.fixture或setUp创建Login实例
        # 2. 测试正常登录
        # 3. 测试错误密码
        # 4. 测试空用户名/密码
        # 5. 测试不存在的用户
        # 6. 测试登出功能
        pass


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
    class TestLogin:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def setup_method():
            # 每个测试方法前执行
            self.login = Login()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_success():
            result = self.login.login("admin", "123456")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is True
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["message"] == "登录成功"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_wrong_password():
            result = self.login.login("admin", "wrong")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is False
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["message"] == "密码错误"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_empty_username():
            result = self.login.login("", "123456")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is False
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "不能为空" in result["message"]
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_user_not_exist():
            result = self.login.login("notexist", "123456")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is False
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["message"] == "用户不存在"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_logout():
            self.login.login("admin", "123456")
            result = self.login.logout()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert result["success"] is True
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert self.login.is_logged_in() is False
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
    1. Pytest安装: pip install pytest
    2. 测试发现规则:
       - 文件: test_*.py 或 *_test.py
       - 函数: test_开头
       - 类: Test开头
    3. 断言:
       - 使用assert
       - pytest.approx用于浮点数
    4. 标记:
       - @pytest.mark.skip 跳过
       - @pytest.mark.xfail 预期失败
       - @pytest.mark.custom 自定义标记
    5. 命令行:
       - pytest -v 详细输出
       - pytest -s 显示print
       - pytest -m smoke 按标记运行
    验证标准：能运行Pytest并看到测试结果
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
        print("1. 第一部分：Pytest简介和安装")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：第一个测试用例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：断言 (assert)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：测试类组织")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：测试失败和跳过")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：标记和分组")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 第七部分：命令行运行")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 实战任务：编写测试用例")
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
