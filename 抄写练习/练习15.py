class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "..."
    
    def info(self):
        return f"{self.__class__.__name__}:{self.name}，{self.age}岁"
    
    def __str__(self):
        return self.info()



class Dog(Animal):
    def __init__(self, name, age , breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        return f"{self.name}:汪！"
    
    def fetch(self):
        return f"{self.name}捡回了球！"
    
    def info(self):
        base = super().info()
        return f"{base}，品种：{self.breed}"


class Cat(Animal):
    def  __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self.indoor =indoor
    
    def speak(self):
        return f"{self.name}：喵~"
    
    def purr(self):
        return f"{self.name}在呼噜..."

class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly
    
    def speak(self):
        return f"{self.name}：啾啾！"
    
    def describe(self):
        fly_status = "会飞" if self.can_fly else "不会飞"
        return f"{self.name}{fly_status}"

dog = Dog("旺财",3,"金毛")
cat =Cat("咪咪",2)
bird = Bird("小黄",1)

print(dog)
print(cat)
print(bird.describe())

print(dog.speak())
print(cat.speak())
print(dog.fetch())
print(cat.purr())

print(f"\n{isinstance(dog,Dog)}")
print(f"{isinstance(dog,Animal)}")
print(f"\n{isinstance(dog,Cat)}")

print(f"{issubclass(Dog, Animal)}")    # True
print(f"{issubclass(Cat, Animal)}")    # True
print(f"{issubclass(Dog, Cat)}")       # False
