# -*- coding: utf-8 -*-
"""
Day 7: Day 7
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：函数是一等公民"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：函数是一等公民")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("函数是一等公民:")
    # 函数可以赋值给变量
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def greet():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return f"Hello, {name}!"
    say_hello = greet  # 没有括号，是赋值不是调用
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(say_hello("Alice"))
    # 函数可以作为参数
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def execute():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return func(arg)
    result = execute(greet, "Bob")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(result)
    # 函数可以作为返回值
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def make_multiplier():
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def multiplier():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return x * n
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return multiplier
    double = make_multiplier(2)
    triple = make_multiplier(3)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"double(5) = {double(5)}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"triple(5) = {triple(5)}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：装饰器基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：装饰器基础")
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
    print("装饰器基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 最简单的装饰器
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def my_decorator():
        """装饰器：在函数执行前后添加操作"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wrapper():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("函数执行前")
            func()
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("函数执行后")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return wrapper
    # 【装饰器 @my_decorator】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @my_decorator
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def say_hi():
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("Hi!")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("使用装饰器:")
    say_hi()
    # 等价于：
    # say_hi = my_decorator(say_hi)
    # 带参数的装饰器
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def timer_decorator():
        """计时装饰器"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wrapper():
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return result
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return wrapper
    # 【装饰器 @timer_decorator】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @timer_decorator
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def slow_function():
        time.sleep(0.1)
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "Done"
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n计时装饰器:")
    result = slow_function()
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"结果: {result}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：日志装饰器"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：日志装饰器")
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
    print("日志装饰器")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def log_decorator():
        """日志装饰器：记录函数调用信息"""
        # 【装饰器 @functools】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @functools.wraps(func)  # 保留原函数信息
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wrapper():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[LOG] 调用 {func.__name__}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[LOG] 位置参数: {args}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[LOG] 关键字参数: {kwargs}")
            result = func(*args, **kwargs)
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[LOG] 返回: {result}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return result
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return wrapper
    # 【装饰器 @log_decorator】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @log_decorator
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_login():
        """测试登录"""
        if username == "admin" and password == "123":
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "登录成功"
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "登录失败"
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("日志装饰器示例:")
    test_login("admin", "123")
    # 带参数的装饰器 (装饰器工厂)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def log_with_level():
        """带级别的日志装饰器"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def decorator():
            # 【装饰器 @functools】
            # 作用: 在不修改原函数的情况下，添加额外功能
            # 原理: 接收函数作为参数，返回新函数
            @functools.wraps(func)
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def wrapper():
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"[{level}] 执行 {func.__name__}")
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return func(*args, **kwargs)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return wrapper
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return decorator
    # 【装饰器 @log_with_level】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @log_with_level("DEBUG")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def debug_test():
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("调试测试")
    # 【装饰器 @log_with_level】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @log_with_level("ERROR")
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def error_test():
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("错误测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n带级别的日志装饰器:")
    debug_test()
    error_test()


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：重试装饰器"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：重试装饰器")
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
    print("重试装饰器")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
        """
        重试装饰器
        参数:
            max_attempts: 最大尝试次数
            delay: 重试间隔(秒)
            exceptions: 捕获的异常类型
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def decorator():
            # 【装饰器 @functools】
            # 作用: 在不修改原函数的情况下，添加额外功能
            # 原理: 接收函数作为参数，返回新函数
            @functools.wraps(func)
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def wrapper():
                for attempt in range(1, max_attempts + 1):
                    # 【异常处理 try-except】
                    # 语法: try: ... except 异常类型: ...
                    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
                    try:
                        # print() - 打印输出
                        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                        # 作用: 把内容输出到控制台
                        print(f"[Retry] 第{attempt}次尝试 {func.__name__}")
                        # return - 返回值
                        # 作用: 将结果返回给调用者，结束函数执行
                        return func(*args, **kwargs)
                    except exceptions as e:
                        # print() - 打印输出
                        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                        # 作用: 把内容输出到控制台
                        print(f"[Retry] 失败: {e}")
                        if attempt == max_attempts:
                            # print() - 打印输出
                            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                            # 作用: 把内容输出到控制台
                            print(f"[Retry] 所有{max_attempts}次尝试都失败")
                            raise
                        time.sleep(delay)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return wrapper
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return decorator
    # 模拟不稳定的操作
    attempt_count = 0
    # 【装饰器 @retry】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @retry(max_attempts=3, delay=0.5)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def unstable_operation():
        """不稳定的操作"""
        global attempt_count
        attempt_count += 1
        if attempt_count < 3:
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise Exception("操作失败")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "操作成功"
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("重试装饰器示例:")
    attempt_count = 0
    result = unstable_operation()
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"最终结果: {result}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：上下文管理器 (with语句)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：上下文管理器 (with语句)")
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
    print("上下文管理器")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 使用类实现上下文管理器
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class Timer:
        """计时上下文管理器"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __enter__():
            """进入上下文时调用"""
            self.start = time.time()
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Timer] 开始计时")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __exit__():
            """退出上下文时调用"""
            self.end = time.time()
            self.interval = self.end - self.start
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Timer] 结束计时: {self.interval:.4f}秒")
            # 返回False表示不处理异常，返回True表示已处理异常
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return False
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("使用Timer上下文管理器:")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with Timer():
        time.sleep(0.1)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("执行一些操作...")
    # 使用contextlib简化
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from contextlib import contextmanager
    # 【装饰器 @contextmanager】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @contextmanager
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def managed_resource():
        """资源管理上下文管理器"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"[Resource] 获取资源: {name}")
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            yield name  # yield之前的代码是__enter__，之后的是__exit__
        finally:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Resource] 释放资源: {name}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n使用contextmanager:")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with managed_resource("数据库连接") as resource:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"使用资源: {resource}")
    # 测试上下文管理器
    # 【装饰器 @contextmanager】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @contextmanager
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_context():
        """测试上下文"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n[TEST] 开始测试: {test_name}")
        start = time.time()
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            yield
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[TEST] 测试通过: {test_name}")
        except Exception as e:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[TEST] 测试失败: {test_name} - {e}")
            raise
        finally:
            elapsed = time.time() - start
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[TEST] 耗时: {elapsed:.4f}秒")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试上下文示例:")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with test_context("登录测试"):
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("执行登录操作...")
        # 模拟成功


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """实战任务：实现 @retry 装饰器"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：实现 @retry 装饰器")
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
    print("实战任务：完善重试装饰器")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def my_retry():
        """
        完善的重试装饰器
        参数:
            max_attempts: 最大尝试次数
            delay: 重试间隔(秒)
            on_retry: 重试时的回调函数，接收(attempt, exception)参数
        示例:
            # 【装饰器 @my_retry】
            # 作用: 在不修改原函数的情况下，添加额外功能
            # 原理: 接收函数作为参数，返回新函数
            @my_retry(max_attempts=3, delay=1)
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def test_login():
                # 测试代码
                pass
        """
        # 你的代码写在这里：
        # 提示：
        # 1. 定义decorator函数接收func
        # 2. 定义wrapper函数接收*args, **kwargs
        # 3. 使用for循环进行重试
        # 4. 如果有on_retry回调，在重试前调用
        # 5. 成功则返回结果，失败则抛出最后一次异常
        pass  # 删除这行，写上你的代码
    # 测试代码 (取消注释测试)
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试my_retry:")
    # 测试1: 带回调的重试
    attempts = []
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def on_retry_callback():
        # append() - 列表末尾添加元素
        # 语法: 列表.append(元素)
        # 返回值: None（直接修改原列表）
        attempts.append(attempt)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  回调: 第{attempt}次重试，错误: {exception}")
    # 【装饰器 @test_count】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @test_count = 0
    # 【装饰器 @my_retry】
    # 作用: 在不修改原函数的情况下，添加额外功能
    # 原理: 接收函数作为参数，返回新函数
    @my_retry(max_attempts=3, delay=0.1, on_retry=on_retry_callback)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def flaky_test():
        global test_count
        test_count += 1
        if test_count < 3:
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise Exception(f"第{test_count}次失败")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return "成功"
    test_count = 0
    attempts = []
    result = flaky_test()
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"结果: {result}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"重试记录: {attempts}")
    """


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
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def my_retry():
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def decorator():
            # 【装饰器 @functools】
            # 作用: 在不修改原函数的情况下，添加额外功能
            # 原理: 接收函数作为参数，返回新函数
            @functools.wraps(func)
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def wrapper():
                last_exception = None
                for attempt in range(1, max_attempts + 1):
                    # 【异常处理 try-except】
                    # 语法: try: ... except 异常类型: ...
                    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
                    try:
                        # return - 返回值
                        # 作用: 将结果返回给调用者，结束函数执行
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        if attempt < max_attempts:
                            if on_retry:
                                on_retry(attempt, e)
                            time.sleep(delay)
                # 所有尝试都失败
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise last_exception
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return wrapper
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return decorator
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
    1. 函数是一等公民：
       - 可以赋值给变量
       - 可以作为参数
       - 可以作为返回值
    2. 装饰器：
       - @decorator语法糖
       - 本质是函数返回函数
       - @functools.wraps保留原函数信息
       - 带参数的装饰器需要三层嵌套
    3. 常用装饰器：
       - 日志装饰器：记录调用信息
       - 计时装饰器：统计执行时间
       - 重试装饰器：失败自动重试
    4. 上下文管理器：
       - __enter__和__exit__方法
       - @contextmanager简化写法
       - 用于资源管理、测试上下文等
    验证标准：能写出简单的装饰器
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
        print("1. 第一部分：函数是一等公民")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：装饰器基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：日志装饰器")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：重试装饰器")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：上下文管理器 (with语句)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务：实现 @retry 装饰器")
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
