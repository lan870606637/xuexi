# -*- coding: utf-8 -*-
"""
Day 2: 控制流（条件与循环）
学习目标：掌握条件判断和循环，能处理批量测试数据
"""


def section1():
    """第一部分：条件判断 (if-elif-else)"""
    print("\n" + "="*60)
    print("第一部分：条件判断 (if-elif-else)")
    print("="*60)
    
    # 【if 语句】
    # 语法:
    #   if 条件:
    #       条件为True时执行的代码
    # 作用: 根据条件判断是否执行某段代码
    # 注意: if后面要有冒号，缩进的代码属于if块
    
    test_result = "passed"
    print("\n基础条件判断:")
    if test_result == "passed":  # 判断 test_result 是否等于 "passed"
        print("  测试通过！")  # 条件为True时执行

    # 【if-else 语句】
    # 语法:
    #   if 条件:
    #       条件为True时执行
    #   else:
    #       条件为False时执行
    # 作用: 二选一，条件满足执行if块，不满足执行else块
    
    score = 75
    print(f"\n成绩判断 (score={score}):")
    if score >= 60:  # 判断 score 是否 >= 60
        print("  及格")  # 75 >= 60 为True，执行这里
    else:
        print("  不及格")  # 条件为False时执行这里

    # 【if-elif-else 语句】
    # 语法:
    #   if 条件1:
    #       条件1为True时执行
    #   elif 条件2:
    #       条件1为False且条件2为True时执行
    #   elif 条件3:
    #       前面都为False且条件3为True时执行
    #   else:
    #       所有条件都为False时执行
    # 作用: 多选一，从上到下判断，满足一个就执行对应的代码块
    
    print(f"\n等级判断 (score={score}):")
    if score >= 90:      # 先判断 >= 90
        grade = "A"
    elif score >= 80:    # 不满足上一个，再判断 >= 80
        grade = "B"
    elif score >= 70:    # 不满足上一个，再判断 >= 70
        grade = "C"      # 75 >= 70 为True，执行这里，后面不再判断
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"  等级: {grade}")

    # 【逻辑运算符】
    # and - 与: 两边都为True，结果才为True
    # or  - 或: 两边有一个为True，结果就为True
    # not - 非: 取反，True变False，False变True
    
    print("\n多条件判断:")
    platform = "Android"
    version = 12

    # and: 两个条件都要满足
    if platform == "Android" and version >= 10:
        print("  支持新特性测试")  # 两个条件都满足，执行

    # in: 成员判断，判断元素是否在列表/字符串中
    if platform in ["Android", "iOS"]:
        print("  是移动端平台")  # "Android" 在列表中，执行

    # not: 取反
    is_emulator = True
    if not is_emulator:  # not True = False
        print("  使用真机测试")  # 条件为False，不执行
    else:
        print("  使用模拟器测试")  # 执行这里


def section2():
    """第二部分：for循环 - 遍历测试数据"""
    print("\n" + "="*60)
    print("第二部分：for循环 - 遍历测试数据")
    print("="*60)

    # 【for 循环】
    # 语法:
    #   for 变量 in 可迭代对象:
    #       循环体
    # 作用: 遍历可迭代对象（列表、字符串、字典等）中的每个元素
    # 执行次数: 等于可迭代对象中元素的个数
    
    # 遍历列表
    test_cases = ["登录测试", "注册测试", "搜索测试", "下单测试"]
    print("\n遍历测试用例:")
    for case in test_cases:  # case 依次取列表中的每个元素
        print(f"  执行: {case}")  # 每次循环执行一次

    # 【range() 函数】
    # 作用: 生成一个整数序列，用于控制循环次数
    # 语法:
    #   range(stop)           - 从0到stop-1
    #   range(start, stop)    - 从start到stop-1
    #   range(start, stop, step) - 从start到stop-1，步长为step
    
    print("\n使用range(5):")
    # range(5) 生成: 0, 1, 2, 3, 4
    for i in range(5):
        print(f"  第{i+1}次测试")  # i从0开始，所以+1显示为第1次

    print("\n使用range(1, 6):")
    # range(1, 6) 生成: 1, 2, 3, 4, 5（包含1，不包含6）
    for i in range(1, 6):
        print(f"  测试编号: {i}")

    print("\n使用range(0, 10, 2) 步长为2:")
    # range(0, 10, 2) 生成: 0, 2, 4, 6, 8（每次+2）
    for i in range(0, 10, 2):
        print(f"  偶数: {i}")

    # 【enumerate() 函数】
    # 语法: enumerate(可迭代对象)
    # 作用: 同时获取元素的索引和值
    # 返回值: (索引, 值) 的元组序列
    
    print("\n使用enumerate:")
    for index, case in enumerate(test_cases):
        # index 是索引(0,1,2,3)，case 是对应的值
        print(f"  [{index}] {case}")

    # 遍历字典
    test_config = {
        "browser": "Chrome",
        "version": "120",
        "headless": True
    }

    print("\n遍历字典:")
    # 字典.items() 返回所有键值对
    for key, value in test_config.items():
        print(f"  {key} = {value}")

    # 【zip() 函数】
    # 语法: zip(列表1, 列表2, ...)
    # 作用: 把多个列表"压缩"在一起，同时遍历
    # 注意: 以最短的列表为准
    
    names = ["登录", "注册", "搜索"]
    status = ["通过", "失败", "通过"]
    print("\n同时遍历多个列表 (zip):")
    # zip(names, status) 生成: ("登录", "通过"), ("注册", "失败"), ("搜索", "通过")
    for name, stat in zip(names, status):
        print(f"  {name}: {stat}")


def section3():
    """第三部分：while循环"""
    print("\n" + "="*60)
    print("第三部分：while循环")
    print("="*60)

    # 【while 循环】
    # 语法:
    #   while 条件:
    #       循环体
    # 作用: 只要条件为True，就重复执行循环体
    # 注意: 必须确保条件最终会变为False，否则会无限循环
    
    # 基础while
    count = 0
    print("\n基础while:")
    while count < 5:  # 条件: count < 5
        print(f"  计数: {count}")
        count += 1  # 计数器+1，等价于 count = count + 1
        # 当count变成5时，条件为False，循环结束

    # while用于重试机制
    print("\n重试机制示例:")
    max_retry = 3
    retry_count = 0
    success = False

    # 条件: 重试次数小于最大次数 且 未成功
    while retry_count < max_retry and not success:
        retry_count += 1  # 重试次数+1
        print(f"  第{retry_count}次尝试...")
        if retry_count == 2:  # 模拟第2次成功
            success = True
            print("  成功！")
            # success变为True，条件变为False，循环结束


def section4():
    """第四部分：break和continue"""
    print("\n" + "="*60)
    print("第四部分：break和continue")
    print("="*60)

    # 【break 语句】
    # 作用: 立即退出整个循环，不再执行后续迭代
    # 使用场景: 找到目标后不需要继续遍历
    
    print("\nbreak示例 (找到第一个失败用例就停止):")
    results = ["通过", "通过", "失败", "通过", "失败"]
    for i, result in enumerate(results):
        if result == "失败":
            print(f"  发现失败用例，位置: {i}")
            break  # 找到第一个就立即退出循环，后面的不再检查
    # 循环结束后，不会检查后面的"通过"和"失败"

    # 【continue 语句】
    # 作用: 跳过当前迭代的剩余代码，直接进入下一次循环
    # 使用场景: 某些条件下不需要执行本次循环的后续操作
    
    print("\ncontinue示例 (跳过已禁用的用例):")
    test_cases = [
        {"name": "TC001", "enabled": True},
        {"name": "TC002", "enabled": False},
        {"name": "TC003", "enabled": True},
    ]
    for case in test_cases:
        if not case["enabled"]:
            print(f"  跳过: {case['name']} (已禁用)")
            continue  # 跳过本次循环的剩余代码，进入下一次循环
        # 如果执行了continue，下面的代码不会执行
        print(f"  执行: {case['name']}")

    # 【嵌套循环】
    # 定义: 一个循环里面包含另一个循环
    # 执行顺序: 外层循环执行一次，内层循环执行完整的一轮
    # 总次数: 外层次数 × 内层次数
    
    print("\n嵌套循环 (测试矩阵):")
    browsers = ["Chrome", "Firefox"]
    features = ["登录", "注册", "搜索"]

    for browser in browsers:  # 外层循环，执行2次
        for feature in features:  # 内层循环，每次执行3次
            # 总共执行 2 × 3 = 6 次
            print(f"  在{browser}上测试{feature}")


def section5():
    """第五部分：列表推导式 (进阶)"""
    print("\n" + "="*60)
    print("第五部分：列表推导式 (简洁写法)")
    print("="*60)

    # 【列表推导式】
    # 作用: 用一行代码创建列表，替代简单的for循环
    # 语法: [表达式 for 变量 in 可迭代对象]
    # 优点: 代码简洁、执行效率高
    
    numbers = [1, 2, 3, 4, 5]
    
    # 传统写法（3行）
    squares = []
    for n in numbers:
        squares.append(n ** 2)  # n的平方
    print(f"传统写法: {squares}")

    # 列表推导式（1行）
    # [n ** 2 for n in numbers]
    # 含义: 对numbers中的每个n，计算n**2，组成新列表
    squares = [n ** 2 for n in numbers]
    print(f"推导式: {squares}")

    # 【带条件的列表推导式】
    # 语法: [表达式 for 变量 in 可迭代对象 if 条件]
    # 作用: 只把满足条件的元素放入新列表
    
    # 只保留偶数（能被2整除的数）
    # n % 2 == 0 表示 n除以2的余数为0，即偶数
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"偶数: {even_numbers}")

    # 【字典推导式】
    # 语法: {键: 值 for 变量 in 可迭代对象}
    # 作用: 用一行代码创建字典
    
    names = ["Alice", "Bob", "Charlie"]
    # 创建 {名字: 名字长度} 的字典
    name_lengths = {name: len(name) for name in names}
    # Alice长度为5，Bob为3，Charlie为7
    print(f"名字长度: {name_lengths}")


def practice_task():
    """实战任务：批量处理测试数据"""
    print("\n" + "="*60)
    print("实战任务：批量处理测试数据")
    print("="*60)

    test_data = [
        {"username": "admin", "password": "123"},
        {"username": "user", "password": "456"},
        {"username": "", "password": "789"},
        {"username": "test", "password": ""},
        {"username": "valid", "password": "pass123"}
    ]

    print(f"\n原始测试数据: {len(test_data)}条")
    for data in test_data:
        print(f"  {data}")

    # 任务1: 过滤掉用户名为空的数据
    print("\n任务1: 过滤空用户名")
    valid_data = []  # 请在这里完成代码

    # 你的代码写在这里：
    # ...

    print(f"有效数据: {len(valid_data)}条")
    for data in valid_data:
        print(f"  {data}")

    # 验证
    expected = [
        {"username": "admin", "password": "123"},
        {"username": "user", "password": "456"},
        {"username": "test", "password": ""},
        {"username": "valid", "password": "pass123"}
    ]
    if valid_data == expected:
        print("✅ 任务1完成！")
    else:
        print("❌ 任务1未完成，请继续")

    # 任务2: 找出密码长度小于3的用户
    print("\n任务2: 弱密码检测")
    weak_password_users = []  # 请在这里完成代码

    # 你的代码写在这里：
    # ...

    print(f"弱密码用户: {weak_password_users}")
    
    # 验证
    if weak_password_users == ["admin"]:
        print("✅ 任务2完成！")
    else:
        print("❌ 任务2未完成，请继续")

    # 任务3: 统计每个用户的用户名长度
    print("\n任务3: 用户名长度统计")
    username_lengths = {}  # 请在这里完成代码

    # 你的代码写在这里：
    # ...

    print(f"用户名长度: {username_lengths}")
    
    # 验证
    expected_lengths = {
        "admin": 5, "user": 4, "": 0, 
        "test": 4, "valid": 5
    }
    if username_lengths == expected_lengths:
        print("✅ 任务3完成！")
    else:
        print("❌ 任务3未完成，请继续")


def show_answer():
    """显示参考答案"""
    print("\n" + "="*60)
    print("参考答案")
    print("="*60)
    
    code = '''
test_data = [
    {"username": "admin", "password": "123"},
    {"username": "user", "password": "456"},
    {"username": "", "password": "789"},
    {"username": "test", "password": ""},
    {"username": "valid", "password": "pass123"}
]

# 任务1: 过滤空用户名
valid_data = []
for data in test_data:
    if data["username"] != "":
        valid_data.append(data)
# 或者用列表推导式:
valid_data = [d for d in test_data if d["username"] != ""]

# 任务2: 弱密码检测
weak_password_users = []
for data in test_data:
    if len(data["password"]) < 3:
        weak_password_users.append(data["username"])

# 任务3: 用户名长度统计
username_lengths = {}
for data in test_data:
    username_lengths[data["username"]] = len(data["username"])
# 或者用字典推导式:
username_lengths = {d["username"]: len(d["username"]) for d in test_data}
'''
    print(code)


def show_summary():
    """显示学习总结"""
    print("\n" + "="*60)
    print("今日学习要点总结")
    print("="*60)
    
    summary = """
1. 条件判断：if-elif-else，多条件组合(and/or/not)
2. for循环：遍历列表、字典，range()，enumerate()，zip()
3. while循环：条件循环，重试机制
4. break：完全退出循环
5. continue：跳过当前迭代
6. 列表推导式：简洁的数据处理写法

验证标准：能写出循环处理列表的代码，完成数据过滤任务
"""
    print(summary)


def main():
    """主菜单"""
    while True:
        print("\n" + "="*60)
        print("Day 2: 控制流（条件与循环）- 学习菜单")
        print("="*60)
        print("1. 条件判断 (if-elif-else)")
        print("2. for循环")
        print("3. while循环")
        print("4. break和continue")
        print("5. 列表推导式")
        print("6. 实战任务")
        print("7. 显示参考答案")
        print("8. 学习总结")
        print("0. 退出")
        print("="*60)
        
        choice = input("\n请选择要学习的部分 (0-8): ").strip()
        
        if choice == "1":
            section1()
        elif choice == "2":
            section2()
        elif choice == "3":
            section3()
        elif choice == "4":
            section4()
        elif choice == "5":
            section5()
        elif choice == "6":
            practice_task()
        elif choice == "7":
            show_answer()
        elif choice == "8":
            show_summary()
        elif choice == "0":
            print("\n感谢学习！再见！")
            break
        else:
            print("\n无效选择，请重新输入")
        
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
