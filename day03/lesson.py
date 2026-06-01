# -*- coding: utf-8 -*-
"""
Day 3: 函数（核心重点）
学习目标：掌握函数定义和调用，理解*args和**kwargs，为封装测试工具打基础
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：函数基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：函数基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    
    # 定义函数 (def关键字)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def say_hello():
        """这是一个简单的函数，打印问候语"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  Hello, World!")

    # 调用函数
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n基础函数:")
    say_hello()

    # 带参数的函数
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def greet(name):
        """带参数的函数"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  Hello, {name}!")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n带参数的函数:")
    greet("Alice")
    greet("Bob")

    # 带返回值的函数
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def add(a, b):
        """返回两个数的和"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return a + b

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n带返回值的函数:")
    result = add(3, 5)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  3 + 5 = {result}")

    # 多返回值 (实际上是返回元组)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def get_min_max(numbers):
        """返回列表中的最小值和最大值"""
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return min(numbers), max(numbers)

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n多返回值:")
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    min_val, max_val = get_min_max(nums)  # 解包赋值
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  列表: {nums}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  最小值: {min_val}, 最大值: {max_val}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：参数类型"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：参数类型详解")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # 1. 位置参数 (必须按顺序传)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def login(username, password):
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  登录用户: {username}, 密码: {'*' * len(password)}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. 位置参数:")
    login("admin", "123456")

    # 2. 默认参数 (不传就使用默认值)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def connect_db(host="localhost", port=3306):
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  连接数据库: {host}:{port}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n2. 默认参数:")
    connect_db()  # 使用全部默认值
    connect_db("192.168.1.1")  # 只传host
    connect_db(port=5432)  # 只传port (关键字传参)
    connect_db(host="10.0.0.1", port=3307)  # 都传

    # 3. 关键字参数 (可以打乱顺序)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def create_user(name, age=18, role="user"):
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  创建用户: {name}, 年龄: {age}, 角色: {role}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n3. 关键字参数:")
    create_user(age=25, name="张三")  # 顺序不重要
    create_user("李四", role="admin", age=30)  # 混合使用


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：*args 和 **kwargs (重点！)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：*args 和 **kwargs (重点)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # *args - 接收任意数量的位置参数
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def sum_all(*args):
        """
        *args 会将多余的位置参数打包成元组(tuple)
        args就是一个元组，可以遍历
        """
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  args类型: {type(args)}, 值: {args}")
        total = 0
        for num in args:
            total += num
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return total

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n*args示例:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  sum_all(10, 20) = {sum_all(10, 20)}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  sum_all() = {sum_all()}")

    # **kwargs - 接收任意数量的关键字参数
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def print_config(**kwargs):
        """
        **kwargs 会将多余的关键字参数打包成字典(dict)
        kwargs就是一个字典
        """
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  kwargs类型: {type(kwargs)}, 值: {kwargs}")
        for key, value in kwargs.items():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"    {key} = {value}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n**kwargs示例:")
    print_config(platform="Android", version=12, device="emulator")

    # 组合使用: def func(a, b, *args, c=1, **kwargs)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def complex_function(required, default="默认值", *args, **kwargs):
        """
        参数顺序：
        1. 位置参数 (required)
        2. 默认参数 (default)
        3. *args
        4. **kwargs
        """
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  required: {required}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  default: {default}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  args: {args}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  kwargs: {kwargs}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n组合参数示例:")
    complex_function("必须参数", "自定义默认值", 1, 2, 3, 
                     extra1="值1", extra2="值2")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：函数作为参数 (高阶函数)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：函数作为参数")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # 函数可以像变量一样传递
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def execute_test(test_func, test_name):
        """执行测试函数"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n  开始执行: {test_name}")
        result = test_func()
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  执行结果: {result}")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return result

    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_login():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "登录测试通过"

    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_register():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "注册测试通过"

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n传递函数:")
    execute_test(test_login, "登录测试")
    execute_test(test_register, "注册测试")

    # lambda表达式 (匿名函数)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\nlambda表达式:")
    # lambda - 匿名函数
    # 语法: lambda 参数: 返回值
    # 作用: 创建简单的单行函数
    square = lambda x: x ** 2
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  square(5) = {square(5)}")

    # lambda常用于简单操作
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  平方列表: {squared}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：作用域"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：作用域")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # 局部变量
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def local_example():
        local_var = "我是局部变量"
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  {local_var}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n局部变量:")
    local_example()
    # print(local_var)  # 错误！外部访问不到

    # 全局变量
    global_var = "我是全局变量"

    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def use_global():
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  函数内访问: {global_var}")

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n全局变量:")
    use_global()
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"  函数外访问: {global_var}")

    # 修改外层函数的变量 (使用nonlocal关键字)
    # 正确用法：需要嵌套函数
    def outer():
        counter = 0

        def increment():
            nonlocal counter
            counter += 1
            print(f"  计数器: {counter}")

        return increment

    print("\n修改外部变量 (nonlocal正确用法):")
    inc = outer()
    inc()
    inc()
    inc()


# 模拟driver (实际项目中是真实的WebDriver)
# 【类定义】
# 语法: class 类名:
# 作用: 创建对象模板，封装数据和方法
class MockDriver:
    """模拟WebDriver，用于演示"""
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def find_element(self, by, value):
        # 模拟查找逻辑
        found_elements = {
            ("id", "username"): "找到用户名输入框",
            ("xpath", "//input"): "找到输入框",
            ("css selector", ".btn"): "找到按钮",
        }
        key = (by, value)
        if key in found_elements:
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return found_elements[key]
        # raise - 主动抛出异常
        # 作用: 当遇到错误条件时，主动抛出异常
        raise Exception(f"元素未找到: {by}={value}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def practice_task():
    """实战任务：封装元素定位函数"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：封装元素定位函数")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
任务描述：
封装一个find_element函数，支持多种定位方式，按顺序尝试
直到找到元素或所有方式都尝试完毕

locator格式: ("id", "username") 或 ("xpath", "//input[@id='username']")
""")

    driver = MockDriver()

    # 请完成下面的函数
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def find_element():
        """
        按顺序尝试多种定位方式查找元素
        
        参数:
            driver: WebDriver实例
            *locators: 多个定位器元组
            timeout: 超时时间(秒)，默认10
            retry: 重试次数，默认3
        
        返回:
            找到的元素
        """
        # 你的代码写在这里：
        pass

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n请修改代码完成find_element函数")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("提示：")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("1. 遍历locators")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. 对每个locator进行retry次尝试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("3. 使用try-except捕获异常")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. 如果找到就返回，否则继续下一个locator")


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
    
    code = '''
# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def find_element(driver, *locators, retry=3):
    # 遍历所有定位方式
    for locator in locators:
        by, value = locator  # 解包
        # 重试机制
        for attempt in range(retry):
            try:
                element = driver.find_element(by, value)
                print(f"使用 {by}={value} 找到元素")
                return element
            except Exception as e:
                print(f"第{attempt+1}次尝试失败: {by}={value}")
                if attempt == retry - 1:
                    break  # 当前定位方式重试完毕，尝试下一个

    # 所有定位方式都失败
    # raise - 主动抛出异常
    # 作用: 当遇到错误条件时，主动抛出异常
    raise Exception(f"所有定位方式都失败: {locators}")

# 调用示例：
# driver = MockDriver()
# element = find_element(
#     driver,
#     ("id", "username"),
#     ("xpath", "//input"),
#     ("css selector", ".btn"),
#     retry=3
# )
'''
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(code)


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
    print("今日学习要点总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    
    summary = """
1. 函数定义：def关键字，文档字符串
2. 参数类型：
   - 位置参数：必须按顺序传
   - 默认参数：不传使用默认值
   - 关键字参数：可以打乱顺序
3. *args：接收任意数量的位置参数，打包成元组
4. **kwargs：接收任意数量的关键字参数，打包成字典
5. 返回值：可以返回多个值（实际是元组）
6. 作用域：局部变量、全局变量、global关键字
7. lambda：匿名函数，用于简单操作

验证标准：能写出带默认参数和可变参数的函数
"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(summary)


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
        print("Day 3: 函数（核心重点）- 学习菜单")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("1. 函数基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 参数类型")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. *args 和 **kwargs")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 函数作为参数")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 作用域")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 参考答案")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 学习总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("0. 退出")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        
        choice = input("\n请选择要学习的部分 (0-8): ").strip()
        
        if choice == "1":
            section1()
        elif choice == "2":
            section2()
        elif choice == "3":
            section3()
        elif choice == "4":
            section4()
        elif choice == "5":
            section5()
        elif choice == "6":
            practice_task()
        elif choice == "7":
            show_answer()
        elif choice == "8":
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
