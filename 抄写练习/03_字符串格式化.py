# ============================================
# 题目03：字符串格式化
# 知识点：% 格式化 / format() / f-string
# ============================================

name = "小明"
age = 18
score = 95.5

# --- 旧式 % 格式化（了解即可）---
print("=== % 格式化 ===")
print("姓名：%s，年龄：%d" % (name, age))
print("成绩：%.1f" % score)   # .1f 表示保留1位小数
print("分数：%05.1f" % score) # 05 表示总宽度5，不足补0

# --- str.format() ---
print("\n=== format() ===")
print("姓名：{}，年龄：{}".format(name, age))
print("姓名：{0}，年龄：{1}，再次：{0}".format(name, age))   # 用下标
print("姓名：{n}，年龄：{a}".format(n=name, a=age))          # 用关键字
print("{:.2f}".format(score))       # 保留2位小数
print("{:>10}".format(name))        # 右对齐，宽度10
print("{:<10}".format(name))        # 左对齐
print("{:^10}".format(name))        # 居中对齐
print("{:0>5}".format(42))          # 右对齐，用0填充 -> 00042

# --- f-string（Python 3.6+，最推荐）---
print("\n=== f-string ===")
print(f"姓名：{name}，年龄：{age}")
print(f"成绩：{score:.2f}")         # 同样支持格式规范
print(f"两年后：{age + 2} 岁")      # 花括号内可以有表达式
print(f"名字长度：{len(name)}")      # 可以调用函数
print(f"{name!r}")                  # !r 表示 repr()
print(f"{name!s}")                  # !s 表示 str()

# --- f-string 对齐与填充 ---
print("\n=== f-string 对齐 ===")
for i in range(1, 6):
    print(f"{i:>3}  {i**2:>5}  {i**3:>7}")  # 右对齐，制表格

# --- 数字格式化 ---
print("\n=== 数字格式化 ===")
big = 1234567.89
print(f"{big:,.2f}")        # 千位分隔符：1,234,567.89
print(f"{0.456:.1%}")       # 百分比：45.6%
print(f"{255:#x}")          # 十六进制：0xff
print(f"{255:#o}")          # 八进制：0o377
print(f"{255:#b}")          # 二进制：0b11111111
print(f"{1234567:_}")       # Python 3.6+ 下划线分隔：1_234_567
