# ============================================
# 题目07：条件判断
# 知识点：if/elif/else / 三元表达式 / match
# ============================================

# --- 基本 if/elif/else ---
print("=== 成绩等级判断 ===")
score = 85

if score >= 90:
    grade = "A"
    print("优秀")
elif score >= 80:
    grade = "B"
    print("良好")
elif score >= 70:
    grade = "C"
    print("中等")
elif score >= 60:
    grade = "D"
    print("及格")
else:
    grade = "F"
    print("不及格")

print(f"等级：{grade}")

# --- 逻辑运算符 ---
print("\n=== 逻辑运算 ===")
age = 20
has_id = True
is_member = False

if age >= 18 and has_id:
    print("可以入场")

if age < 18 or is_member:
    print("有优惠")
else:
    print("无优惠")

if not is_member:
    print("请办理会员卡")

# --- 比较运算符 ---
print("\n=== 比较运算 ===")
x = 10
print(x == 10)      # True，等于
print(x != 5)       # True，不等于
print(x > 5)        # True，大于
print(x <= 10)      # True，小于等于

# 链式比较（Python 特有，很优雅）
print(0 < x < 20)   # True，等价于 0 < x and x < 20

# --- in / not in / is / is not ---
print("\n=== in 和 is ===")
fruits = ["苹果", "香蕉", "橙子"]
print("苹果" in fruits)          # True
print("葡萄" not in fruits)      # True

a = None
print(a is None)                  # True
print(a is not None)              # False

# 注意：比较对象相同性用 is，比较值相等用 ==
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1
print(lst1 == lst2)     # True，值相等
print(lst1 is lst2)     # False，不同对象
print(lst1 is lst3)     # True，同一个对象

# --- 三元表达式（条件表达式）---
print("\n=== 三元表达式 ===")
age = 17
status = "成年" if age >= 18 else "未成年"
print(status)

num = -5
abs_val = num if num >= 0 else -num
print(f"绝对值：{abs_val}")

# --- 嵌套条件（保持简洁）---
print("\n=== 嵌套条件 ===")
username = "admin"
password = "123456"
is_active = True

if username == "admin":
    if password == "123456":
        if is_active:
            print("登录成功")
        else:
            print("账户已禁用")
    else:
        print("密码错误")
else:
    print("用户名不存在")

# --- match 语句（Python 3.10+）---
print("\n=== match 语句 ===")
command = "quit"

match command:
    case "start":
        print("启动程序")
    case "stop":
        print("停止程序")
    case "quit" | "exit":   # 多个值用 |
        print("退出程序")
    case _:                 # 默认分支，类似 default
        print(f"未知命令：{command}")

# match 结构体
print("\n--- match 结构体 ---")
point = (1, 0)

match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"x轴上，x={x}")
    case (0, y):
        print(f"y轴上，y={y}")
    case (x, y):
        print(f"普通点，x={x}, y={y}")
