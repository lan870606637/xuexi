# ============================================
# 题目24：递归
# 知识点：递归函数 / 终止条件 / 经典递归问题
# ============================================

import sys
sys.setrecursionlimit(10000)    # 默认是1000，可以调大

# --- 递归的两个要素 ---
# 1. 终止条件（base case）：什么时候停止
# 2. 递归步骤：把问题分解为更小的子问题

# --- 阶乘 ---
print("=== 阶乘 ===")
def factorial(n):
    if n <= 1:              # 终止条件
        return 1
    return n * factorial(n - 1)   # 递归调用

for i in range(1, 8):
    print(f"{i}! = {factorial(i)}")

# --- 斐波那契数列 ---
print("\n=== 斐波那契（朴素递归）===")
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 加记忆化（缓存），避免重复计算
print("\n=== 斐波那契（记忆化）===")
from functools import lru_cache

@lru_cache(maxsize=None)    # 缓存所有结果
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print([fib_memo(i) for i in range(10)])
print(f"fib(40) = {fib_memo(40)}")     # 很快！

# --- 求幂 ---
print("\n=== 快速幂 ===")
def power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half       # 利用对称性，减少乘法次数
    return base * power(base, exp - 1)

print(power(2, 10))         # 1024
print(power(3, 5))          # 243

# --- 汉诺塔 ---
print("\n=== 汉诺塔 ===")
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"  移动盘子 1：{source} -> {target}")
        return
    hanoi(n - 1, source, auxiliary, target)     # 把 n-1 个移到辅助柱
    print(f"  移动盘子 {n}：{source} -> {target}")  # 移动最大盘
    hanoi(n - 1, auxiliary, target, source)     # 把 n-1 个从辅助柱移到目标

hanoi(3, "A", "C", "B")

# --- 二分查找（递归版）---
print("\n=== 二分查找 ===")
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1                   # 未找到
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(nums, 7))     # 3
print(binary_search(nums, 12))    # -1

# --- 合并排序（递归经典）---
print("\n=== 合并排序 ===")
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [38, 27, 43, 3, 9, 82, 10]
print(f"排序前：{nums}")
print(f"排序后：{merge_sort(nums)}")

# --- 目录树打印 ---
print("\n=== 树形打印 ===")
tree = {
    "root": {
        "src": {
            "main.py": None,
            "utils.py": None,
        },
        "tests": {
            "test_main.py": None,
        },
        "README.md": None,
    }
}

def print_tree(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    if isinstance(node, dict):
        for i, (key, val) in enumerate(node.items()):
            is_last_item = (i == len(node) - 1)
            print(prefix + connector + key)
            if isinstance(val, dict):
                extension = "    " if is_last else "│   "
                print_tree(val, prefix + extension, is_last_item)

for key, val in tree.items():
    print(key)
    print_tree(val)

# --- 递归 vs 迭代的选择 ---
print("\n=== 递归 vs 迭代 ===")
# 迭代版阶乘（通常更高效）
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iter(10))   # 3628800

# 规则：
# - 树形/图形结构 -> 递归更自然
# - 线性处理（列表） -> 迭代更高效
# - 深度超过1000层 -> 要避免递归或用迭代实现
