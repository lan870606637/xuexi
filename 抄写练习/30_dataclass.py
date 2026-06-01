# ============================================
# 题目30：dataclass（数据类）
# 知识点：@dataclass / field / 后处理 / 比较 / 冻结
# ============================================

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional

# --- 传统类 vs dataclass ---
print("=== 传统方式 ===")
class PersonOld:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age}, email={self.email!r})"

    def __eq__(self, other):
        if not isinstance(other, PersonOld):
            return NotImplemented
        return (self.name, self.age, self.email) == (other.name, other.age, other.email)

p = PersonOld("张三", 25, "zhangsan@example.com")
print(p)

# --- dataclass 自动生成 __init__ / __repr__ / __eq__ ---
print("\n=== dataclass ===")
@dataclass
class Person:
    name: str
    age: int
    email: str = ""             # 默认值

p1 = Person("张三", 25, "zhangsan@example.com")
p2 = Person("李四", 30)
p3 = Person("张三", 25, "zhangsan@example.com")

print(p1)                       # 自动生成的 __repr__
print(p1 == p3)                 # True，自动生成的 __eq__
print(p1 == p2)                 # False

# --- field()：自定义字段 ---
print("\n=== field() ===")
@dataclass
class Student:
    name: str
    age: int
    scores: List[int] = field(default_factory=list)  # 列表默认值必须用 factory
    grade: str = field(init=False)      # init=False：不在 __init__ 中设置
    _id: int = field(default=0, repr=False)  # repr=False：不在打印中显示

    def __post_init__(self):            # __init__ 完成后自动调用
        avg = sum(self.scores) / len(self.scores) if self.scores else 0
        if avg >= 90:
            self.grade = "A"
        elif avg >= 80:
            self.grade = "B"
        elif avg >= 70:
            self.grade = "C"
        else:
            self.grade = "D"

s1 = Student("张三", 20, [85, 92, 78])
s2 = Student("李四", 22, [95, 88, 96])
print(s1)
print(s2)

# --- 排序（order=True）---
print("\n=== 带排序的 dataclass ===")
@dataclass(order=True)
class Point:
    x: float
    y: float

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5

points = [Point(3, 4), Point(1, 1), Point(5, 0), Point(0, 2)]
print(sorted(points))           # 按 x 主排序，x 相同再按 y

# --- 冻结（frozen=True）-> 不可变 ---
print("\n=== 冻结的 dataclass ===")
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

p = ImmutablePoint(3.0, 4.0)
print(p)

try:
    p.x = 5.0               # 会报错
except Exception as e:
    print(f"不能修改：{e}")

# 冻结的 dataclass 可以作为字典键（可哈希）
positions = {ImmutablePoint(0, 0): "原点", ImmutablePoint(1, 0): "右"}
print(positions[ImmutablePoint(0, 0)])

# --- 转换为字典和元组 ---
print("\n=== asdict / astuple ===")
p = Person("张三", 25, "zhangsan@example.com")
print(asdict(p))                # {'name': '张三', 'age': 25, 'email': '...'}
print(astuple(p))               # ('张三', 25, '...')

# --- 继承 ---
print("\n=== dataclass 继承 ===")
@dataclass
class Employee(Person):
    department: str = ""
    salary: float = 0.0

e = Employee("张三", 25, "zhangsan@example.com", "技术部", 12000)
print(e)

# --- 实用案例：配置类 ---
print("\n=== 配置类 ===")
@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 3306
    database: str = "mydb"
    username: str = "root"
    password: str = field(default="", repr=False)   # 密码不在打印中显示
    max_connections: int = 10

    @property
    def connection_string(self):
        return f"mysql://{self.username}@{self.host}:{self.port}/{self.database}"

cfg = DatabaseConfig(host="192.168.1.1", database="prod_db", password="secret")
print(cfg)
print(f"连接字符串：{cfg.connection_string}")
