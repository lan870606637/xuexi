name = "小明"
age = 18
score = 95.5



print("姓名：{}，年龄：{}".format(name,age))
print("姓名：{0}，年龄：{1}，再次：{0}".format(name,age))
print("姓名：{n}，年龄：{a}".format(n=name, a=age))
print("{:.2f}".format(score))
print("{:>10}".format(name))
print("{:<10}".format(name))
print("{:^10}".format(name))
print("{:0>5}".format(42))


print(f"姓名：{name}，年龄：{age}")
print(f"成绩：{score:.2f}")
print(f"两年后：{age+2}")
print(f"名字长度:{len(name)}")
print(f"{name!r}")
print(f"{name!s}")

for i in range(1,6):
 print(f"{i:>3}  {i**2:>5}  {i**3:>7}")



 big =1234567.89
 print(f"{big:,.2f}")
 print(f"{0.456:.1%}")
 print(f"{255:#x}")
 print(f"{255:#o}")
print(f"{255:#b}")
print(f"{big:_}")

