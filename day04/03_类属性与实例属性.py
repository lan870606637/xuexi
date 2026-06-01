# -*- coding: utf-8 -*-
"""
03 - 类属性 vs 实例属性

实例属性：每个对象一份，写法是 self.xxx = ...
类属性：  所有对象共享一份，写在 class 块里、不带 self
"""

# ============================================================
# 1. 一个最直观的对比
# ============================================================
class TestRun:
    # 类属性 —— 所有 TestRun 对象共享同一个 total_count
    total_count = 0

    def __init__(self, name):
        self.name = name                  # 实例属性：每个对象独立
        TestRun.total_count += 1          # 修改类属性，所有人都受影响
        self.id = TestRun.total_count     # 顺手给自己一个 id


t1 = TestRun("登录")
t2 = TestRun("注册")
t3 = TestRun("下单")

# 实例属性：各管各的
print("名字:", t1.name, t2.name, t3.name)
print("id:", t1.id, t2.id, t3.id)

# 类属性：所有实例都能读，值一样
print("一共创建了:", TestRun.total_count)
print("从实例也能读:", t1.total_count, "/", t2.total_count, "/", t3.total_count)


# ============================================================
# 2. 类属性最常见的两个用途
# ============================================================
# 用途 A：常量配置 —— 不会变的"这一类对象都该有的设定"
class HttpClient:
    DEFAULT_TIMEOUT = 30          # 所有 client 默认超时 30s
    BASE_URL = "https://api.test.com"


print("\n默认超时:", HttpClient.DEFAULT_TIMEOUT)
print("base url:", HttpClient.BASE_URL)


# 用途 B：计数器/注册表 —— 跟踪"一共创建了多少"
class Spider:
    instances = []                # 类属性：一个列表，记录所有实例

    def __init__(self, url):
        self.url = url
        Spider.instances.append(self)   # 每创建一个就登记进去


Spider("https://a.com")
Spider("https://b.com")
Spider("https://c.com")
print("\n创建过的爬虫数:", len(Spider.instances))
print("所有 url:", [s.url for s in Spider.instances])


# ============================================================
# 3. ⚠️ 必须知道的坑：实例赋值会"屏蔽"类属性
# ============================================================
class Config:
    timeout = 10        # 类属性


c1 = Config()
c2 = Config()

print("\n--- 初始 ---")
print("c1.timeout:", c1.timeout, "c2.timeout:", c2.timeout, "Config.timeout:", Config.timeout)

# 通过实例赋值，看起来像在改类属性，其实是在 c1 上**新增**了一个实例属性
c1.timeout = 999

print("\n--- c1.timeout = 999 之后 ---")
print("c1.timeout:", c1.timeout)            # 999 （读到的是新建的实例属性）
print("c2.timeout:", c2.timeout)            # 10  （类属性完全没动）
print("Config.timeout:", Config.timeout)    # 10

# 真要改类属性，得通过类名
Config.timeout = 60
print("\n--- Config.timeout = 60 之后 ---")
print("c1.timeout:", c1.timeout)            # 999（实例属性还在，盖住了类属性）
print("c2.timeout:", c2.timeout)            # 60 （没盖住，读到了新的类属性）


# ============================================================
# 4. 还有一个更坑的：可变类属性（列表/字典）
# ============================================================
# 如果类属性是一个 list，所有实例共享同一个 list！
# 这通常是 bug，新手非常容易写错。
class Wrong:
    tags = []     # 想给"每个对象一个 tags 列表"，但这样写不行

    def add_tag(self, t):
        self.tags.append(t)   # 修改的是同一个列表


a = Wrong()
b = Wrong()
a.add_tag("p1")
b.add_tag("p2")
print("\nWrong:", a.tags, b.tags)   # 两个都是 ['p1', 'p2'] —— 一个列表被两人改


# 正确做法：把"每个对象独立"的东西，放到 __init__ 里
class Right:
    def __init__(self):
        self.tags = []        # 每次创建对象都 new 一个新列表


a = Right(); b = Right()
a.tags.append("p1")
b.tags.append("p2")
print("Right:", a.tags, b.tags)     # ['p1'] ['p2'] —— 各自独立


# ============================================================
# 一句话总结：
#   • "所有对象都该有的常量或共享状态" → 类属性
#   • "每个对象独立的状态"             → 实例属性，放 __init__ 里
#   • 列表/字典之类的可变对象 → 永远放 __init__，别做类属性
# ============================================================
