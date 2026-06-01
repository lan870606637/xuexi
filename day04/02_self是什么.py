# -*- coding: utf-8 -*-
"""
02 - self 究竟是什么？

很多初学者卡在 self —— 觉得它"凭空冒出来"。
其实 self 只是一个普通参数，代表"调用这个方法的那个对象"。

记住这条等式：
    a.method(x)   ⇔   ClassName.method(a, x)
                                       ↑
                                       self 就是 a
"""

# ============================================================
# 1. 看清楚 self 是怎么传进来的
# ============================================================
class Counter:
    def __init__(self, start=0):
        # self 代表"正在创建的这个对象"
        # self.value = start  → 把 start 存到"这个对象"的 value 属性上
        self.value = start

    def add(self, n):
        # 调用 a.add(3) 时，self=a，所以这里实际是 a.value += 3
        self.value += n


a = Counter(10)
b = Counter(100)

a.add(3)     # 等价于 Counter.add(a, 3)
b.add(5)     # 等价于 Counter.add(b, 5)

print("a.value =", a.value)   # 13 —— 只改了 a
print("b.value =", b.value)   # 105 —— b 完全独立

# 验证一下"等价"：手动用类名调
Counter.add(a, 100)
print("再加 100 后, a.value =", a.value)   # 113


# ============================================================
# 2. 忘记 self 会怎样？
# ============================================================
class Bad:
    def __init__(self):
        value = 999       # ⚠ 漏写了 self.
                          # 这只是函数内的局部变量，函数一结束就销毁

bad = Bad()
# print(bad.value)        # 取消注释会报错: AttributeError
                          # 因为 Bad 对象上根本没有 value 这个属性

print("\nBad 对象有哪些属性?", vars(bad))   # 空字典 {}


# ============================================================
# 3. 方法内访问/修改对象自己的数据，全靠 self
# ============================================================
class TestCase:
    def __init__(self, name):
        self.name = name
        self.status = "pending"

    def run(self):
        # 这里要访问"这个用例自己"的 name 和 status，必须用 self
        print(f"执行 {self.name}（之前状态 {self.status}）")
        self.status = "running"


tc = TestCase("登录测试")
tc.run()
print("现在状态:", tc.status)


# ============================================================
# 总结
# ============================================================
# - self 是方法的第一个参数，Python 自动把"调用者"传进去
# - 想把数据"留在对象身上"，必须写 self.xxx = ...
# - 想以后访问/修改，也必须用 self.xxx
# - self 这个名字不是关键字，理论上可以改成 this、me，但全世界都用 self，别改
