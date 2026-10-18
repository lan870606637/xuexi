class Dog:
    species = "犬科动物"
    total_count = 0 

    def __init__(self, name , breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        Dog.total_count += 1
    
    def bark(self):
        print(f"{self.name}:汪汪汪！")

    def info(self):
        return f"{self.name} （{self.breed}），{self.age}岁"

    def birthday(self):
        self.age += 1
        print(f"{self.name}过生日了，现在{self.age}岁")
    
    def __str__(self):
        return f"Dog({self.name},{self.breed})"

    
    def __repr__(self):
        return f"Dog(name={self.name!r},breed={self.breed!r}),age={self.age}"


dog1 = Dog("旺柴","金毛",3)
dog2 = Dog("小黑","拉布拉多",5)

print(dog1)
print(repr(dog2))


print(dog1.name)
print(dog1.breed)
print(dog1.info())

print(Dog.species)
print(dog1.species)
print(f"总共创建了{Dog.total_count}只狗")

Dog.species = "家犬"
print(dog1.species)
print(dog2.species)

dog1.species = "特殊犬"
print(dog1.species)
print(dog2.species)


class Circle:
    PI = 3.14159

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2
    
    @classmethod
    def from_diameter(cls,diameter):
        return cls(diameter /2 )
    

    @staticmethod
    def is_valid_radius(r):
        return r > 0
    

c1 = Circle(5)
print(f"半径5的面积：{c1.area():.2f}")

c2 = Circle.from_diameter(10)
print(f"直径10的面积：{c2.area():.2f}")

print(Circle.is_valid_radius(-1))
print(Circle.is_valid_radius(5))

class Rectangle:
    def __init__(self,width,height):
        self._width =width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if value <= 0:
            raise ValueError("宽度必须大于0")
        self._width = value
    
    @property
    def area(self):
        return self._width * self._height


    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

rect = Rectangle(4,5)
print(f"面积：{rect.area}")
print(f"周长：{rect.perimeter}")

rect.width = 6
print(f"修改宽度后面积：{rect.area}")

try:
    rect.width = -1
except ValueError as e:
    print(f"错误：{e}")
    