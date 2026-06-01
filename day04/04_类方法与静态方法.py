# -*- coding: utf-8 -*-
"""
04 - 类方法 与 静态方法

方法分三种：
    普通方法     def f(self, ...)         第一个参数是"实例自己"
    类方法       @classmethod  def f(cls) 第一个参数是"类本身"
    静态方法     @staticmethod def f(...) 没有特殊参数，就是个普通函数，
                                          只是挂在类的命名空间里

90% 的方法都是普通方法，剩下两个只在特定场景用。
"""
import time


# ============================================================
# 1. 类方法 (@classmethod) —— 最经典用途：另一种"创建方式"
# ============================================================
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 一种"备用的构造方法"：从字符串解析出 User
    # cls 就是 User 这个类本身，cls(name, age) 等价于 User(name, age)
    # 之后即使类被改名或被继承，这里也自动跟着变
    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name.strip(), int(age))

    def __repr__(self):
        return f"User({self.name!r}, {self.age})"


u1 = User("Alice", 25)                       # 正常构造
u2 = User.from_string("Bob, 30")             # 用类方法构造
print(u1)
print(u2)


# ============================================================
# 2. 类方法的另一个用途：操作"类属性"
# ============================================================
class TestStats:
    total = 0
    passed = 0

    @classmethod
    def record_pass(cls):
        cls.total += 1
        cls.passed += 1

    @classmethod
    def record_fail(cls):
        cls.total += 1

    @classmethod
    def pass_rate(cls):
        if cls.total == 0:
            return 0
        return cls.passed / cls.total

    @classmethod
    def reset(cls):
        cls.total = 0
        cls.passed = 0


TestStats.record_pass()
TestStats.record_pass()
TestStats.record_fail()
print(f"\n通过率: {TestStats.pass_rate():.0%} （{TestStats.passed}/{TestStats.total}）")


# ============================================================
# 3. 静态方法 (@staticmethod) —— "工具函数，但语义上归这个类管"
# ============================================================
class StringUtils:

    @staticmethod
    def is_valid_email(s):
        # 跟实例和类都没关系，纯粹判断字符串
        return "@" in s and "." in s.split("@")[-1]

    @staticmethod
    def now_timestamp():
        return int(time.time())


# 不需要创建对象，直接用
print("\n邮箱有效?", StringUtils.is_valid_email("a@b.com"))   # True
print("邮箱有效?", StringUtils.is_valid_email("not-email"))    # False
print("现在时间戳:", StringUtils.now_timestamp())


# ============================================================
# 4. 三种方法对比
# ============================================================
class Demo:
    where = "class attribute"

    def normal(self, x):
        print(f"  normal  -> self={self}, x={x}")

    @classmethod
    def cls_method(cls, x):
        print(f"  classmd -> cls={cls.__name__}, x={x}")

    @staticmethod
    def static(x):
        print(f"  static  -> x={x}")


d = Demo()
print("\n--- 三种调用 ---")
d.normal(1)            # self 是 d
d.cls_method(2)        # cls 是 Demo
d.static(3)            # 完全不需要 d/Demo 的信息

Demo.cls_method(4)     # 类方法直接用类名调
Demo.static(5)         # 静态方法也是


# ============================================================
# 选择心法（用得最多 → 用得最少）：
#
#   def f(self, ...)                     90% 场景，操作"我这个对象"
#       └─ 比如 page.click(), case.run()
#
#   @classmethod def f(cls, ...)         10% 场景：
#       └─ 想写"另一种构造方式"（from_dict, from_file, ...）
#       └─ 想操作类级别的计数器/注册表
#
#   @staticmethod def f(...)             极少：
#       └─ 一个纯函数，但放在外面又显得散，逻辑上归这个类
# ============================================================
