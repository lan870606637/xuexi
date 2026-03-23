# -*- coding: utf-8 -*-
"""
Day 12: Day 12
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：Appium简介"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：Appium简介")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Appium是什么？
    - 开源的移动应用自动化测试框架
    - 支持iOS、Android、Windows应用
    - 使用WebDriver协议
    - 支持原生应用、混合应用、Web应用
    Appium架构:
    +----------------+     +----------------+     +----------------+
    |   测试脚本      | --> |  Appium Server | --> |    移动设备     |
    | (Python/Java)  |     |   (HTTP服务)    |     | (iOS/Android) |
    +----------------+     +----------------+     +----------------+
    环境搭建步骤:
    1. 安装Node.js
    2. 安装Appium: npm install -g appium
    3. 安装Appium Doctor: npm install -g appium-doctor
    4. 检查环境: appium-doctor
    5. 安装Python客户端: pip install Appium-Python-Client
    6. 安装Android SDK (测试Android)
    7. 安装Xcode (测试iOS)
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：Desired Capabilities"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：Desired Capabilities")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Desired Capabilities是告诉Appium如何启动应用的配置参数
    """
    # Android配置示例
    android_caps = {
        # 平台相关
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "emulator-5554",
        # 应用相关
        "appPackage": "com.example.app",
        "appActivity": ".MainActivity",
        # 自动化引擎
        "automationName": "UiAutomator2",
        # 其他选项
        "noReset": False,  # 是否重置应用状态
        "fullReset": False,  # 是否完全重置
        "newCommandTimeout": 300,  # 新命令超时时间(秒)
        "autoGrantPermissions": True,  # 自动授予权限
    }
    # iOS配置示例
    ios_caps = {
        "platformName": "iOS",
        "platformVersion": "15.0",
        "deviceName": "iPhone 13",
        "udid": "auto",  # 自动检测设备
        # 应用相关
        "bundleId": "com.example.app",
        # 或者使用app路径
        # "app": "/path/to/app.app",
        # 自动化引擎
        "automationName": "XCUITest",
        # Xcode相关
        "xcodeOrgId": "<Team ID>",
        "xcodeSigningId": "iPhone Developer",
    }
    # 使用已有应用(不重新安装)
    existing_app_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2",
        "noReset": True,  # 不重置应用状态
    }


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：常用Capabilities详解"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：常用Capabilities详解")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    CAPABILITIES_DOC = """
    常用Capabilities:
    【平台相关】
    - platformName: 平台名称 (Android/iOS)
    - platformVersion: 系统版本
    - deviceName: 设备名称
    - udid: 设备唯一标识
    【应用相关】
    - app: app文件路径 (绝对路径)
    - appPackage: Android应用包名
    - appActivity: Android启动Activity
    - bundleId: iOS应用bundle ID
    【自动化引擎】
    - automationName: 
      - Android: UiAutomator2 (推荐) / Espresso
      - iOS: XCUITest
    【会话相关】
    - noReset: 不重置应用状态 (保留登录等)
    - fullReset: 完全重置 (卸载重装)
    - newCommandTimeout: 新命令超时时间
    - autoLaunch: 是否自动启动应用
    【Android特有】
    - appWaitPackage: 等待的包名
    - appWaitActivity: 等待的Activity
    - autoGrantPermissions: 自动授予权限
    - unicodeKeyboard: 使用Unicode键盘
    - resetKeyboard: 重置键盘
    - chromedriverExecutable: ChromeDriver路径 (WebView)
    【iOS特有】
    - xcodeOrgId: Apple Developer Team ID
    - xcodeSigningId: 签名ID
    - updatedWDABundleId: WebDriverAgent bundle ID
    - usePrebuiltWDA: 使用预构建的WDA
    - derivedDataPath: WDA构建路径
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(CAPABILITIES_DOC)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：连接设备"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：连接设备")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    连接设备的步骤:
    1. 启动Appium Server
       appium
       或指定参数:
       appium --address 127.0.0.1 --port 4723
    2. 检查设备连接
       Android: adb devices
       iOS: xcrun simctl list devices
    3. 获取应用信息
       Android:
       - 获取包名: adb shell pm list packages
       - 获取Activity: adb shell dumpsys package <package_name> | grep Activity
       iOS:
       - 使用Xcode查看bundle ID
    4. 编写测试脚本连接
    """
    # 连接示例代码 (需要真实环境才能运行)
    CONNECTION_EXAMPLE = '''
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from appium import webdriver
    # 配置
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2",
    }
    # 连接Appium Server
    driver = webdriver.Remote(
        command_executor="http://localhost:4723/wd/hub",
        desired_capabilities=caps
    )
    # 现在可以操作应用了
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("应用已启动")
    # 关闭会话
    driver.quit()
    '''
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n连接示例代码已准备")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：模拟操作代码"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：模拟操作代码")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    由于实际运行需要Appium环境，这里提供模拟代码供学习
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockAppiumDriver:
        """模拟Appium Driver"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.caps = capabilities
            self.session_id = "mock_session_123"
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 创建会话: {capabilities.get('platformName')}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def quit():
            """关闭会话"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Mock] 关闭会话")
        # 元素查找
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_element():
            """查找单个元素"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 查找元素: {by}={value}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_elements():
            """查找多个元素"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 查找多个元素: {by}={value}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return [MockElement(by, value)]
        # 操作
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            """点击"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 点击元素")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            """输入文本"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 输入: {text}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def clear():
            """清空输入框"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 清空输入框")
        # 手势
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def swipe():
            """滑动"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 滑动: ({start_x},{start_y}) -> ({end_x},{end_y})")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def tap():
            """点击坐标"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 点击坐标: {positions}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def long_press():
            """长按"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 长按元素 {duration}ms")
        # 屏幕操作
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_screenshot_as_file():
            """截图"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 截图保存到: {filename}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_window_size():
            """获取屏幕尺寸"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"width": 1080, "height": 1920}
        # 等待
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def implicitly_wait():
            """隐式等待"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 设置隐式等待: {time_to_wait}s")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def wait_for_element():
            """显式等待元素"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 等待元素: {by}={value}, 超时: {timeout}s")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value)
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
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 元素点击")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 元素输入: {text}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def clear():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Mock] 元素清空")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_attribute():
            attrs = {"text": "示例文本", "enabled": "true", "displayed": "true"}
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return attrs.get(name, "")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_displayed():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return True
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_enabled():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return True


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：元素定位策略"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：元素定位策略")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Appium元素定位策略:
    1. ID (推荐)
       driver.find_element("id", "com.example:id/username")
    2. XPath
       driver.find_element("xpath", "//android.widget.EditText[@resource-id='com.example:id/username']")
    3. Accessibility ID (推荐)
       driver.find_element("accessibility id", "username_input")
    4. Class Name
       driver.find_element("class name", "android.widget.EditText")
    5. Android UIAutomator (Android特有)
       driver.find_element("-android uiautomator", 'new UiSelector().resourceId("com.example:id/username")')
    6. iOS Predicate (iOS特有)
       driver.find_element("-ios predicate string", "type == 'XCUIElementTypeTextField'")
    7. CSS Selector (WebView)
       driver.find_element("css selector", "#username")
    """
    LOCATOR_EXAMPLES = {
        "id": ("id", "com.example.app:id/login_button"),
        "xpath": ("xpath", "//android.widget.Button[@text='登录']"),
        "accessibility_id": ("accessibility id", "login_button"),
        "class_name": ("class name", "android.widget.Button"),
        "android_uiautomator": ("-android uiautomator", 'new UiSelector().text("登录")'),
    }
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demonstrate_locators():
        """演示元素定位"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n元素定位示例:")
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.app",
            "appActivity": ".MainActivity",
            "automationName": "UiAutomator2",
        }
        driver = MockAppiumDriver(caps)
        # 各种定位方式
        for name, locator in LOCATOR_EXAMPLES.items():
            by, value = locator
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"\n{name}: {locator}")
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                element = driver.find_element(by, value)
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"  找到元素: {element}")
            except Exception as e:
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"  错误: {e}")
        driver.quit()
    # 运行演示
    if __name__ == "__main__":
        demonstrate_locators()


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """实战任务：编写Capabilities配置"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：编写Capabilities配置")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为以下场景编写合适的Desired Capabilities
    """
    # 场景1: 在Android模拟器上测试已有应用(设置应用)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def get_android_settings_caps():
        """
        返回Android设置应用的Capabilities
        要求:
        - 使用Android平台
        - 使用UiAutomator2引擎
        - 不重置应用状态
        """
        # 你的代码写在这里
        pass
    # 场景2: 在iOS模拟器上测试新应用
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def get_ios_app_caps():
        """
        返回iOS应用的Capabilities
        参数:
            app_path: app文件路径
        要求:
        - 使用iOS平台
        - 使用XCUITest引擎
        - 自动接受权限
        """
        # 你的代码写在这里
        pass
    # 场景3: 在真机上测试Android应用
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def get_android_real_device_caps():
        """
        返回Android真机测试的Capabilities
        参数:
            udid: 设备udid
            app_path: apk文件路径
        要求:
        - 指定udid
        - 安装并启动应用
        - 自动授予权限
        """
        # 你的代码写在这里
        pass


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
    def get_android_settings_caps():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "automationName": "UiAutomator2",
            "noReset": True,
        }
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def get_ios_app_caps():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return {
            "platformName": "iOS",
            "platformVersion": "15.0",
            "deviceName": "iPhone 13",
            "app": app_path,
            "automationName": "XCUITest",
            "autoAcceptAlerts": True,
        }
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def get_android_real_device_caps():
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return {
            "platformName": "Android",
            "udid": udid,
            "app": app_path,
            "automationName": "UiAutomator2",
            "autoGrantPermissions": True,
            "noReset": False,
        }
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
    1. Appium简介:
       - 跨平台移动自动化框架
       - 基于WebDriver协议
       - 支持原生/混合/Web应用
    2. 环境搭建:
       - 安装Node.js和Appium
       - 安装Appium-Python-Client
       - 配置Android SDK / Xcode
    3. Desired Capabilities:
       - platformName, platformVersion, deviceName
       - appPackage, appActivity (Android)
       - bundleId (iOS)
       - automationName
       - noReset, fullReset
    4. 元素定位:
       - ID (推荐)
       - XPath
       - Accessibility ID (推荐)
       - Class Name
       - UIAutomator (Android)
       - Predicate (iOS)
    验证标准：能写出正确的Desired Capabilities配置
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
        print("1. 第一部分：Appium简介")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：Desired Capabilities")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：常用Capabilities详解")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：连接设备")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：模拟操作代码")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：元素定位策略")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 实战任务：编写Capabilities配置")
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
