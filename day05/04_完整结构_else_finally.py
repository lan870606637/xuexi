# -*- coding: utf-8 -*-
"""
04 - 完整结构：try / except / else / finally

完整四件套：

    try:
        可能出错的代码
    except 异常类型:
        出错时执行
    else:
        没出错时执行       （可省略）
    finally:
        不管有没有错都执行  （可省略）
"""

# ============================================================
# 1. else 块：只在 try 没抛异常时执行
# ============================================================
def safe_div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  ✗ {a}/{b} 失败：除以零")
        return None
    else:
        # 只有 try 顺利跑完，才会进 else
        # 用途：把"成功后才该做的事"放这里，跟"可能出错的代码"分开
        print(f"  ✓ {a}/{b} = {result}")
        return result


print("--- else 演示 ---")
safe_div(10, 2)
safe_div(10, 0)


# ============================================================
# 2. finally 块：无论成功失败，一定执行
# ============================================================
# 最经典用途：清理资源（关文件、断开连接、释放锁）
def read_file(path):
    f = None
    try:
        f = open(path, "r")
        return f.read()
    except FileNotFoundError:
        print(f"  ✗ 文件不存在: {path}")
        return ""
    finally:
        # 无论上面 return 没 return、有没有异常，
        # 这一段一定会执行 —— 保证文件被关上
        if f is not None:
            f.close()
            print(f"  ✓ 文件已关闭: {path}")


print("\n--- finally 演示 ---")
read_file("/tmp/不存在.txt")          # 走 except，finally 仍执行
# read_file(__file__)                # 走正常分支，finally 也执行


# ============================================================
# 3. 四件套放一起 —— 经典模板
# ============================================================
def divide_demo(a, b):
    print(f"\n[计算] {a} / {b}")
    try:
        result = a / b
    except ZeroDivisionError:
        print("  [except] 除以零")
        return None
    except TypeError:
        print("  [except] 类型错误")
        return None
    else:
        print(f"  [else]   成功 = {result}")
        return result
    finally:
        print("  [finally] 计算流程结束")
        # 注意：finally 在 return 之前执行，但不会影响返回值


divide_demo(10, 2)       # 走 else + finally
divide_demo(10, 0)       # 走 except + finally
divide_demo("a", 2)      # 走 TypeError + finally


# ============================================================
# 4. finally 的"杀手级"用法 —— 测试用例的清理动作
# ============================================================
def run_test():
    print("\n[测试用例]")
    # 假装这是 Appium driver / WebDriver
    driver = "<driver>"
    print("  setUp: 启动浏览器")
    try:
        print("  step1: 打开页面")
        print("  step2: 点击登录按钮")
        # 模拟一个失败
        raise AssertionError("断言失败：未跳转到首页")
        print("  step3: 这一行不会执行")
    except AssertionError as e:
        print(f"  ✗ 用例失败: {e}")
    finally:
        # ↓↓↓ 这里是关键！无论成功失败，driver 都要关
        # 没有 finally，失败时 driver 不关，下条用例就乱套了
        print(f"  tearDown: 关闭 {driver}")


run_test()


# ============================================================
# 注意一个小细节
# ------------------------------------------------------------
# 为什么不能把"成功才做的事"直接放在 try 里？
#
#   try:
#       data = api.call()
#       process(data)           ← 如果 process 也炸了，except 会把它当作 api 的错
#   except SomeError:
#       ...
#
# 用 else 就清晰：
#
#   try:
#       data = api.call()       ← try 只包"会出 SomeError 的那一行"
#   except SomeError:
#       ...
#   else:
#       process(data)           ← 成功之后才该做的事
# ============================================================
