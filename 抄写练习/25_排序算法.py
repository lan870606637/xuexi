# ============================================
# 题目25：排序算法
# 知识点：冒泡排序 / 选择排序 / 插入排序 / 快速排序
# ============================================

import time
import random

# --- 冒泡排序 ---
# 思路：相邻元素比较，大的往右冒泡，每轮确定最大值
# 时间复杂度：O(n²)
print("=== 冒泡排序 ===")
def bubble_sort(arr):
    arr = arr.copy()        # 不修改原数组
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):  # 每轮少比一个（已排好的）
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:     # 没有发生交换，已经有序，提前退出
            break
    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print(f"排序前：{data}")
print(f"排序后：{bubble_sort(data)}")

# --- 选择排序 ---
# 思路：每轮找到最小值，放到已排序部分的末尾
# 时间复杂度：O(n²)，交换次数少
print("\n=== 选择排序 ===")
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):  # 在未排序部分找最小值
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 交换
    return arr

data = [64, 25, 12, 22, 11]
print(f"排序前：{data}")
print(f"排序后：{selection_sort(data)}")

# --- 插入排序 ---
# 思路：像打牌，将元素插入到已排序部分的正确位置
# 时间复杂度：O(n²)，但近乎有序时近似 O(n)
print("\n=== 插入排序 ===")
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]        # 当前要插入的元素
        j = i - 1
        while j >= 0 and arr[j] > key:  # 找到插入位置
            arr[j + 1] = arr[j]         # 元素后移
            j -= 1
        arr[j + 1] = key    # 插入
    return arr

data = [5, 2, 4, 6, 1, 3]
print(f"排序前：{data}")
print(f"排序后：{insertion_sort(data)}")

# --- 快速排序 ---
# 思路：选基准值，分成两半，递归排序
# 时间复杂度：平均 O(n log n)，最坏 O(n²)
print("\n=== 快速排序 ===")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]      # 选中间元素为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = [3, 6, 8, 10, 1, 2, 1]
print(f"排序前：{data}")
print(f"排序后：{quick_sort(data)}")

# 原地快排（更省内存）
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- Python 内置排序 ---
print("\n=== Python 内置排序（Timsort）===")
data = [5, 2, 8, 1, 9, 3]
print(sorted(data))             # 返回新列表
data.sort()                     # 原地排序
print(data)

# 自定义排序
students = [("张三", 85), ("李四", 92), ("王五", 78)]
students.sort(key=lambda x: x[1], reverse=True)  # 按成绩降序
print(students)

# 多关键字排序
from operator import attrgetter, itemgetter
students2 = [
    {"name": "张三", "age": 20, "score": 85},
    {"name": "李四", "age": 22, "score": 92},
    {"name": "王五", "age": 20, "score": 78},
]
# 先按年龄升序，再按成绩降序
result = sorted(students2, key=lambda x: (x["age"], -x["score"]))
for s in result:
    print(f"  {s['name']}: {s['age']}岁, {s['score']}分")

# --- 性能比较 ---
print("\n=== 性能比较 ===")
size = 1000
test_data = [random.randint(0, 10000) for _ in range(size)]

algorithms = [
    ("冒泡排序", bubble_sort),
    ("选择排序", selection_sort),
    ("插入排序", insertion_sort),
    ("快速排序", quick_sort),
    ("内置sorted", sorted),
]

for name, func in algorithms:
    data_copy = test_data.copy()
    start = time.perf_counter()
    func(data_copy)
    end = time.perf_counter()
    print(f"  {name}: {(end-start)*1000:.2f}ms")
