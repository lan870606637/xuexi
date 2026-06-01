# -*- coding: utf-8 -*-
"""
06 - 多态（Polymorphism）

一句话：只要"长得一样"（有相同的方法名），就可以被同样的方式使用，
        不需要它们继承同一个父类。

Python 里这叫"鸭子类型"：
    如果它走起来像鸭子、叫起来像鸭子，那它就是鸭子。
"""


# ============================================================
# 1. 经典场景：同一段测试代码，跑不同的浏览器
# ============================================================
class ChromeDriver:
    def get(self, url):
        print(f"[Chrome]  打开 {url}")

class FirefoxDriver:
    def get(self, url):
        print(f"[Firefox] 打开 {url}")

class SafariDriver:
    def get(self, url):
        print(f"[Safari]  打开 {url}")


# 这个函数不关心你传什么类型，只关心："你有没有 .get() 方法？"
def open_homepage(driver):
    driver.get("https://example.com")


for d in [ChromeDriver(), FirefoxDriver(), SafariDriver()]:
    open_homepage(d)


# ============================================================
# 2. 同样的思路 —— 不同断言策略
# ============================================================
class EqualAssert:
    def check(self, actual, expected):
        return actual == expected

class ContainsAssert:
    def check(self, actual, expected):
        return expected in actual

class RegexAssert:
    import re
    def check(self, actual, pattern):
        import re
        return re.search(pattern, actual) is not None


# 测试框架不关心你用哪种策略，只调 .check() 就行
def run_check(strategy, actual, expected):
    result = "PASS" if strategy.check(actual, expected) else "FAIL"
    print(f"{strategy.__class__.__name__:20s} -> {result}")


print()
run_check(EqualAssert(),    "Hello World", "Hello World")
run_check(ContainsAssert(), "Hello World", "World")
run_check(RegexAssert(),    "Hello 123",   r"\d+")


# ============================================================
# 3. 多态 vs 继承 —— 它们是两个独立概念
# ============================================================
# 上面三个 Driver 类、三个 Assert 类，都没有共同父类，
# 但它们能"被同样方式使用"，这就是多态。
#
# 当然，用继承也能实现多态（推荐做法），因为有父类约束：
class Animal:
    def speak(self):
        raise NotImplementedError("子类必须实现 speak()")

class Dog(Animal):
    def speak(self): print("Woof!")

class Cat(Animal):
    def speak(self): print("Meow!")


print()
for a in [Dog(), Cat()]:
    a.speak()         # 调用相同方法，行为不同 = 多态


# ============================================================
# 一句话总结：
#   多态 = "我不在乎你是谁，只要你能做我要的事"
#   测试框架里到处都是多态：换 driver、换断言、换报告器、换数据源
# ============================================================
