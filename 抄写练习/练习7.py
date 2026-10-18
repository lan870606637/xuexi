score =85

if score >=90:
    grade = "A"
    print("优秀")
elif score >=80:
    grade = "B"
    print("良好")
elif score >=70:
    grade = "C"
    print("中等")
elif score >=60:
    grade = "D"
    print("及格")
else:
    grade = "F"
    print("不及格")

print(f"等级：{grade}")


age = 20
has_id = True
is_member = False

if age >= 18 and has_id:
    print("可以入场")

if age< 18 or is_member:
    print("有优惠")
else:
    print("无优惠")

if not is_member:
    print("请办理会员卡")


x = 10
print(x == 10)
print(x != 5)
print(x >5)
print(x<=10)

print(0<x<20)

fruits = ["苹果","香蕉","橙子"]
print("苹果" in fruits)
print("葡萄" not in fruits)
print("橙子" not in fruits)

a =None
print(a is None)
print(a is not None)

print("-----------------------")
lst1 = [1,2,3]
lst2 = [1,2,3]
lst3 = lst1
print(lst1 == lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))
print(id(lst3))
print(lst1 is lst3)

age = 17
status = "成年" if age>18 else "未成年"
print(status)

num = -5
abs_val = num if num >=0 else -num
print(f"绝对值：{abs_val}")

print("-----------")

username = "admin"
password = "123456"
is_active = True

if username == "admin":
    if password == "123456":
        if is_active:
            print("登录成功")
        else:
            print("账号已禁用")
    else:
        print("密码错误")
else:
    print("用户名不存在")


print("\n=== match 语句 ===")
command = "quit"

match command:
    case "start":
        print("程序启动")
    case "stop":
        print("停止程序")
    case "quit" | "exit":
        print("退出程序")
    case _:
        print(f"未知命令：{command}")


point = (1,0)

match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"x轴上，x={x}")
    case (0, y):
        print(f"y轴上，y={y}")
    case (x, y):
        print(f"普通点，x={x}, y={y}")


