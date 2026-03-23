# -*- coding: utf-8 -*-
"""
Day 5: Day 5
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：异常基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：异常基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 什么是异常？
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("异常示例:")
    # 这段代码会报错
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"捕获到除零错误: {e}")
    # 常见的异常类型
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n常见异常类型:")
    # ValueError
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        num = int("abc")
    except ValueError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"ValueError: {e}")
    # TypeError
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        result = "10" + 5
    except TypeError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"TypeError: {e}")
    # KeyError
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        data = {"name": "Tom"}
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(data["age"])
    except KeyError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"KeyError: 键 {e} 不存在")
    # IndexError
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        lst = [1, 2, 3]
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(lst[10])
    except IndexError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"IndexError: {e}")
    # FileNotFoundError
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        # 【with 语句】
        # 作用: 自动管理资源，确保文件等正确关闭
        # 原理: 使用上下文管理器 __enter__ 和 __exit__
        with open("not_exist.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"FileNotFoundError: {e}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：try-except-else-finally"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：try-except-else-finally")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("完整的异常处理结构")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def divide():
        """除法运算，演示完整异常处理"""
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            # 尝试执行的代码
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"尝试计算: {a} / {b}")
            result = a / b
        except ZeroDivisionError:
            # 发生特定异常时执行
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("错误：除数不能为零")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return None
        except TypeError:
            # 另一种异常
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("错误：参数类型不正确")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return None
        except Exception as e:
            # 捕获所有其他异常
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"未知错误: {e}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return None
        else:
            # 没有异常时执行
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("计算成功！")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return result
        finally:
            # 无论是否异常都会执行
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("计算结束\n")
    # 测试各种情况
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("测试1: 正常情况")
    divide(10, 2)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("测试2: 除零")
    divide(10, 0)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("测试3: 类型错误")
    divide("10", 2)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：捕获多个异常"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：捕获多个异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("捕获多个异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 方式1：多个except
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def read_config_v1():
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, 'r') as f:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return f.read()
        except FileNotFoundError:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"配置文件不存在: {file_path}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "{}"
        except PermissionError:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"没有权限读取: {file_path}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "{}"
    # 方式2：合并捕获
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def read_config_v2():
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, 'r') as f:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return f.read()
        except (FileNotFoundError, PermissionError) as e:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"读取失败: {e}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "{}"
    # 方式3：捕获所有异常 (谨慎使用)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def read_config_v3():
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, 'r') as f:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return f.read()
        except Exception as e:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"读取失败: {type(e).__name__}: {e}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "{}"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：自定义异常"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：自定义异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("自定义异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 定义测试相关的自定义异常
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestFrameworkError(Exception):
        """测试框架基础异常"""
        pass
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ElementNotFoundError(TestFrameworkError):
        """元素未找到异常"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.locator = locator
            self.message = message
            super().__init__(f"{message}: {locator}")
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestDataError(TestFrameworkError):
        """测试数据错误"""
        pass
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TimeoutError(TestFrameworkError):
        """超时错误"""
        pass
    # 使用自定义异常
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ElementFinder:
        """元素查找器"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.driver = driver
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find():
            """查找元素，找不到抛出自定义异常"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"查找元素: {locator} (超时: {timeout}s)")
            # 模拟查找失败
            found = False  # 实际应该调用driver.find_element
            if not found:
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise ElementNotFoundError(locator)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "Element"
    # 测试自定义异常
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试自定义异常:")
    finder = ElementFinder("MockDriver")
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        finder.find(("id", "username"))
    except ElementNotFoundError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"捕获自定义异常: {e}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：raise抛出异常"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：raise抛出异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("raise抛出异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def validate_test_data():
        """验证测试数据"""
        if not isinstance(data, dict):
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise TestDataError("测试数据必须是字典类型")
        if "username" not in data:
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise TestDataError("缺少username字段")
        if "password" not in data:
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise TestDataError("缺少password字段")
        if len(data["password"]) < 6:
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise TestDataError("密码长度不能少于6位")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("数据验证通过")
    # 测试数据验证
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试数据验证:")
    test_cases = [
        {"username": "admin", "password": "123456"},  # 正确
        "invalid data",  # 类型错误
        {"username": "admin"},  # 缺少password
        {"username": "admin", "password": "123"},  # 密码太短
    ]
    for i, data in enumerate(test_cases):
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n测试用例 {i+1}: {data}")
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            validate_test_data(data)
        except TestDataError as e:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"验证失败: {e}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：异常链 (异常传递)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：异常链 (异常传递)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("异常链")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def low_level_operation():
        """底层操作"""
        # raise - 主动抛出异常
        # 作用: 当遇到错误条件时，主动抛出异常
        raise ConnectionError("网络连接失败")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def high_level_operation():
        """高层操作"""
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            low_level_operation()
        except ConnectionError as e:
            # 捕获底层异常，包装成高层异常
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise TestFrameworkError("测试执行失败") from e
    # 测试异常链
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试异常链:")
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        high_level_operation()
    except TestFrameworkError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"高层异常: {e}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"原始异常: {e.__cause__}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """实战任务：带重试的元素点击"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：带重试的元素点击")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：带重试的元素点击")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：实现一个safe_click函数，具有以下特性：
    1. 支持重试机制
    2. 捕获常见异常
    3. 记录每次重试的信息
    4. 所有重试失败后抛出异常
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockDriver:
        """模拟WebDriver"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.attempt = 0
            self.fail_times = fail_times
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_element():
            self.attempt += 1
            if self.attempt <= self.fail_times:
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise Exception(f"元素未找到 (尝试{self.attempt})")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return f"Element({locator})"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"点击元素: {element}")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def safe_click():
        """
        带重试的元素点击
        参数:
            driver: WebDriver实例
            locator: 元素定位器
            retry: 重试次数，默认3
            delay: 每次重试间隔(秒)，默认1
        返回:
            点击的元素
        异常:
            所有重试失败后抛出ElementNotFoundError
        """
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import time
        # 你的代码写在这里：
        # 提示：
        # 1. 使用for循环进行retry次尝试
        # 2. 使用try-except捕获异常
        # 3. 每次失败打印信息并等待delay秒
        # 4. 成功则返回元素
        # 5. 全部失败则抛出ElementNotFoundError
        pass  # 删除这行，写上你的代码
    # 测试代码 (取消注释测试)
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试safe_click:")
    # 测试1: 第2次成功
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试1: 第2次成功")
    driver1 = MockDriver(fail_times=1)
    elem = safe_click(driver1, "id:username", retry=3)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"成功点击: {elem}")
    # 测试2: 一直失败
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试2: 一直失败")
    driver2 = MockDriver(fail_times=5)
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        elem = safe_click(driver2, "id:password", retry=3)
    except ElementNotFoundError as e:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"预期异常: {e}")
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
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
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def safe_click():
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import time
        for attempt in range(retry):
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"第{attempt + 1}次尝试点击: {locator}")
                element = driver.find_element(locator)
                driver.click(element)
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"点击成功!")
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return element
            except Exception as e:
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"  失败: {e}")
                if attempt < retry - 1:
                    # print() - 打印输出
                    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                    # 作用: 把内容输出到控制台
                    print(f"  等待{delay}秒后重试...")
                    time.sleep(delay)
                else:
                    # print() - 打印输出
                    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                    # 作用: 把内容输出到控制台
                    print(f"  所有{retry}次尝试都失败")
        # 所有重试失败
        # raise - 主动抛出异常
        # 作用: 当遇到错误条件时，主动抛出异常
        raise ElementNotFoundError(locator, f"点击失败，已重试{retry}次")
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section9():
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
    1. 异常类型：
       - ValueError, TypeError, KeyError, IndexError
       - FileNotFoundError, ZeroDivisionError等
    2. 异常处理结构：
       - try: 尝试执行的代码
       - except: 捕获异常
       - else: 无异常时执行
       - finally: 无论是否异常都执行
    3. 捕获多个异常：
       - 多个except块
       - except (A, B) as e
    4. 自定义异常：
       - 继承Exception或其子类
       - 可以添加自定义属性
    5. raise：
       - 抛出异常
       - raise X from Y (异常链)
    6. 最佳实践：
       - 捕获具体异常，不要裸except
       - 使用finally释放资源
       - 自定义异常提高代码可读性
    验证标准：能写出带异常处理和重试的函数
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
        print("1. 第一部分：异常基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：try-except-else-finally")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：捕获多个异常")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：自定义异常")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：raise抛出异常")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：异常链 (异常传递)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 实战任务：带重试的元素点击")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 今日学习要点总结")
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
