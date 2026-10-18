# -*- coding: utf-8 -*-
"""
Day 6: Day 6
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：文件读写基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：文件读写基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import os
    # 创建测试目录
    test_dir = "day06_test_files"
    os.makedirs(test_dir, exist_ok=True)
    # 1. 写入文件
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("写入文件:")
    file_path = os.path.join(test_dir, "test.txt")
    # 方式1：基本写法
    # open() - 打开文件
    # 语法: open(文件路径, 模式, encoding=编码)
    # 模式: r读 w写 a追加 b二进制
    # 注意: 要用close()关闭或用with自动管理
    f = open(file_path, "w", encoding="utf-8")  # w=写入模式
    f.write("第一行\n")
    f.write("第二行\n")
    f.close()  # 必须关闭！
    # 方式2：with语句 (推荐！自动关闭)
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("重新写入第一行\n")
        f.write("重新写入第二行\n")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"文件已写入: {file_path}")
    # 2. 读取文件
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n读取文件:")
    # 方式1：read() - 读取全部
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"read():\n{content}")
    # 方式2：readline() - 逐行读取
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "r", encoding="utf-8") as f:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("readline():")
        line1 = f.readline()
        line2 = f.readline()
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  第1行: {line1.strip()}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  第2行: {line2.strip()}")
    # 方式3：readlines() - 读取为列表
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"readlines(): {lines}")
    # 方式4：直接遍历 (推荐用于大文件)
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "r", encoding="utf-8") as f:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("遍历文件:")
        for i, line in enumerate(f, 1):
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  第{i}行: {line.strip()}")
    # 3. 追加模式
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n追加模式:")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "a", encoding="utf-8") as f:  # a=追加模式
        f.write("追加的第三行\n")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(file_path, "r", encoding="utf-8") as f:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"追加后内容:\n{f.read()}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：文件路径操作"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：文件路径操作")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("文件路径操作 (os.path和pathlib)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import os
    # from...import - 从模块导入特定内容
    # 作用: 只导入需要的函数/类，不用写模块名前缀
    from pathlib import Path
    # 获取当前工作目录
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"当前目录: {os.getcwd()}")
    # 拼接路径
    config_path = os.path.join("config", "test.json")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"拼接路径: {config_path}")
    # 获取绝对路径
    abs_path = os.path.abspath(file_path)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"绝对路径: {abs_path}")
    # 获取目录名和文件名
    dirname = os.path.dirname(abs_path)
    basename = os.path.basename(abs_path)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"目录: {dirname}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"文件名: {basename}")
    # 分离文件名和扩展名
    name, ext = os.path.splitext(basename)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"文件名: {name}, 扩展名: {ext}")
    # 检查文件/目录是否存在
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"\n文件存在? {os.path.exists(file_path)}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"是文件? {os.path.isfile(file_path)}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"是目录? {os.path.isdir(test_dir)}")
    # pathlib (更现代的写法)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n使用pathlib:")
    p = Path(file_path)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"Path对象: {p}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"父目录: {p.parent}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"文件名: {p.name}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"扩展名: {p.suffix}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"存在? {p.exists()}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：JSON处理"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：JSON处理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("JSON处理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import json
    # 1. Python对象转JSON字符串
    test_config = {
        "platform": "Android",
        "version": 12,
        "device": "emulator-5554",
        "capabilities": {
            "automationName": "UiAutomator2",
            "noReset": True
        },
        "test_cases": ["login", "register", "search"]
    }
    # json.dumps: Python对象 -> JSON字符串
    json_str = json.dumps(test_config)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"JSON字符串:\n{json_str}")
    # 美化输出 (indent缩进)
    json_pretty = json.dumps(test_config, indent=2, ensure_ascii=False)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"\n美化输出:\n{json_pretty}")
    # 2. JSON字符串转Python对象
    # json.loads: JSON字符串 -> Python对象
    parsed = json.loads(json_str)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"\n解析后的类型: {type(parsed)}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"平台: {parsed['platform']}")
    # 3. 写入JSON文件
    json_file = os.path.join(test_dir, "config.json")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(test_config, f, indent=2, ensure_ascii=False)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"\nJSON已保存: {json_file}")
    # 4. 读取JSON文件
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(json_file, "r", encoding="utf-8") as f:
        loaded_config = json.load(f)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"读取的配置: {loaded_config}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：YAML处理"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：YAML处理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("YAML处理 (需要安装: pip install pyyaml)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【异常处理 try-except】
    # 语法: try: ... except 异常类型: ...
    # 作用: 捕获并处理可能发生的错误，防止程序崩溃
    try:
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import yaml
        has_yaml = True
    except ImportError:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("提示: 请先安装PyYAML: pip install pyyaml")
        has_yaml = False
    if has_yaml:
        # YAML内容 (字符串)
        yaml_content = """
    # 测试配置
    platform: Android
    version: 12
    devices:
      - emulator-5554
      - emulator-5556
    capabilities:
      automationName: UiAutomator2
      noReset: true
      newCommandTimeout: 300
        """
        # YAML字符串 -> Python对象
        yaml_data = yaml.safe_load(yaml_content)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"解析的YAML:\n{yaml_data}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"设备列表: {yaml_data['devices']}")
        # Python对象 -> YAML字符串
        yaml_output = yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n转回YAML:\n{yaml_output}")
        # 写入YAML文件
        yaml_file = os.path.join(test_dir, "config.yaml")
        # 【with 语句】
        # 作用: 自动管理资源，确保文件等正确关闭
        # 原理: 使用上下文管理器 __enter__ 和 __exit__
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\nYAML已保存: {yaml_file}")
        # 读取YAML文件
        # 【with 语句】
        # 作用: 自动管理资源，确保文件等正确关闭
        # 原理: 使用上下文管理器 __enter__ 和 __exit__
        with open(yaml_file, "r", encoding="utf-8") as f:
            loaded_yaml = yaml.safe_load(f)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"读取的YAML: {loaded_yaml}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：CSV处理 (测试数据常用)"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：CSV处理 (测试数据常用)")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("CSV处理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import csv
    csv_file = os.path.join(test_dir, "test_data.csv")
    # 写入CSV
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("写入CSV:")
    test_data = [
        ["username", "password", "expected"],
        ["admin", "123456", "success"],
        ["user", "wrong", "fail"],
        ["", "123456", "fail"],
    ]
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(test_data)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"CSV已保存: {csv_file}")
    # 读取CSV
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n读取CSV:")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  {row}")
    # 使用DictReader (更方便)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n使用DictReader:")
    # 【with 语句】
    # 作用: 自动管理资源，确保文件等正确关闭
    # 原理: 使用上下文管理器 __enter__ 和 __exit__
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  {dict(row)}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """实战任务：读取测试配置"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：读取测试配置")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：读取测试配置")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def load_config():
        """
        读取配置文件，支持JSON和YAML格式
        参数:
            file_path: 配置文件路径
        返回:
            配置字典
        异常:
            文件不存在或格式错误时抛出异常
        """
        # 你的代码写在这里：
        # 提示：
        # 1. 检查文件是否存在
        # 2. 根据文件扩展名(.json或.yaml/.yml)选择解析方式
        # 3. 使用相应的库解析文件
        # 4. 返回解析后的字典
        pass  # 删除这行，写上你的代码
    # 测试代码 (取消注释测试)
    """
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n测试load_config:")
    # 测试JSON
    json_config = load_config(json_file)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"JSON配置: {json_config}")
    # 测试YAML (如果安装了pyyaml)
    if has_yaml:
        yaml_config = load_config(yaml_file)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"YAML配置: {yaml_config}")
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """参考答案（完成后对照）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("参考答案（完成后对照）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def load_config():
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import os
        # import - 导入模块
        # 作用: 引入其他模块的功能使用
        import json
        if not os.path.exists(file_path):
            # raise - 主动抛出异常
            # 作用: 当遇到错误条件时，主动抛出异常
            raise FileNotFoundError(f"配置文件不存在: {file_path}")
        # 获取文件扩展名
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        # 【with 语句】
        # 作用: 自动管理资源，确保文件等正确关闭
        # 原理: 使用上下文管理器 __enter__ 和 __exit__
        with open(file_path, "r", encoding="utf-8") as f:
            if ext == ".json":
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return json.load(f)
            elif ext in [".yaml", ".yml"]:
                # import - 导入模块
                # 作用: 引入其他模块的功能使用
                import yaml
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return yaml.safe_load(f)
            else:
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise ValueError(f"不支持的配置文件格式: {ext}")
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """今日学习要点总结"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("今日学习要点总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    1. 文件读写：
       - with语句 (推荐，自动关闭)
       - 模式: r(读), w(写), a(追加)
       - 编码: 始终指定utf-8
    2. 路径操作：
       - os.path.join() 拼接路径
       - os.path.exists() 检查存在
       - pathlib.Path (现代写法)
    3. JSON处理：
       - json.dumps() / json.loads() - 字符串
       - json.dump() / json.load() - 文件
       - indent参数美化输出
    4. YAML处理：
       - pip install pyyaml
       - yaml.safe_load() / yaml.dump()
    5. CSV处理：
       - csv.writer() / csv.reader()
       - csv.DictReader() (推荐)
    验证标准：能从配置文件读取测试环境配置
    """

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section9():
    """第九部分：logging日志模块（补充）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第九部分：logging日志模块（补充）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import logging
    import os

    # ---- 1. logging基本概念 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. logging模块基本概念:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    日志级别 (从低到高):
    - DEBUG    (10): 调试信息，最详细的日志
    - INFO     (20): 一般信息，确认程序按预期运行
    - WARNING  (30): 警告信息，表示可能出现问题 (默认级别)
    - ERROR    (40): 错误信息，程序某些功能无法执行
    - CRITICAL (50): 严重错误，程序可能无法继续运行

    为什么用logging而不是print?
    - 可以控制日志级别，按需过滤
    - 可以输出到文件，方便排查问题
    - 可以格式化输出，包含时间、模块名等
    - 自动化测试中用于记录测试执行过程
    """)

    # ---- 2. 基本配置 basicConfig ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. basicConfig基本配置:")
    # 【logging.basicConfig】
    # 语法: logging.basicConfig(level, format, filename, filemode)
    # 作用: 配置日志的基本设置
    # level: 设置日志级别
    # format: 设置日志格式
    # filename: 输出到文件
    logging.basicConfig(
        level=logging.DEBUG,  # 设置最低日志级别
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        # %(asctime)s  - 时间
        # %(name)s     - logger名称
        # %(levelname)s - 日志级别
        # %(message)s  - 日志内容
    )
    # 获取logger对象
    logger = logging.getLogger("TestLogger")

    # 输出不同级别的日志
    logger.debug("这是一条DEBUG日志 - 调试用")
    logger.info("这是一条INFO日志 - 正常信息")
    logger.warning("这是一条WARNING日志 - 警告")
    logger.error("这是一条ERROR日志 - 出错了")
    logger.critical("这是一条CRITICAL日志 - 严重错误")

    # ---- 3. 自定义Logger ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n3. 自定义Logger (实际项目推荐):")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    在自动化测试项目中，通常自定义Logger:

    import logging

    def get_logger(name, log_file='test.log', level=logging.INFO):
        # 创建logger
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # 创建文件处理器 - 日志写入文件
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)

        # 创建控制台处理器 - 日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # 创建格式化器
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器到logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

    使用:
    logger = get_logger('appium_test', 'logs/test.log')
    logger.info('测试开始')
    logger.error('元素未找到: login_button')
    """)

    # ---- 4. 在测试框架中使用logging ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. 在自动化测试中使用logging:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    # 在BasePage中集成logging:
    class BasePage:
        def __init__(self, driver):
            self.driver = driver
            self.logger = logging.getLogger(self.__class__.__name__)

        def find_element(self, locator):
            self.logger.info(f'查找元素: {locator}')
            try:
                element = self.driver.find_element(*locator)
                self.logger.info(f'元素找到: {locator}')
                return element
            except Exception as e:
                self.logger.error(f'元素未找到: {locator}, 错误: {e}')
                raise

        def click(self, locator):
            self.logger.info(f'点击元素: {locator}')
            self.find_element(locator).click()

    # 在conftest.py中配置logging:
    import pytest
    import logging

    @pytest.fixture(autouse=True)
    def test_logger(request):
        logger = logging.getLogger(request.node.name)
        logger.info(f'===== 测试开始: {request.node.name} =====')
        yield
        logger.info(f'===== 测试结束: {request.node.name} =====')
    """)

    # ---- 5. 常用格式化变量 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("5. 常用格式化变量:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    %(asctime)s    - 日志时间 (2024-01-15 10:30:00,123)
    %(name)s       - Logger名称
    %(levelname)s  - 日志级别 (DEBUG/INFO/WARNING/ERROR/CRITICAL)
    %(message)s    - 日志内容
    %(filename)s   - 文件名
    %(lineno)d     - 行号
    %(funcName)s   - 函数名
    %(pathname)s   - 文件完整路径

    推荐格式:
    '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s'
    输出: 2024-01-15 10:30:00 [INFO] LoginPage.click:25 - 点击登录按钮
    """)


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def practice_task():
    """实战任务"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请修改代码完成任务...")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def show_answer():
    """显示参考答案"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("参考答案")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请参考原文件中的答案部分")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def show_summary():
    """显示学习总结"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("学习总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请参考原文件中的总结部分")

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def main():
    """主菜单"""
    while True:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("Day {day_num}: 学习菜单")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("1. 第一部分：文件读写基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：文件路径操作")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：JSON处理")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：YAML处理")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：CSV处理 (测试数据常用)")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务：读取测试配置")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 今日学习要点总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 补充：logging日志模块")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("10. 实战任务")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 参考答案")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 学习总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("0. 退出")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        
        choice = input("\n请选择 (0-9): ").strip()
        
        if choice == "1":
            section1()
        if choice == "2":
            section2()
        if choice == "3":
            section3()
        if choice == "4":
            section4()
        if choice == "5":
            section5()
        if choice == "6":
            section6()
        if choice == "7":
            section7()
        if choice == "8":
            section8()
        if choice == "9":
            section9()
        elif choice == "10":
            practice_task()
        elif choice == "8":
            show_answer()
        elif choice == "7":
            show_summary()
        elif choice == "0":
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n感谢学习！再见！")
            break
        else:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n无效选择，请重新输入")
        
        # input() - 获取用户输入
        # 语法: input(提示信息)
        # 返回值: 用户输入的字符串
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
