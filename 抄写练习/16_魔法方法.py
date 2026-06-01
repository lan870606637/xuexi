# ============================================
# 题目16：魔法方法（Dunder Methods）
# 知识点：__str__ / __len__ / __eq__ / __add__ / 运算符重载
# ============================================

# --- __str__ 和 __repr__ ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"

    # --- 运算符重载 ---
    def __add__(self, other):       # self + other
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # self - other
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):      # self * 数字
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):     # 数字 * self（右侧乘法）
        return self.__mul__(scalar)

    def __neg__(self):              # -self（取反）
        return Point(-self.x, -self.y)

    # --- 比较运算符 ---
    def __eq__(self, other):        # ==
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):        # <（按到原点距离比较）
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __le__(self, other):        # <=
        return self == other or self < other

    # --- 其他 ---
    def __abs__(self):              # abs()
        return (self.x**2 + self.y**2) ** 0.5

    def __bool__(self):             # bool(point)
        return self.x != 0 or self.y != 0


print("=== Point 运算 ===")
p1 = Point(1, 2)
p2 = Point(3, 4)

print(str(p1))          # Point(1, 2)
print(repr(p2))

print(p1 + p2)          # Point(4, 6)
print(p2 - p1)          # Point(2, 2)
print(p1 * 3)           # Point(3, 6)
print(3 * p1)           # Point(3, 6)，用了 __rmul__
print(-p1)              # Point(-1, -2)

print(p1 == Point(1, 2))    # True
print(p1 < p2)              # True（距离更小）
print(abs(p2))              # 5.0
print(bool(Point(0, 0)))    # False
print(bool(p1))             # True


# --- 容器相关魔法方法 ---
print("\n=== 容器魔法方法 ===")
class NumberList:
    def __init__(self, *args):
        self.data = list(args)

    def __len__(self):              # len()
        return len(self.data)

    def __getitem__(self, index):   # lst[index] / lst[start:stop]
        return self.data[index]

    def __setitem__(self, index, value):  # lst[index] = value
        self.data[index] = value

    def __delitem__(self, index):   # del lst[index]
        del self.data[index]

    def __contains__(self, item):   # item in lst
        return item in self.data

    def __iter__(self):             # for x in lst
        return iter(self.data)

    def __str__(self):
        return f"NumberList{self.data}"

    def __repr__(self):
        return str(self)


nl = NumberList(10, 20, 30, 40, 50)
print(f"长度：{len(nl)}")
print(f"第一个：{nl[0]}")
print(f"切片：{nl[1:3]}")
print(f"20 in nl: {20 in nl}")
print(f"99 in nl: {99 in nl}")

nl[0] = 100
print(nl)

del nl[2]
print(nl)

print("遍历：", end="")
for x in nl:
    print(x, end=" ")
print()

# --- 上下文管理器 __enter__ / __exit__ ---
print("\n=== 上下文管理器 ===")
class Timer:
    import time

    def __enter__(self):
        import time
        self.start = time.time()
        print("计时开始")
        return self                 # 返回值赋给 as 后的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"计时结束，耗时：{elapsed:.4f}秒")
        return False                # False 表示不抑制异常


with Timer() as t:
    total = sum(range(100000))
    print(f"计算结果：{total}")

# --- __call__（让实例像函数一样调用）---
print("\n=== __call__ ===")
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n

add5 = Adder(5)
print(add5(10))         # 15
print(add5(20))         # 25
print(callable(add5))   # True，因为定义了 __call__
