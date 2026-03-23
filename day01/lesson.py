# -*- coding: utf-8 -*-
"""
Day 1: 数据类型与变量
学习目标：掌握Python基础数据类型，能看懂和修改AI生成的代码

运行方式：
- 直接运行会显示菜单，选择要学习的部分
- 或者运行特定函数如：python -c "from day01.lesson import section1; section1()"
"""


def section1():
    """第一部分：数字类型 (Number)"""
    print("\n" + "="*60)
    print("第一部分：数字类型 (Number)")
    print("="*60)
    
    # 【变量赋值】
    # 语法: 变量名 = 值
    # 作用: 把右边的值存到左边的变量中
    # 变量名规则: 只能包含字母、数字、下划线，不能以数字开头
    
    # 整数 (int)
    # 定义: 没有小数部分的数字
    # 示例: 0, -5, 100, 9999
    age = 25
    print(f"年龄: {age}, 类型: {type(age)}")
    # type() 函数: 查看变量的数据类型
    # 返回值: <class 'int'> 表示整数类型

    # 浮点数 (float)
    # 定义: 有小数部分的数字
    # 示例: 3.14, -0.5, 2.0
    price = 19.99
    print(f"价格: {price}, 类型: {type(price)}")
    # 注意: 2.0 是浮点数，不是整数

    # 【基本运算】
    # 语法: 数字 运算符 数字
    # 返回值: 运算结果
    
    a = 10
    b = 3
    print(f"\n基本运算 (a={a}, b={b}):")
    
    # 加法 (+)
    # 作用: 两个数相加
    print(f"加法: {a} + {b} = {a + b}")
    
    # 减法 (-)
    # 作用: 左边数减去右边数
    print(f"减法: {a} - {b} = {a - b}")
    
    # 乘法 (*)
    # 作用: 两个数相乘
    print(f"乘法: {a} * {b} = {a * b}")
    
    # 除法 (/)
    # 作用: 左边数除以右边数
    # 注意: 结果永远是浮点数，即使能整除
    # 示例: 10 / 2 = 5.0 (不是 5)
    print(f"除法: {a} / {b} = {a / b}")
    
    # 整除 (//)
    # 作用: 除法后向下取整（去掉小数部分）
    # 示例: 10 // 3 = 3 (因为 3.33... 向下取整是 3)
    print(f"整除: {a} // {b} = {a // b}")
    
    # 取余 (%)
    # 作用: 除法的余数
    # 示例: 10 % 3 = 1 (因为 10 = 3*3 + 1)
    print(f"取余: {a} % {b} = {a % b}")
    
    # 幂运算 (**)
    # 作用: 左边数的右边数次方
    # 示例: 10 ** 3 = 10*10*10 = 1000
    print(f"幂运算: {a} ** {b} = {a ** b}")


def section2():
    """第二部分：字符串 (String)"""
    print("\n" + "="*60)
    print("第二部分：字符串 (String)")
    print("="*60)
    
    # 字符串定义
    single_quote = '单引号字符串'
    double_quote = "双引号字符串"
    triple_quote = '''多行
字符串'''

    print(f"\n字符串示例:")
    print(single_quote)
    print(double_quote)
    print(triple_quote)

    # 字符串常用方法
    test_name = "  login Test  "
    print(f"\n字符串操作:")
    print(f"原字符串: '{test_name}'")
    
    # strip() - 去除首尾空格
    # 语法: 字符串.strip()
    # 作用: 删除字符串开头和结尾的所有空格（包括空格、换行、制表符）
    # 返回值: 新的字符串，原字符串不变
    print(f"去空格: '{test_name.strip()}'")
    
    # lower() - 转小写
    # 语法: 字符串.lower()
    # 作用: 把所有字母变成小写
    # 返回值: 新的字符串
    print(f"转小写: '{test_name.lower()}'")
    
    # upper() - 转大写
    # 语法: 字符串.upper()
    # 作用: 把所有字母变成大写
    print(f"转大写: '{test_name.upper()}'")
    
    # replace() - 替换
    # 语法: 字符串.replace(旧字符串, 新字符串)
    # 作用: 把字符串中所有的"旧字符串"替换成"新字符串"
    # 注意: 只替换完全匹配的部分，不会修改其他内容（如空格保留）
    # 返回值: 新的字符串，原字符串不变
    print(f"替换: '{test_name.replace('login', 'Logout')}'")
    
    # split() - 分割
    # 语法: 字符串.split(分隔符)
    # 作用: 按分隔符把字符串切成列表，默认按空格分割
    # 返回值: 列表
    print(f"分割: {test_name.split()}")
    
    # len() - 长度
    # 语法: len(字符串)
    # 作用: 计算字符串的字符数（包括空格）
    # 返回值: 整数
    print(f"长度: {len(test_name)}")

    # 字符串拼接和格式化
    platform = "Android"
    version = 12
    print(f"\n字符串格式化:")
    
    # f-string（推荐）
    # 语法: f"字符串{变量}"
    # 作用: 在字符串中嵌入变量或表达式
    print(f"测试平台: {platform}, 版本: {version}")
    
    # format方法
    # 语法: "字符串{}".format(值)
    # 作用: 用format里的值替换{}占位符
    print("测试平台: {}, 版本: {}".format(platform, version))
    
    # %格式化 (旧式，不推荐)
    # 语法: "字符串%s" % 值
    # %s表示字符串，%d表示整数
    print("测试平台: %s, 版本: %d" % (platform, version))


def section3():
    """第三部分：布尔值 (Boolean)"""
    print("\n" + "="*60)
    print("第三部分：布尔值 (Boolean)")
    print("="*60)
    
    # 【布尔值】
    # 定义: 只有两个值: True(真) 和 False(假)
    # 作用: 表示是/否、开/关、通过/失败等两种状态
    
    is_passed = True   # 测试通过
    is_failed = False  # 测试失败

    print(f"\n布尔值:")
    print(f"测试通过: {is_passed}, 类型: {type(is_passed)}")
    # type(True) 返回 <class 'bool'>
    print(f"测试失败: {is_failed}")

    # 【比较运算符】
    # 作用: 比较两个值，返回布尔值
    # 返回值: True 或 False
    
    score = 85
    print(f"\n比较运算 (score={score}):")
    
    # 大于 (>)
    # 语法: 左边 > 右边
    # 作用: 判断左边是否大于右边
    print(f"score > 60: {score > 60}")   # 85 > 60 是 True
    
    # 大于等于 (>=)
    # 语法: 左边 >= 右边
    # 作用: 判断左边是否大于或等于右边
    print(f"score >= 85: {score >= 85}") # 85 >= 85 是 True
    
    # 等于 (==)
    # 语法: 左边 == 右边
    # 作用: 判断两边是否相等
    # 注意: 是两个等号！一个等号(=)是赋值
    print(f"score == 85: {score == 85}") # 85 == 85 是 True
    
    # 不等于 (!=)
    # 语法: 左边 != 右边
    # 作用: 判断两边是否不相等
    print(f"score != 100: {score != 100}") # 85 != 100 是 True
    
    # 小于 (<)
    # 语法: 左边 < 右边
    print(f"score < 90: {score < 90}")   # 85 < 90 是 True
    
    # 小于等于 (<=)
    # 语法: 左边 <= 右边
    print(f"score <= 85: {score <= 85}") # 85 <= 85 是 True


def section4():
    """第四部分：列表 (List) - 重点！测试数据常用"""
    print("\n" + "="*60)
    print("第四部分：列表 (List) - 测试数据常用")
    print("="*60)
    
    # 【列表 List】
    # 定义: 用方括号 [] 包裹的有序集合
    # 特点: 可以存放任意类型，可以修改，索引从0开始
    # 语法: [元素1, 元素2, 元素3, ...]
    
    browsers = ["Chrome", "Firefox", "Safari", "Edge"]
    print(f"\n列表示例:")
    print(f"浏览器列表: {browsers}")

    # 【索引访问】
    # 语法: 列表[索引]
    # 规则: 索引从0开始，-1表示最后一个，-2表示倒数第二个
    print(f"第一个浏览器: {browsers[0]}")   # 索引0 = 第一个元素
    print(f"最后一个浏览器: {browsers[-1]}") # 索引-1 = 最后一个元素

    # 【切片操作】
    # 语法: 列表[start:end:step]
    # 作用: 获取列表的一部分（子列表）
    # 规则: 包含start索引，不包含end索引；step是步长，默认为1
    print(f"前两个: {browsers[0:2]}")  # 取索引0和1的元素，不包含2
    print(f"后两个: {browsers[-2:]}")  # 从倒数第2个取到末尾

    # 【列表增删改查】
    print(f"\n列表操作:")

    # append() - 末尾添加
    # 语法: 列表.append(元素)
    # 作用: 在列表末尾添加一个元素
    # 返回值: None（直接修改原列表）
    browsers.append("Opera")
    print(f"append后: {browsers}")

    # insert() - 指定位置插入
    # 语法: 列表.insert(索引, 元素)
    # 作用: 在指定索引位置插入元素，原位置及后面的元素后移
    browsers.insert(1, "IE")  # 在索引1位置插入"IE"
    print(f"insert后: {browsers}")

    # 修改元素
    # 语法: 列表[索引] = 新值
    # 作用: 直接修改指定位置的元素
    browsers[1] = "Brave"  # 把索引1的元素改成"Brave"
    print(f"修改后: {browsers}")

    # remove() - 按值删除
    # 语法: 列表.remove(值)
    # 作用: 删除第一个匹配的元素
    # 注意: 如果值不存在会报错 ValueError
    browsers.remove("Brave")
    print(f"remove后: {browsers}")

    # pop() - 按索引删除
    # 语法: 列表.pop(索引) 或 列表.pop()
    # 作用: 删除指定索引的元素并返回它，默认删除最后一个
    # 返回值: 被删除的元素
    deleted = browsers.pop()  # 删除并返回最后一个元素
    print(f"pop后: {browsers}, 被删除: {deleted}")

    # 【列表其他操作】
    print(f"\n列表其他操作:")
    
    # len() - 长度
    # 语法: len(列表)
    # 作用: 计算列表中元素的个数
    print(f"长度: {len(browsers)}")
    
    # in - 成员判断
    # 语法: 元素 in 列表
    # 作用: 判断元素是否在列表中
    # 返回值: True 或 False
    print(f"Chrome是否在列表: {'Chrome' in browsers}")
    
    # sort() - 排序
    # 语法: 列表.sort() 或 列表.sort(reverse=True)
    # 作用: 对列表进行排序，默认升序（从小到大）
    # 注意: 直接修改原列表，返回None
    browsers.sort()
    print(f"排序后: {browsers}")


def section5():
    """第五部分：字典 (Dict) - 重点！测试配置常用"""
    print("\n" + "="*60)
    print("第五部分：字典 (Dict) - 测试配置常用")
    print("="*60)
    
    # 【字典 Dict】
    # 定义: 用花括号 {} 包裹的键值对集合
    # 特点: 键必须是唯一的，通过键访问值，无序（Python3.7+保持插入顺序）
    # 语法: {键1: 值1, 键2: 值2, ...}
    
    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.example.app",
        "appActivity": ".MainActivity"
    }

    print(f"\n字典示例:")
    print(f"配置信息: {capabilities}")

    # 【访问字典值】
    # 方式1: 字典[键]
    # 作用: 通过键获取值
    # 注意: 如果键不存在会报错 KeyError
    print(f"平台: {capabilities['platformName']}")
    
    # 方式2: 字典.get(键, 默认值)
    # 作用: 通过键获取值，如果不存在返回默认值
    # 优点: 不会报错，更安全
    print(f"设备: {capabilities.get('deviceName')}")
    print(f"不存在key: {capabilities.get('noKey', '默认值')}")

    # 【增删改查】
    print(f"\n字典操作:")

    # 增加/修改
    # 语法: 字典[键] = 值
    # 作用: 如果键存在则修改值，不存在则添加新键值对
    capabilities["automationName"] = "UiAutomator2"  # 新增键值对
    capabilities["platformName"] = "iOS"  # 修改已有键的值
    print(f"增改后: {capabilities}")

    # 删除
    # 语法: del 字典[键]
    # 作用: 删除指定的键值对
    # 注意: 键不存在会报错
    del capabilities["appActivity"]
    print(f"del后: {capabilities}")

    # 【遍历字典】
    print(f"\n遍历字典:")
    
    # 方式1: 遍历键（默认）
    # for 键 in 字典:
    for key in capabilities:
        print(f"  {key}: {capabilities[key]}")
    
    # 方式2: 遍历键值对
    # 字典.items() 返回所有键值对，每个是 (键, 值) 元组
    for key, value in capabilities.items():
        print(f"  {key} = {value}")


def section6():
    """第六部分：类型转换"""
    print("\n" + "="*60)
    print("第六部分：类型转换")
    print("="*60)
    
    # 【类型转换】
    # 作用: 把一种数据类型转换成另一种
    # 常见函数: int(), float(), str(), list(), dict(), bool()
    
    print(f"\n类型转换:")

    # int() - 字符串/浮点数转整数
    # 语法: int(值)
    # 作用: 把字符串或浮点数转换成整数
    # 注意: 字符串必须是数字格式，否则会报错
    num_str = "100"
    num_int = int(num_str)
    print(f"'{num_str}' -> int: {num_int}, 类型: {type(num_int)}")

    # str() - 转字符串
    # 语法: str(值)
    # 作用: 把任意类型转换成字符串
    num = 200
    str_num = str(num)
    print(f"{num} -> str: '{str_num}', 类型: {type(str_num)}")

    # split() - 字符串转列表
    # 语法: 字符串.split(分隔符)
    # 作用: 按分隔符分割字符串，返回列表
    config_str = "a,b,c,d"
    config_list = config_str.split(",")
    print(f"'{config_str}' -> list: {config_list}")

    # join() - 列表转字符串
    # 语法: "连接符".join(列表)
    # 作用: 用连接符把列表元素连接成字符串
    # 注意: 列表元素必须是字符串
    joined = "-".join(config_list)
    print(f"{config_list} -> str: '{joined}'")


def practice_task():
    """实战任务：解析测试配置"""
    print("\n" + "="*60)
    print("实战任务：解析测试配置")
    print("="*60)

    config_str = "platform=Android,version=12,device=emulator"
    print(f"原始配置字符串: {config_str}")
    print("\n任务：将字符串转换成字典")
    print('期望结果: {"platform": "Android", "version": "12", "device": "emulator"}')
    print("\n提示：")
    print("1. 先用 split(',') 分割成列表")
    print("2. 遍历列表，对每个元素用 split('=') 分割成键值对")
    print("3. 存入字典")

    config_dict = {}  # 初始化空字典

    # 你的代码写在这里：
    # ...

    print(f"\n转换后的字典: {config_dict}")
    
    # 验证答案
    expected = {"platform": "Android", "version": "12", "device": "emulator"}
    if config_dict == expected:
        print("✅ 恭喜！答案正确！")
    else:
        print("❌ 答案不正确，请再试一次")
        print(f"期望: {expected}")


def show_answer():
    """显示参考答案"""
    print("\n" + "="*60)
    print("参考答案")
    print("="*60)
    
    code = '''
config_str = "platform=Android,version=12,device=emulator"
config_dict = {}

# 方法1：使用循环
pairs = config_str.split(",")  # ["platform=Android", "version=12", "device=emulator"]
for pair in pairs:
    key, value = pair.split("=")  # 解包赋值
    config_dict[key] = value

print(config_dict)
# 输出: {'platform': 'Android', 'version': '12', 'device': 'emulator'}

# 方法2：使用字典推导式（高级）
config_dict = {k: v for k, v in (pair.split("=") for pair in config_str.split(","))}
'''
    print(code)


def show_summary():
    """显示学习总结"""
    print("\n" + "="*60)
    print("今日学习要点总结")
    print("="*60)
    
    summary = """
1. 数字类型：int, float，掌握基本运算
2. 字符串：定义、常用方法、格式化(f-string)
3. 布尔值：True/False，比较运算
4. 列表：增删改查、切片、遍历 - 测试数据常用
5. 字典：键值对操作、遍历 - 测试配置常用
6. 类型转换：int(), str(), split(), join()

验证标准：能独立写出配置字符串转字典的代码
"""
    print(summary)


def main():
    """主菜单"""
    while True:
        print("\n" + "="*60)
        print("Day 1: 数据类型与变量 - 学习菜单")
        print("="*60)
        print("1. 数字类型 (Number)")
        print("2. 字符串 (String)")
        print("3. 布尔值 (Boolean)")
        print("4. 列表 (List)")
        print("5. 字典 (Dict)")
        print("6. 类型转换")
        print("7. 实战任务")
        print("8. 显示参考答案")
        print("9. 学习总结")
        print("0. 退出")
        print("="*60)
        
        choice = input("\n请选择要学习的部分 (0-9): ").strip()
        
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
            section6()
        elif choice == "7":
            practice_task()
        elif choice == "8":
            show_answer()
        elif choice == "9":
            show_summary()
        elif choice == "0":
            print("\n感谢学习！再见！")
            break
        else:
            print("\n无效选择，请重新输入")
        
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
