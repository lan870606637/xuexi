# -*- coding: utf-8 -*-
"""
Day 13: Day 13
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：常用操作"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：常用操作")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Appium常用操作:
    - 点击 (click)
    - 输入文本 (send_keys)
    - 清空 (clear)
    - 获取文本 (text)
    - 获取属性 (get_attribute)
    - 检查显示/可用状态 (is_displayed/is_enabled)
    """
    # 模拟Appium操作 (同Day12)
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
            self._text = text
            self._displayed = True
            self._enabled = True
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def click():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  [操作] 点击元素")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def send_keys():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  [操作] 输入文本: '{text}'")
            self._text = text
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def clear():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  [操作] 清空输入框")
            self._text = ""
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
        def get_attribute():
            attrs = {
                "text": self._text,
                "enabled": str(self._enabled).lower(),
                "displayed": str(self._displayed).lower(),
                "resource-id": self.value if self.by == "id" else "",
                "class": "android.widget.EditText",
            }
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
            return self._displayed
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_enabled():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._enabled
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
            self.implicit_wait_time = 0
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[Driver] 创建会话: {capabilities.get('platformName')}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def quit():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[Driver] 关闭会话")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_element():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[查找] 元素: {by}={value}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockElement(by, value, f"Element({value})")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def find_elements():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[查找] 多个元素: {by}={value}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return [MockElement(by, value, f"Element1"), 
                    MockElement(by, value, f"Element2")]
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def implicitly_wait():
            self.implicit_wait_time = time_to_wait
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[设置] 隐式等待: {time_to_wait}秒")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_window_size():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {"width": 1080, "height": 1920}
        # 手势操作
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def tap():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[手势] 点击坐标: {positions}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def swipe():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[手势] 滑动: ({start_x},{start_y}) -> ({end_x},{end_y})")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def scroll():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[手势] 滚动: 从元素到元素")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def flick():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[手势] 快速滑动: ({start_x},{start_y}) -> ({end_x},{end_y})")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def long_press():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[手势] 长按元素: {duration}ms")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def drag_and_drop():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[手势] 拖拽: 从元素到元素")
        # 屏幕操作
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_screenshot_as_file():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[截图] 保存到: {filename}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_screenshot_as_base64():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "base64_encoded_image_data"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def save_screenshot():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[截图] 保存到: {filename}")
        # 按键操作
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def press_keycode():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[按键] 按下键码: {keycode}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def long_press_keycode():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[按键] 长按键码: {keycode}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def hide_keyboard():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[键盘] 隐藏键盘")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def is_keyboard_shown():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return False
        # 应用操作
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def launch_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[应用] 启动应用")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def close_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[应用] 关闭应用")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def reset():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("[应用] 重置应用")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def background_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[应用] 后台运行 {seconds} 秒")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def install_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[应用] 安装: {app_path}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def remove_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[应用] 卸载: {app_id}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def activate_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[应用] 激活: {app_id}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def terminate_app():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[应用] 终止: {app_id}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def query_app_state():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[应用] 查询状态: {app_id}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return 4  # RUNNING_IN_FOREGROUND
        # 上下文操作 (WebView)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def contexts():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ["NATIVE_APP", "WEBVIEW_com.example.app"]
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def current_context():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return "NATIVE_APP"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def switch_to():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[上下文] 切换到: {context}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：元素操作示例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：元素操作示例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_element_operations():
        """演示元素操作"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("元素操作示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
        }
        driver = MockAppiumDriver(caps)
        driver.implicitly_wait(10)
        # 1. 点击操作
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. 点击操作:")
        login_btn = driver.find_element("id", "login_button")
        login_btn.click()
        # 2. 输入操作
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. 输入操作:")
        username_input = driver.find_element("id", "username")
        username_input.clear()
        username_input.send_keys("admin")
        # 3. 获取元素信息
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n3. 获取元素信息:")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  文本: {username_input.text}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  是否显示: {username_input.is_displayed()}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  是否可用: {username_input.is_enabled()}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  resource-id: {username_input.get_attribute('resource-id')}")
        # 4. 查找多个元素
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n4. 查找多个元素:")
        items = driver.find_elements("class name", "android.widget.TextView")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  找到 {len(items)} 个元素")
        driver.quit()


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：手势操作"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：手势操作")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_gesture_operations():
        """演示手势操作"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("手势操作示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        caps = {"platformName": "Android", "deviceName": "emulator-5554"}
        driver = MockAppiumDriver(caps)
        # 获取屏幕尺寸
        size = driver.get_window_size()
        width = size["width"]
        height = size["height"]
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n屏幕尺寸: {width}x{height}")
        # 1. 点击坐标
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. 点击坐标:")
        driver.tap([(width/2, height/2)])
        # 2. 滑动操作
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. 滑动操作:")
        # 向上滑动 (从下到上)
        driver.swipe(width/2, height*0.8, width/2, height*0.2)
        # 向下滑动 (从上到下)
        driver.swipe(width/2, height*0.2, width/2, height*0.8)
        # 向左滑动
        driver.swipe(width*0.8, height/2, width*0.2, height/2)
        # 向右滑动
        driver.swipe(width*0.2, height/2, width*0.8, height/2)
        # 3. 长按
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n3. 长按操作:")
        element = driver.find_element("id", "item")
        driver.long_press(element, duration=2000)
        # 4. 拖拽
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n4. 拖拽操作:")
        source = driver.find_element("id", "source")
        target = driver.find_element("id", "target")
        driver.drag_and_drop(source, target)
        driver.quit()


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：等待机制"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：等待机制")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Appium等待机制:
    1. 隐式等待 (Implicit Wait)
       - 设置全局等待时间
       - 元素查找时自动等待
       - driver.implicitly_wait(10)
    2. 显式等待 (Explicit Wait)
       - 针对特定条件等待
       - 更灵活，推荐使用
    3. 睡眠等待 (Sleep)
       - 固定等待时间
       - 不推荐，除非必要
    """
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from selenium.webdriver.support.ui import WebDriverWait
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from selenium.webdriver.support import expected_conditions as EC
    # 显式等待示例 (需要真实环境)
    EXPLICIT_WAIT_EXAMPLE = '''
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from selenium.webdriver.support.ui import WebDriverWait
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from selenium.webdriver.support import expected_conditions as EC
    # 等待元素出现 (最长10秒)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("id", "login_button"))
    )
    # 等待元素可点击
    clickable = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(("id", "login_button"))
    )
    # 等待元素可见
    visible = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(("id", "welcome_message"))
    )
    # 等待文本出现
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(("id", "status"), "加载完成")
    )
    # 自定义等待条件
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def element_has_text():
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _predicate():
            # 【异常处理 try-except】
            # 语法: try: ... except 异常类型: ...
            # 作用: 捕获并处理可能发生的错误，防止程序崩溃
            try:
                element = driver.find_element(*locator)
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return text in element.text
            except:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return False
        # return - 返回值
        # 作用: 将结果返回给调用者，结束函数执行
        return _predicate
    WebDriverWait(driver, 10).until(
        element_has_text(("id", "result"), "成功")
    )
    '''
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n显式等待示例代码已准备")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：Android特有操作"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：Android特有操作")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    Android特有操作:
    """
    ANDROID_OPERATIONS = """
    【按键操作】
    # Android按键码
    KEYCODE_HOME = 3
    KEYCODE_BACK = 4
    KEYCODE_CALL = 5
    KEYCODE_ENDCALL = 6
    KEYCODE_VOLUME_UP = 24
    KEYCODE_VOLUME_DOWN = 25
    KEYCODE_POWER = 26
    KEYCODE_CAMERA = 27
    KEYCODE_MENU = 82
    KEYCODE_NOTIFICATION = 83
    # 使用示例
    driver.press_keycode(4)  # 返回键
    driver.press_keycode(3)  # Home键
    【Toast消息】
    # 获取Toast消息 (Android)
    toast = driver.find_element("xpath", "//android.widget.Toast")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(toast.text)
    【通知栏】
    # 打开通知栏
    driver.open_notifications()
    【网络状态】
    # 获取网络连接状态
    network = driver.network_connection
    # 设置网络连接
    # 0: 无网络, 1: 飞行模式, 2: 仅WiFi, 4: 仅数据, 6: 全部
    driver.set_network_connection(6)
    【输入法】
    # 切换输入法
    driver.available_ime_engines
    driver.activate_ime_engine(engine)
    driver.deactivate_ime_engine()
    【ADB命令】
    # 执行ADB shell命令 (UiAutomator2支持)
    result = driver.execute_script('mobile: shell', {
        'command': 'pm list packages',
        'args': [],
        'includeStderr': True,
        'timeout': 5000
    })
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(ANDROID_OPERATIONS)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：iOS特有操作"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：iOS特有操作")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    iOS特有操作:
    """
    IOS_OPERATIONS = """
    【TouchAction】
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from appium.webdriver.common.touch_action import TouchAction
    # 点击
    TouchAction(driver).tap(element).perform()
    # 长按
    TouchAction(driver).long_press(element).wait(2000).release().perform()
    # 滑动
    TouchAction(driver).press(x=100, y=200).move_to(x=100, y=400).release().perform()
    # 多点触控
    finger1 = TouchAction(driver).tap(x=100, y=100)
    finger2 = TouchAction(driver).tap(x=200, y=200)
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from appium.webdriver.common.multi_action import MultiAction
    MultiAction(driver).add(finger1, finger2).perform()
    【iOS手势】
    # 滚动
    driver.execute_script('mobile: scroll', {
        'direction': 'down',
        'element': element.id
    })
    # 滑动
    driver.execute_script('mobile: swipe', {
        'direction': 'left',
        'element': element.id
    })
    # 捏合缩放
    driver.execute_script('mobile: pinch', {
        'scale': 0.5,  # <1缩小, >1放大
        'velocity': 1.0,
        'element': element.id
    })
    【Biometric认证】
    # 启用/禁用生物识别
    driver.toggle_touch_id_enrollment()
    # 模拟Touch ID匹配
    driver.perform_touch_id(True)   # 成功
    driver.perform_touch_id(False)  # 失败
    【Shake】
    # 模拟摇一摇
    driver.shake()
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(IOS_OPERATIONS)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """实战任务：编写Appium测试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：编写Appium测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：编写一个完整的登录测试流程
    """
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_login_flow():
        """
        登录测试流程
        步骤:
        1. 等待并输入用户名
        2. 输入密码
        3. 点击登录按钮
        4. 验证登录成功
        参数:
            driver: Appium WebDriver实例
        """
        # 你的代码写在这里
        # 提示：
        # 1. 使用find_element查找元素
        # 2. 使用send_keys输入文本
        # 3. 使用click点击按钮
        # 4. 使用断言验证结果
        pass
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_swipe_to_refresh():
        """
        下拉刷新测试
        步骤:
        1. 获取屏幕尺寸
        2. 从屏幕顶部向下滑动
        3. 等待刷新完成
        参数:
            driver: Appium WebDriver实例
        """
        # 你的代码写在这里
        pass
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_long_press_menu():
        """
        长按显示菜单测试
        步骤:
        1. 找到列表项元素
        2. 长按该元素
        3. 验证菜单出现
        参数:
            driver: Appium WebDriver实例
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
    def test_login_flow():
        # 1. 输入用户名
        username_input = driver.find_element("id", "com.example:id/username")
        username_input.clear()
        username_input.send_keys("admin")
        # 2. 输入密码
        password_input = driver.find_element("id", "com.example:id/password")
        password_input.clear()
        password_input.send_keys("123456")
        # 3. 点击登录
        login_btn = driver.find_element("id", "com.example:id/login_button")
        login_btn.click()
        # 4. 验证登录成功
        welcome_msg = driver.find_element("id", "com.example:id/welcome_message")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert "欢迎" in welcome_msg.text
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_swipe_to_refresh():
        # 获取屏幕尺寸
        size = driver.get_window_size()
        width = size["width"]
        height = size["height"]
        # 从顶部向下滑动 (下拉刷新)
        driver.swipe(width/2, height*0.2, width/2, height*0.8)
        # 等待刷新指示器消失
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import time
        time.sleep(2)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def test_long_press_menu():
        # 找到列表项
        item = driver.find_element("xpath", "//android.widget.ListView/android.view.ViewGroup[1]")
        # 长按
        driver.long_press(item, duration=2000)
        # 验证菜单出现
        menu = driver.find_element("id", "com.example:id/context_menu")
        # assert - 断言
        # 语法: assert 条件, 错误信息
        # 作用: 条件为False时抛出AssertionError
        assert menu.is_displayed()
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
    1. 元素操作:
       - click(), send_keys(), clear()
       - text, get_attribute()
       - is_displayed(), is_enabled()
    2. 手势操作:
       - tap(): 点击坐标
       - swipe(): 滑动
       - long_press(): 长按
       - drag_and_drop(): 拖拽
       - scroll(): 滚动
    3. 等待机制:
       - implicitly_wait(): 隐式等待
       - WebDriverWait: 显式等待
       - expected_conditions: 预期条件
    4. 应用操作:
       - launch_app(), close_app()
       - background_app(), activate_app()
       - install_app(), remove_app()
    5. 平台特有:
       - Android: press_keycode(), open_notifications()
       - iOS: TouchAction, biometric认证
    验证标准：能在模拟器上打开App并执行操作
    """
    # 运行演示
    if __name__ == "__main__":
        demo_element_operations()
        demo_gesture_operations()

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section10():
    """第十部分：显式等待深入（补充）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第十部分：显式等待深入（补充）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # ---- 1. 三种等待方式对比 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. 三种等待方式对比:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    ┌──────────────┬────────────────────────────────────────┐
    │ 等待方式      │ 说明                                   │
    ├──────────────┼────────────────────────────────────────┤
    │ time.sleep() │ 强制等待，固定时间，不推荐               │
    │ 隐式等待      │ 全局设置，对所有find_element生效         │
    │ 显式等待      │ 针对特定条件等待，最灵活，推荐使用        │
    └──────────────┴────────────────────────────────────────┘

    # 隐式等待 (全局设置一次)
    driver.implicitly_wait(10)  # 最多等10秒

    # 显式等待 (针对特定元素/条件)
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    wait = WebDriverWait(driver, 10, poll_frequency=0.5)
    # driver: 浏览器/App驱动
    # 10: 最长等待时间(秒)
    # poll_frequency: 轮询间隔(秒)，默认0.5
    """)

    # ---- 2. Expected Conditions详解 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. Expected Conditions常用条件:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    from selenium.webdriver.support import expected_conditions as EC

    # ---- 元素存在/可见 ----
    # 等待元素出现在DOM中 (不一定可见)
    EC.presence_of_element_located((By.ID, 'login_btn'))

    # 等待元素可见 (出现在DOM中且可见)
    EC.visibility_of_element_located((By.ID, 'login_btn'))

    # 等待元素不可见
    EC.invisibility_of_element_located((By.ID, 'loading'))

    # ---- 元素可交互 ----
    # 等待元素可点击 (可见且enabled)
    EC.element_to_be_clickable((By.ID, 'submit_btn'))

    # ---- 文本相关 ----
    # 等待元素包含指定文本
    EC.text_to_be_present_in_element((By.ID, 'status'), '成功')

    # ---- 多个元素 ----
    # 等待至少一个元素出现
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'item'))

    # ---- 其他条件 ----
    # 等待页面标题包含
    EC.title_contains('首页')

    # 等待Alert弹窗出现
    EC.alert_is_present()
    """)

    # ---- 3. 实际使用示例 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("3. 实际使用示例:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    wait = WebDriverWait(driver, 10)

    # 示例1: 等待登录按钮可点击后再点击
    login_btn = wait.until(
        EC.element_to_be_clickable((By.ID, 'com.app:id/login'))
    )
    login_btn.click()

    # 示例2: 等待加载动画消失
    wait.until(
        EC.invisibility_of_element_located((By.ID, 'loading_spinner'))
    )

    # 示例3: 等待Toast提示出现
    toast = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//android.widget.Toast')
        )
    )
    print(f'Toast内容: {toast.text}')

    # 示例4: 等待列表加载完成
    items = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'android.widget.TextView')
        )
    )
    print(f'找到 {len(items)} 个元素')
    """)

    # ---- 4. 自定义等待条件 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. 自定义等待条件:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    # 当内置条件不满足需求时，可以自定义:

    # 方式1: 使用lambda
    wait.until(lambda d: d.find_element(By.ID, 'list').text != '加载中...')

    # 方式2: 定义函数
    def element_has_text(locator, text):
        def _predicate(driver):
            try:
                element = driver.find_element(*locator)
                return text in element.text
            except:
                return False
        return _predicate

    wait.until(element_has_text((By.ID, 'status'), '完成'))

    # 方式3: 定义类 (更正式)
    class ElementCountGreaterThan:
        '''等待元素数量大于指定值'''
        def __init__(self, locator, count):
            self.locator = locator
            self.count = count

        def __call__(self, driver):
            elements = driver.find_elements(*self.locator)
            return len(elements) > self.count

    # 等待列表元素超过5个
    wait.until(ElementCountGreaterThan((By.CLASS_NAME, 'item'), 5))
    """)

    # ---- 5. BasePage中封装等待 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("5. 在BasePage中封装等待 (最佳实践):")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    class BasePage:
        def __init__(self, driver, timeout=10):
            self.driver = driver
            self.wait = WebDriverWait(driver, timeout)

        def wait_for_visible(self, locator):
            '''等待元素可见'''
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )

        def wait_for_clickable(self, locator):
            '''等待元素可点击'''
            return self.wait.until(
                EC.element_to_be_clickable(locator)
            )

        def wait_for_invisible(self, locator):
            '''等待元素消失 (如loading)'''
            return self.wait.until(
                EC.invisibility_of_element_located(locator)
            )

        def safe_click(self, locator):
            '''安全点击: 先等待可点击再点击'''
            element = self.wait_for_clickable(locator)
            element.click()

        def safe_input(self, locator, text):
            '''安全输入: 先等待可见再输入'''
            element = self.wait_for_visible(locator)
            element.clear()
            element.send_keys(text)

    常见坑:
    - 隐式等待和显式等待不要混用，可能导致等待时间不可预期
    - TimeoutException不要吞掉，要让测试明确失败
    - poll_frequency不要设太小 (如0.01)，会浪费CPU
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
        print("1. 第一部分：常用操作")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：元素操作示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：手势操作")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：等待机制")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：Android特有操作")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：iOS特有操作")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 实战任务：编写Appium测试")
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
        print("10. 补充：显式等待深入")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("11. 实战任务")
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
        elif choice == "11":
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
