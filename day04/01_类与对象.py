# -*- coding: utf-8 -*-
"""
01 - 类与对象

要回答的问题：
  1. 什么是"类"？什么是"对象"？
  2. 为什么不直接用字典/函数，要专门搞个类出来？

一句话：类是"图纸"，对象是按图纸造出来的"实物"。
"""

# ============================================================
# 先看一段"难受"的代码 —— 不用类
# ============================================================
# 用字典管理测试用例，每次都要重复一堆字段，
# 字段名打错运行时才发现，也没法给"所有用例"统一加一个行为。
case1 = {"name": "登录", "priority": "high", "status": "pending"}
case2 = {"name": "注册", "priority": "low",  "status": "pending"}

# 给用例做点什么，只能写散乱的全局函数
def run_case(case):
    print(f"执行 {case['name']}")
    case["status"] = "running"

run_case(case1)
print(case1)


# ============================================================
# 用类重写：数据 + 行为绑在一起
# ============================================================
class TestCase:
    """一个测试用例"""

    # __init__ 是"创建对象时"自动调用的特殊方法（构造方法）
    # 把外部传入的 name / priority 存到 self 上 —— self 下一节专门讲
    def __init__(self, name, priority="normal"):
        self.name = name
        self.priority = priority
        self.status = "pending"   # 默认状态

    # 用例可以做的动作，写成挂在类里的函数（方法）
    def run(self):
        print(f"▶ 执行: {self.name}")
        self.status = "running"

    def mark_passed(self):
        self.status = "passed"
        print(f"✓ {self.name} 通过")

    def mark_failed(self, reason):
        self.status = "failed"
        self.failure_reason = reason
        print(f"✗ {self.name} 失败：{reason}")


# ============================================================
# 使用：一行创建对象，一行调用方法
# ============================================================
print("\n--- 创建对象 ---")
tc1 = TestCase("登录测试", "high")    # 这一行触发 __init__
tc2 = TestCase("注册测试")            # priority 用默认值 "normal"

print(tc1.name, tc1.priority, tc1.status)
print(tc2.name, tc2.priority, tc2.status)

print("\n--- 调用方法 ---")
tc1.run()
tc1.mark_passed()

tc2.run()
tc2.mark_failed("元素未找到")

print("\n--- 最终状态 ---")
print(f"{tc1.name}: {tc1.status}")
print(f"{tc2.name}: {tc2.status}（原因：{tc2.failure_reason}）")


# ============================================================
# 体会一下：
#   - 字典版本的 case1["status"] = "passed" 散落在到处
#   - 类版本的 tc1.mark_passed() 集中在 TestCase 一个地方
#   - 想加新行为？只在 TestCase 里加个方法，所有用例都获得
# ============================================================
