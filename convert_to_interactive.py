# -*- coding: utf-8 -*-
"""
批量转换脚本：将学习文件改为菜单式交互形式
"""

import os
import re
from pathlib import Path


def extract_sections(content):
    """从文件内容中提取各个部分"""
    sections = []
    
    # 匹配 # === 开头的部分
    pattern = r'# =+\n# (.*?)\n# =+(.*?)\n(?=# =|\Z)'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        body = match.group(2).strip()
        sections.append({
            'title': title,
            'body': body,
            'index': i + 1
        })
    
    return sections


def create_interactive_file(day_num, original_content):
    """创建交互式文件内容"""
    # 提取文件顶部的docstring
    docstring_match = re.search(r'^"""(.*?)"""', original_content, re.DOTALL)
    docstring = docstring_match.group(1) if docstring_match else f"Day {day_num}"
    
    # 提取学习目标
    goal_match = re.search(r'学习目标[：:](.+)', original_content)
    goal = goal_match.group(1).strip() if goal_match else ""
    
    # 提取各个部分
    sections = extract_sections(original_content)
    
    if not sections:
        return None
    
    # 生成新的文件内容
    new_content = f'# -*- coding: utf-8 -*-\n"""\nDay {day_num}: {docstring.strip()}\n"""\n\n'
    
    # 生成section函数
    for section in sections:
        func_name = f"section{section['index']}"
        new_content += f"\ndef {func_name}():\n"
        new_content += f'    """{section["title"]}"""\n'
        new_content += f'    print("\\n" + "="*60)\n'
        new_content += f'    print("{section["title"]}")\n'
        new_content += f'    print("="*60)\n'
        
        # 处理body，添加缩进
        body_lines = section['body'].split('\n')
        for line in body_lines:
            if line.strip():
                # 保留原有的注释和代码
                new_content += f"    {line}\n"
        
        new_content += "\n"
    
    # 添加实战任务函数
    new_content += '''def practice_task():
    """实战任务"""
    print("\\n" + "="*60)
    print("实战任务")
    print("="*60)
    print("请修改代码完成任务...")


def show_answer():
    """显示参考答案"""
    print("\\n" + "="*60)
    print("参考答案")
    print("="*60)
    print("请参考原文件中的答案部分")


def show_summary():
    """显示学习总结"""
    print("\\n" + "="*60)
    print("学习总结")
    print("="*60)
    print("请参考原文件中的总结部分")

'''
    
    # 添加主菜单
    new_content += '''def main():
    """主菜单"""
    while True:
        print("\\n" + "="*60)
        print("Day {day_num}: 学习菜单")
        print("="*60)
'''
    
    for section in sections:
        new_content += f'        print("{section["index"]}. {section["title"]}")\n'
    
    new_content += '''        print("9. 实战任务")
        print("8. 参考答案")
        print("7. 学习总结")
        print("0. 退出")
        print("="*60)
        
        choice = input("\\n请选择 (0-9): ").strip()
        
'''
    
    for section in sections:
        new_content += f'        if choice == "{section["index"]}":\n'
        new_content += f'            section{section["index"]}()\n'
    
    new_content += '''        elif choice == "9":
            practice_task()
        elif choice == "8":
            show_answer()
        elif choice == "7":
            show_summary()
        elif choice == "0":
            print("\\n感谢学习！再见！")
            break
        else:
            print("\\n无效选择，请重新输入")
        
        input("\\n按回车键继续...")


if __name__ == "__main__":
    main()
'''
    
    return new_content


def main():
    """主函数"""
    base_dir = Path("c:/Users/user/Desktop/jiaoben/xuexi/python_learning")
    
    # 处理day03到day21
    for day_num in range(3, 22):
        day_str = f"day{day_num:02d}"
        file_path = base_dir / day_str / "lesson.py"
        
        if file_path.exists():
            print(f"处理 {day_str}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = create_interactive_file(day_num, content)
            
            if new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ✓ {day_str} 已转换")
            else:
                print(f"  ✗ {day_str} 无法转换（未找到部分）")
        else:
            print(f"  ✗ {day_str} 文件不存在")
    
    print("\n转换完成！")


if __name__ == "__main__":
    main()
