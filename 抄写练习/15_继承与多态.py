# ============================================
# 题目15：继承与多态
# 知识点：单继承 / 多重继承 / super() / 方法重写 / 多态
# ============================================

# --- 基类（父类）---
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def info(self):
        return f"{self.__class__.__name__}: {self.name}，{self.age}岁"

    def __str__(self):
        return self.info()


# --- 单继承 ---
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)     # 调用父类的 __init__
        self.breed = breed              # 子类特有属性

    def speak(self):                    # 重写父类方法
        return f"{self.name}：汪！"

    def fetch(self):                    # 子类特有方法
        return f"{self.name} 捡回了球！"

    def info(self):
        base = super().info()           # 调用父类方法
        return f"{base}，品种：{self.breed}"


class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name}：喵~"

    def purr(self):
        return f"{self.name} 在呼噜..."


class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name}：啾啾！"

    def describe(self):
        fly_status = "会飞" if self.can_fly else "不会飞"
        return f"{self.name} {fly_status}"


# --- 创建实例，测试继承 ---
print("=== 继承 ===")
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2)
bird = Bird("小黄", 1)

print(dog)              # 继承了 __str__ -> info()
print(cat)
print(bird.describe())

print(dog.speak())
print(cat.speak())
print(dog.fetch())      # 子类特有方法
print(cat.purr())

# 检查继承关系
print(f"\n{isinstance(dog, Dog)}")      # True
print(f"{isinstance(dog, Animal)}")    # True，狗也是动物
print(f"{isinstance(dog, Cat)}")       # False

print(f"{issubclass(Dog, Animal)}")    # True
print(f"{issubclass(Cat, Animal)}")    # True
print(f"{issubclass(Dog, Cat)}")       # False

# --- 多态（同一接口，不同行为）---
print("\n=== 多态 ===")
animals = [
    Dog("旺财", 3, "金毛"),
    Cat("咪咪", 2),
    Bird("小黄", 1),
    Dog("大黑", 5, "哈士奇"),
]

# 同一个循环，不同的 speak() 行为
for animal in animals:
    print(animal.speak())       # 多态！

# 函数不关心具体类型
def make_noise(animal):
    print(animal.speak())

for a in animals:
    make_noise(a)

# --- 多重继承 ---
print("\n=== 多重继承 ===")
class Flyable:
    def fly(self):
        return f"{self.name} 正在飞行"

class Swimmable:
    def swim(self):
        return f"{self.name} 正在游泳"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name}：嘎嘎！"

duck = Duck("唐老鸭", 4)
print(duck.speak())
print(duck.fly())
print(duck.swim())

# MRO：方法解析顺序（从左到右）
print("\nMRO:", [c.__name__ for c in Duck.__mro__])

# --- 抽象基类（强制子类实现方法）---
print("\n=== 抽象基类 ===")
from abc import ABC, abstractmethod

class Shape(ABC):           # 继承 ABC 使其成为抽象基类
    @abstractmethod
    def area(self):         # 抽象方法，子类必须实现
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):     # 普通方法，子类可以继承
        return f"面积：{self.area():.2f}，周长：{self.perimeter():.2f}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

shapes = [Square(4), Circle(3), Square(6)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.describe()}")

# try:
#     s = Shape()   # 不能实例化抽象类，会报 TypeError
# except TypeError as e:
#     print(e)
