# -*- coding: utf-8 -*-
"""
批量添加语法注释脚本
给所有lesson.py文件添加详细的语法说明
"""

import os
import re

# 定义语法注释规则
COMMENT_RULES = [
    # 函数相关
    (r'^(\s*)def\s+(\w+)\s*\([^)]*\):', r'\1# 【函数定义】\n\1# 语法: def 函数名(参数):\n\1# 作用: 封装可复用的代码块\n\1# 调用: 函数名(参数)\n\1def \2():'),
    
    # return语句
    (r'^(\s*)return\s+(.+)$', r'\1# return - 返回值\n\1# 作用: 将结果返回给调用者，结束函数执行\n\1return \2'),
    
    # 类定义
    (r'^(\s*)class\s+(\w+)', r'\1# 【类定义】\n\1# 语法: class 类名:\n\1# 作用: 创建对象模板，封装数据和方法\n\1class \2'),
    
    # __init__方法
    (r'^(\s*)def\s+__init__\s*\(self', r'\1# 【构造方法】\n\1# 语法: def __init__(self, 参数):\n\1# 作用: 创建对象时自动调用，初始化对象属性\n\1def __init__(self'),
    
    # try-except
    (r'^(\s*)try:', r'\1# 【异常处理 try-except】\n\1# 语法: try: ... except 异常类型: ...\n\1# 作用: 捕获并处理可能发生的错误，防止程序崩溃\n\1try:'),
    
    # raise
    (r'^(\s*)raise\s+(.+)$', r'\1# raise - 主动抛出异常\n\1# 作用: 当遇到错误条件时，主动抛出异常\n\1raise \2'),
    
    # with语句
    (r'^(\s*)with\s+(.+):', r'\1# 【with 语句】\n\1# 作用: 自动管理资源，确保文件等正确关闭\n\1# 原理: 使用上下文管理器 __enter__ 和 __exit__\n\1with \2:'),
    
    # open函数
    (r'^(\s*)(\w+)\s*=\s*open\s*\(', r'\1# open() - 打开文件\n\1# 语法: open(文件路径, 模式, encoding=编码)\n\1# 模式: r读 w写 a追加 b二进制\n\1# 注意: 要用close()关闭或用with自动管理\n\1\2 = open('),
    
    # import语句
    (r'^(\s*)import\s+(.+)$', r'\1# import - 导入模块\n\1# 作用: 引入其他模块的功能使用\n\1import \2'),
    
    # from import
    (r'^(\s*)from\s+(.+)\s+import', r'\1# from...import - 从模块导入特定内容\n\1# 作用: 只导入需要的函数/类，不用写模块名前缀\n\1from \2 import'),
    
    # @装饰器
    (r'^(\s*)@(\w+)', r'\1# 【装饰器 @\2】\n\1# 作用: 在不修改原函数的情况下，添加额外功能\n\1# 原理: 接收函数作为参数，返回新函数\n\1@\2'),
    
    # lambda表达式
    (r'^(\s*)(\w+)\s*=\s*lambda', r'\1# lambda - 匿名函数\n\1# 语法: lambda 参数: 返回值\n\1# 作用: 创建简单的单行函数\n\1\2 = lambda'),
    
    # 列表操作
    (r'^(\s*)(\w+)\.append\s*\(', r'\1# append() - 列表末尾添加元素\n\1# 语法: 列表.append(元素)\n\1# 返回值: None（直接修改原列表）\n\1\2.append('),
    
    (r'^(\s*)(\w+)\.insert\s*\(', r'\1# insert() - 指定位置插入元素\n\1# 语法: 列表.insert(索引, 元素)\n\1# 作用: 在指定索引位置插入，后面的元素后移\n\1\2.insert('),
    
    (r'^(\s*)(\w+)\.remove\s*\(', r'\1# remove() - 按值删除元素\n\1# 语法: 列表.remove(值)\n\1# 注意: 删除第一个匹配项，不存在会报错\n\1\2.remove('),
    
    (r'^(\s*)(\w+)\.pop\s*\(', r'\1# pop() - 按索引删除并返回\n\1# 语法: 列表.pop(索引) 或 列表.pop()\n\1# 默认删除最后一个，返回被删除的元素\n\1\2.pop('),
    
    (r'^(\s*)(\w+)\.sort\s*\(', r'\1# sort() - 列表排序\n\1# 语法: 列表.sort() 或 列表.sort(reverse=True)\n\1# 作用: 原地排序（修改原列表），默认升序\n\1\2.sort('),
    
    # 字符串操作
    (r'^(\s*)(\w+)\.strip\s*\(', r'\1# strip() - 去除首尾空格\n\1# 语法: 字符串.strip()\n\1# 作用: 删除开头和结尾的空白字符\n\1\2.strip('),
    
    (r'^(\s*)(\w+)\.lower\s*\(', r'\1# lower() - 转小写\n\1# 语法: 字符串.lower()\n\1# 作用: 把所有字母变成小写\n\1\2.lower('),
    
    (r'^(\s*)(\w+)\.upper\s*\(', r'\1# upper() - 转大写\n\1# 语法: 字符串.upper()\n\1# 作用: 把所有字母变成大写\n\1\2.upper('),
    
    (r'^(\s*)(\w+)\.replace\s*\(', r'\1# replace() - 替换字符串\n\1# 语法: 字符串.replace(旧字符串, 新字符串)\n\1# 作用: 把所有旧字符串替换成新字符串\n\1\2.replace('),
    
    (r'^(\s*)(\w+)\.split\s*\(', r'\1# split() - 分割字符串\n\1# 语法: 字符串.split(分隔符)\n\1# 作用: 按分隔符分割，返回列表\n\1\2.split('),
    
    (r'^(\s*)(\w+)\.join\s*\(', r'\1# join() - 连接字符串\n\1# 语法: "连接符".join(可迭代对象)\n\1# 作用: 用连接符把元素连接成字符串\n\1\2.join('),
    
    # 字典操作
    (r'^(\s*)(\w+)\.keys\s*\(\)', r'\1# keys() - 获取所有键\n\1# 语法: 字典.keys()\n\1# 返回值: dict_keys对象，包含所有键\n\1\2.keys()'),
    
    (r'^(\s*)(\w+)\.values\s*\(\)', r'\1# values() - 获取所有值\n\1# 语法: 字典.values()\n\1# 返回值: dict_values对象，包含所有值\n\1\2.values()'),
    
    (r'^(\s*)(\w+)\.items\s*\(\)', r'\1# items() - 获取所有键值对\n\1# 语法: 字典.items()\n\1# 返回值: dict_items对象，每个元素是(键, 值)元组\n\1\2.items()'),
    
    (r'^(\s*)(\w+)\.get\s*\(', r'\1# get() - 安全获取字典值\n\1# 语法: 字典.get(键, 默认值)\n\1# 作用: 获取键对应的值，不存在返回默认值（不会报错）\n\1\2.get('),
    
    # 内置函数
    (r'^(\s*)len\s*\(', r'\1# len() - 计算长度\n\1# 语法: len(对象)\n\1# 作用: 计算字符串/列表/字典等的元素个数\n\1len('),
    
    (r'^(\s*)type\s*\(', r'\1# type() - 查看类型\n\1# 语法: type(对象)\n\1# 返回值: 对象的类型，如 <class "int">\n\1type('),
    
    (r'^(\s*)range\s*\(', r'\1# range() - 生成整数序列\n\1# 语法: range(stop) 或 range(start, stop, step)\n\1# 作用: 生成从start到stop-1的整数序列\n\1range('),
    
    (r'^(\s*)enumerate\s*\(', r'\1# enumerate() - 枚举\n\1# 语法: enumerate(可迭代对象, start=0)\n\1# 返回值: (索引, 值) 的元组序列\n\1enumerate('),
    
    (r'^(\s*)zip\s*\(', r'\1# zip() - 并行遍历\n\1# 语法: zip(列表1, 列表2, ...)\n\1# 作用: 把多个列表"压缩"在一起同时遍历\n\1zip('),
    
    (r'^(\s*)int\s*\(', r'\1# int() - 转整数\n\1# 语法: int(值) 或 int(字符串, 进制)\n\1# 作用: 把字符串或浮点数转换成整数\n\1int('),
    
    (r'^(\s*)str\s*\(', r'\1# str() - 转字符串\n\1# 语法: str(值)\n\1# 作用: 把任意类型转换成字符串\n\1str('),
    
    (r'^(\s*)list\s*\(', r'\1# list() - 转列表\n\1# 语法: list(可迭代对象)\n\1# 作用: 把元组、字符串等转换成列表\n\1list('),
    
    (r'^(\s*)dict\s*\(', r'\1# dict() - 创建字典\n\1# 语法: dict() 或 dict(键值对) 或 dict(关键字参数)\n\1# 作用: 创建字典对象\n\1dict('),
    
    (r'^(\s*)print\s*\(', r'\1# print() - 打印输出\n\1# 语法: print(值1, 值2, ..., sep=" ", end="\\n")\n\1# 作用: 把内容输出到控制台\n\1print('),
    
    # 类型转换
    (r'^(\s*)input\s*\(', r'\1# input() - 获取用户输入\n\1# 语法: input(提示信息)\n\1# 返回值: 用户输入的字符串\n\1input('),
    
    # 断言语句
    (r'^(\s*)assert\s+(.+)$', r'\1# assert - 断言\n\1# 语法: assert 条件, 错误信息\n\1# 作用: 条件为False时抛出AssertionError\n\1assert \2'),
]

def add_comments_to_file(file_path):
    """给单个文件添加语法注释"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经添加过详细注释
    if '# 【' in content or '# 语法:' in content:
        print(f"跳过（已有详细注释）: {file_path}")
        return
    
    print(f"处理: {file_path}")
    
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        new_line = line
        # 应用所有规则
        for pattern, replacement in COMMENT_RULES:
            match = re.match(pattern, line)
            if match:
                # 替换并保留原始缩进
                new_line = re.sub(pattern, replacement, line)
                break
        new_lines.append(new_line)
    
    new_content = '\n'.join(new_lines)
    
    # 备份原文件
    backup_path = file_path + '.backup'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 写入新内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  完成！备份: {backup_path}")

def main():
    """主函数"""
    base_dir = r"c:\Users\user\Desktop\jiaoben\xuexi\python_learning"
    
    processed = 0
    skipped = 0
    
    for day_num in range(3, 22):  # 从Day 3开始，Day 1-2已手动处理
        day_str = f"day{day_num:02d}"
        file_path = os.path.join(base_dir, day_str, "lesson.py")
        
        if os.path.exists(file_path):
            if '# 【' in open(file_path, 'r', encoding='utf-8').read():
                print(f"跳过（已有注释）: {file_path}")
                skipped += 1
            else:
                add_comments_to_file(file_path)
                processed += 1
        else:
            print(f"文件不存在: {file_path}")
    
    print(f"\n处理完成！")
    print(f"已处理: {processed} 个文件")
    print(f"已跳过: {skipped} 个文件")
    print(f"备份文件后缀: .backup")

if __name__ == "__main__":
    main()
