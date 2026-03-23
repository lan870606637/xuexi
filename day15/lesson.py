# -*- coding: utf-8 -*-
"""
Day 15: Day 15
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：项目结构"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：项目结构")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    PROJECT_STRUCTURE = """
    项目结构:
    my_test_framework/
    ├── config/                 # 配置文件
    │   ├── config.yaml        # 主配置
    │   ├── android_caps.yaml  # Android配置
    │   └── ios_caps.yaml      # iOS配置
    ├── pages/                  # 页面对象
    │   ├── base_page.py
    │   ├── login_page.py
    │   └── home_page.py
    ├── tests/                  # 测试用例
    │   ├── conftest.py
    │   └── test_login.py
    ├── utils/                  # 工具类
    │   ├── logger.py          # 日志工具
    │   ├── config_reader.py   # 配置读取
    │   └── driver_factory.py  # Driver工厂
    ├── reports/                # 测试报告
    │   └── .gitkeep
    ├── logs/                   # 日志文件
    │   └── .gitkeep
    ├── screenshots/            # 截图
    │   └── .gitkeep
    ├── data/                   # 测试数据
    │   └── test_data.json
    ├── requirements.txt
    └── pytest.ini
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(PROJECT_STRUCTURE)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：配置管理"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：配置管理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ConfigReader:
        """
        配置读取器
        支持YAML和JSON格式
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.config_dir = Path(config_dir)
            self._configs = {}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def load():
            """
            加载配置文件
            参数:
                filename: 配置文件名
            返回:
                配置字典
            """
            if filename in self._configs:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._configs[filename]
            file_path = self.config_dir / filename
            if not file_path.exists():
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise FileNotFoundError(f"配置文件不存在: {file_path}")
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, "r", encoding="utf-8") as f:
                if filename.endswith(".yaml") or filename.endswith(".yml"):
                    config = yaml.safe_load(f)
                elif filename.endswith(".json"):
                    config = json.load(f)
                else:
                    # raise - 主动抛出异常
                    # 作用: 当遇到错误条件时，主动抛出异常
                    raise ValueError(f"不支持的配置文件格式: {filename}")
            self._configs[filename] = config
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return config
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get():
            """
            获取配置值
            参数:
                filename: 配置文件名
                key: 配置键，支持点号分隔 (如 "database.host")
                default: 默认值
            """
            config = self.load(filename)
            if key is None:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return config
            # 支持嵌套键 (如 "database.host")
            keys = key.split(".")
            value = config
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return default
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return value
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def reload():
            """重新加载配置"""
            if filename:
                self._configs.pop(filename, None)
            else:
                self._configs.clear()
    # 配置示例
    CONFIG_EXAMPLE = """
    # config/config.yaml
    environment: test
    appium:
      server_url: "http://localhost:4723/wd/hub"
      implicit_wait: 10
      explicit_wait: 20
    database:
      host: localhost
      port: 3306
      name: test_db
      user: test_user
      password: test_pass
    report:
      screenshot_on_failure: true
      html_report: true
      allure_report: true
    log:
      level: INFO
      format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
      file: logs/test.log
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n配置示例:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(CONFIG_EXAMPLE)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：日志封装"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：日志封装")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class Logger:
        """
        日志工具类
        封装Python logging模块
        """
        _loggers = {}
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_logger():
            """
            获取日志记录器
            参数:
                name: 日志名称
                log_dir: 日志目录
                level: 日志级别
            """
            if name in cls._loggers:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return cls._loggers[name]
            # 创建logger
            logger = logging.getLogger(name)
            logger.setLevel(level)
            # 避免重复添加handler
            if logger.handlers:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return logger
            # 创建日志目录
            log_path = Path(log_dir)
            log_path.mkdir(parents=True, exist_ok=True)
            # 日志格式
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            # 控制台handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
            # 文件handler
            log_file = log_path / f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            cls._loggers[name] = logger
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return logger
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def debug():
            """记录debug日志"""
            cls.get_logger(name).debug(message)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def info():
            """记录info日志"""
            cls.get_logger(name).info(message)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def warning():
            """记录warning日志"""
            cls.get_logger(name).warning(message)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def error():
            """记录error日志"""
            cls.get_logger(name).error(message)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def critical():
            """记录critical日志"""
            cls.get_logger(name).critical(message)
    # 日志装饰器
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def log_step():
        """
        步骤日志装饰器
        使用示例:
            # 【装饰器 @log_step】
            # 作用: 在不修改原函数的情况下，添加额外功能
            # 原理: 接收函数作为参数，返回新函数
            @log_step("输入用户名")
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def input_username():
                self.send_keys(self.USERNAME_INPUT, username)
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def decorator():
            # 【函数定义】
            # 语法: def 函数名(参数):
            # 作用: 封装可复用的代码块
            # 调用: 函数名(参数)
            def wrapper():
                logger = Logger.get_logger()
                logger.info(f"[步骤] {step_name}")
                # 【异常处理 try-except】
                # 语法: try: ... except 异常类型: ...
                # 作用: 捕获并处理可能发生的错误，防止程序崩溃
                try:
                    result = func(*args, **kwargs)
                    logger.info(f"[步骤] {step_name} - 成功")
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return result
                except Exception as e:
                    logger.error(f"[步骤] {step_name} - 失败: {e}")
                    raise
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return wrapper
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return decorator
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def log_test():
        """
        测试用例日志装饰器
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wrapper():
            logger = Logger.get_logger()
            test_name = test_func.__name__
            logger.info(f"{'='*60}")
            logger.info(f"[测试开始] {test_name}")
            logger.info(f"{'='*60}")
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                result = test_func(*args, **kwargs)
                logger.info(f"[测试通过] {test_name}")
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return result
            except Exception as e:
                logger.error(f"[测试失败] {test_name}: {e}")
                raise
            finally:
                logger.info(f"{'='*60}\n")
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return wrapper


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：Driver工厂"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：Driver工厂")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class DriverFactory:
        """
        WebDriver工厂类
        负责创建和管理Driver实例
        """
        _driver = None
        _config_reader = ConfigReader()
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_driver():
            """
            获取Driver实例 (单例模式)
            参数:
                platform: 平台 (android/ios)
                config_file: 配置文件名
            """
            if cls._driver is None:
                cls._driver = cls.create_driver(platform, config_file)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return cls._driver
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def create_driver():
            """
            创建新的Driver实例
            参数:
                platform: 平台 (android/ios)
                config_file: 配置文件名
            """
            # 读取配置
            caps = cls._config_reader.load(config_file)
            # 获取server URL
            server_url = cls._config_reader.get("config.yaml", "appium.server_url", 
                                                "http://localhost:4723/wd/hub")
            logger = Logger.get_logger()
            logger.info(f"创建Driver: platform={platform}, caps={caps}")
            # 实际项目中使用:
            # from appium import webdriver
            # driver = webdriver.Remote(server_url, caps)
            # 模拟driver
            driver = MockDriver(caps)
            # 设置隐式等待
            implicit_wait = cls._config_reader.get("config.yaml", "appium.implicit_wait", 10)
            driver.implicitly_wait(implicit_wait)
            logger.info("Driver创建成功")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return driver
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def quit_driver():
            """退出Driver"""
            if cls._driver:
                logger = Logger.get_logger()
                logger.info("退出Driver")
                cls._driver.quit()
                cls._driver = None
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def restart_driver():
            """重启Driver"""
            cls.quit_driver()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return cls.get_driver(platform, config_file)
    # 模拟Driver
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockDriver:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.caps = caps
            self.implicit_wait_time = 0
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def implicitly_wait():
            self.implicit_wait_time = seconds
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def quit():
            pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：基础页面对象 (带日志)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：基础页面对象 (带日志)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class BasePage:
        """
        基础页面类 (带日志)
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.driver = driver
            self.logger = Logger.get_logger("page")
        # 【装饰器 @log_step】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @log_step("查找元素")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_element():
            """查找元素"""
            by, value = locator
            self.logger.debug(f"查找元素: {by}={value}")
            # 实际: return self.driver.find_element(by, value)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value)
        # 【装饰器 @log_step】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @log_step("点击元素")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            """点击元素"""
            element = self.find_element(locator)
            element.click()
        # 【装饰器 @log_step】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @log_step("输入文本")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            """输入文本"""
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def take_screenshot():
            """截图"""
            if filename is None:
                filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            filepath = screenshot_dir / filename
            self.logger.info(f"截图保存到: {filepath}")
            # 实际: self.driver.get_screenshot_as_file(str(filepath))
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return str(filepath)
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
            pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """实战任务：搭建框架基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：搭建框架基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：搭建一个完整的测试框架基础
    要求:
    1. 创建配置文件 (config.yaml)
    2. 实现ConfigReader类
    3. 实现Logger类
    4. 实现DriverFactory类
    5. 实现带日志的BasePage
    """
    # 请完成下面的代码
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MyConfigReader:
        """
        自定义配置读取器
        要求:
        1. 支持读取YAML和JSON
        2. 支持环境变量覆盖配置
        3. 支持嵌套键访问 (如 "database.host")
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def load():
            """加载配置文件"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get():
            """获取配置值"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _apply_env_override():
            """应用环境变量覆盖"""
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
    class MyConfigReader:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.config_dir = Path(config_dir)
            self._configs = {}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def load():
            if filename in self._configs:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._configs[filename]
            file_path = self.config_dir / filename
            if not file_path.exists():
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise FileNotFoundError(f"配置文件不存在: {file_path}")
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(file_path, "r", encoding="utf-8") as f:
                if filename.endswith((".yaml", ".yml")):
                    config = yaml.safe_load(f)
                elif filename.endswith(".json"):
                    config = json.load(f)
                else:
                    # raise - 主动抛出异常
                    # 作用: 当遇到错误条件时，主动抛出异常
                    raise ValueError(f"不支持的格式: {filename}")
            # 应用环境变量覆盖
            config = self._apply_env_override(config)
            self._configs[filename] = config
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return config
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get():
            config = self.load(filename)
            if key is None:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return config
            keys = key.split(".")
            value = config
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return default
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return value
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _apply_env_override():
            if isinstance(config, dict):
                result = {}
                for key, value in config.items():
                    env_key = f"{prefix}_{key.upper()}" if prefix else key.upper()
                    if isinstance(value, (dict, list)):
                        result[key] = self._apply_env_override(value, env_key)
                    else:
                        env_value = os.getenv(env_key)
                        result[key] = env_value if env_value is not None else value
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return result
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return config
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
    1. 项目结构:
       - config/: 配置文件
       - pages/: 页面对象
       - tests/: 测试用例
       - utils/: 工具类
       - reports/: 测试报告
       - logs/: 日志文件
    2. 配置管理:
       - 支持YAML/JSON
       - 嵌套键访问
       - 环境变量覆盖
    3. 日志封装:
       - 统一日志格式
       - 文件+控制台输出
       - 日志装饰器
    4. Driver工厂:
       - 单例模式
       - 配置驱动
       - 自动管理生命周期
    验证标准：能搭建基础的自动化测试框架
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
        print("1. 第一部分：项目结构")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：配置管理")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：日志封装")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：Driver工厂")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：基础页面对象 (带日志)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务：搭建框架基础")
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
