# Day 04 · 面向对象编程（OOP）

> 今天要做什么：从"用字典/函数勉强凑出来"的代码，升级到"用类把数据和行为绑在一起"。
> 这是后面 Day 14 写 POM（页面对象模型）、Day 15 搭项目结构的基础。

---

## 为什么需要面向对象？

假设你要管理 100 条测试用例，每条用例有 `name / priority / status / failure_reason`。

不用类的话，你会写一堆字典：

```python
case1 = {"name": "登录", "priority": "high", "status": "pending", "failure_reason": None}
case2 = {"name": "注册", "priority": "low",  "status": "pending", "failure_reason": None}
# ... 100 行类似的
```

字段名打错？运行时才发现。
想给所有用例加一个 `mark_failed(reason)` 方法？只能写一个全局函数，传字典进去。

**类**把"用例长什么样"和"用例能做什么"打包在一个地方：

```python
class TestCase:
    def __init__(self, name, priority="normal"): ...
    def run(self): ...
    def mark_failed(self, reason): ...
```

之后 `tc = TestCase("登录", "high")` 一行搞定，`tc.run()` 一行执行，字段拼错 IDE 直接红线。

---

## 今日学习路线

| 文件 | 学什么 | 重点 |
|---|---|---|
| `01_类与对象.py` | 类的定义、`__init__`、实例方法 | 类是"图纸"，对象是按图纸造的"实物" |
| `02_self是什么.py` | self 的本质 | self 就是"调用这个方法的那个对象" |
| `03_类属性与实例属性.py` | 类属性 vs 实例属性 | 类属性所有对象共享，实例属性各管各 |
| `04_类方法与静态方法.py` | `@classmethod`、`@staticmethod` | 90% 用普通方法，剩下两个按需 |
| `05_继承.py` | 继承、`super()`、方法重写 | 子类"是一种"父类才能继承 |
| `06_多态.py` | 鸭子类型 | 只看"有没有这个方法"，不看类型 |
| `07_实战_页面对象.py` | 综合实战：POM 雏形 | 把今天所学全部串起来 |
| `练习.py` | 4 道小题 | 写完再看末尾的参考答案 |

---

## 你应该获得的能力

学完这一天，要能做到：

1. **看懂别人的类**：知道 `class A(B):` 意思是"A 继承 B"，知道 `super().__init__()` 在干嘛
2. **自己写一个简单的类**：包括 `__init__`、几个方法、几个属性
3. **判断该用类还是该用函数**：单纯的"一次性计算"用函数，需要保持状态/复用结构就用类
4. **写出最朴素的 POM**：把一个登录页面封装成一个类，外部一行 `page.login(user, pwd)` 就能用

---

## 常见踩坑

| 坑 | 现象 | 原因 |
|---|---|---|
| 忘写 `self` | `AttributeError: object has no attribute 'xxx'` | 在 `__init__` 里写了 `name = "x"` 而不是 `self.name = "x"`，只是局部变量 |
| 调方法时少传 self | 直接用 `MyClass.method()` 报错 | 应该用 `obj.method()`，self 会自动传 |
| 继承忘调父类 init | 子类对象没有父类的属性 | 子类 `__init__` 里要写 `super().__init__(...)` |
| 改了"类属性"只影响自己 | `t1.count = 999` 后 `t2.count` 还是旧值 | 一旦在实例上赋值，就变成实例属性，覆盖了类属性 |

---

## 怎么用这一天的文件

```bash
cd day04
python 01_类与对象.py        # 按顺序一个一个跑，看输出，对照源码
python 02_self是什么.py
# ...
python 07_实战_页面对象.py
python 练习.py               # 自己写代码，写完看答案
```

每个文件都是独立可运行的，看输出 + 看源码 + 改两行试试，比死读注释强 10 倍。
