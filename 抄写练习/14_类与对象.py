# ============================================
# 题目14：类与对象
# 知识点：__init__ / 实例属性 / 类属性 / 实例方法
# ============================================

# --- 定义类 ---
class Dog:
    # 类属性：所有实例共享
    species = "犬科动物"
    total_count = 0

    # 初始化方法（构造函数）
    def __init__(self, name, breed, age):
        # 实例属性：每个实例独有
        self.name = name
        self.breed = breed
        self.age = age
        Dog.total_count += 1    # 每次创建实例，类计数+1

    # 实例方法：第一个参数必须是 self
    def bark(self):
        print(f"{self.name}：汪汪汪！")

    def info(self):
        return f"{self.name}（{self.breed}），{self.age}岁"

    def birthday(self):
        self.age += 1
        print(f"{self.name} 过生日了，现在 {self.age} 岁")

    # __str__：print(实例) 时调用
    def __str__(self):
        return f"Dog({self.name}, {self.breed})"

    # __repr__：在控制台直接输入实例名时调用
    def __repr__(self):
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"


# --- 创建实例 ---
print("=== 创建实例 ===")
dog1 = Dog("旺财", "金毛", 3)
dog2 = Dog("小黑", "拉布拉多", 5)

print(dog1)                 # 调用 __str__
print(repr(dog2))           # 调用 __repr__

# --- 访问属性和方法 ---
print("\n=== 访问属性和方法 ===")
print(dog1.name)            # 旺财
print(dog1.breed)           # 金毛
print(dog1.info())

dog1.bark()
dog1.birthday()

# --- 类属性 vs 实例属性 ---
print("\n=== 类属性 ===")
print(Dog.species)          # 通过类名访问
print(dog1.species)         # 也可以通过实例访问（会查找类属性）
print(f"总共创建了 {Dog.total_count} 只狗")

# 修改类属性
Dog.species = "家犬"
print(dog1.species)         # 家犬
print(dog2.species)         # 家犬，所有实例都改了

# 实例属性会遮蔽同名类属性
dog1.species = "特殊犬"     # 只修改了 dog1 的实例属性
print(dog1.species)         # 特殊犬
print(dog2.species)         # 家犬，不受影响

# --- 类方法和静态方法 ---
print("\n=== 类方法与静态方法 ===")
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):             # 实例方法
        return self.PI * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):  # 类方法，第一个参数是 cls（类本身）
        return cls(diameter / 2)       # 替代构造函数

    @staticmethod
    def is_valid_radius(r):     # 静态方法，与类和实例都无关
        return r > 0

c1 = Circle(5)
print(f"半径5的面积：{c1.area():.2f}")

c2 = Circle.from_diameter(10)   # 用类方法创建实例
print(f"直径10的面积：{c2.area():.2f}")

print(Circle.is_valid_radius(-1))   # False
print(Circle.is_valid_radius(5))    # True

# --- 属性装饰器 @property ---
print("\n=== @property ===")
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):            # getter
        return self._width

    @width.setter
    def width(self, value):     # setter
        if value <= 0:
            raise ValueError("宽度必须大于0")
        self._width = value

    @property
    def area(self):             # 只读属性（只有 getter）
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


rect = Rectangle(4, 5)
print(f"面积：{rect.area}")         # 像属性一样访问，不用加()
print(f"周长：{rect.perimeter}")

rect.width = 6                      # 调用 setter
print(f"修改宽度后面积：{rect.area}")

try:
    rect.width = -1                 # 会触发 ValueError
except ValueError as e:
    print(f"错误：{e}")

# rect.area = 100  # 报错，只读属性无法赋值
