# ============================================
# 题目04：列表基础操作
# 知识点：增删改查、排序、切片
# ============================================

# --- 创建列表 ---
fruits = ["苹果", "香蕉", "橙子", "葡萄", "芒果"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
mixed = [1, "hello", True, 3.14, None]   # 列表可以混合类型
empty = []

print("=== 创建列表 ===")
print(fruits)
print(mixed)
print(len(fruits))          # 长度

# --- 访问元素 ---
print("\n=== 访问元素 ===")
print(fruits[0])            # 第一个：苹果
print(fruits[-1])           # 最后一个：芒果
print(fruits[1:3])          # 切片：['香蕉', '橙子']
print(fruits[::-1])         # 反转列表

# --- 增加元素 ---
print("\n=== 增加元素 ===")
fruits.append("草莓")        # 末尾添加
print(fruits)

fruits.insert(1, "西瓜")    # 在下标1处插入
print(fruits)

others = ["柠檬", "樱桃"]
fruits.extend(others)        # 批量添加
print(fruits)

# --- 删除元素 ---
print("\n=== 删除元素 ===")
fruits.remove("西瓜")        # 删除第一个匹配值
print(fruits)

popped = fruits.pop()        # 弹出最后一个元素
print(f"弹出了：{popped}")
print(fruits)

popped2 = fruits.pop(1)     # 弹出下标1的元素
print(f"弹出了：{popped2}")
print(fruits)

del fruits[0]               # 用 del 删除
print(fruits)

# --- 修改元素 ---
print("\n=== 修改元素 ===")
fruits[0] = "蓝莓"
print(fruits)

fruits[1:3] = ["桃子", "梨"]  # 切片赋值，批量修改
print(fruits)

# --- 查找元素 ---
print("\n=== 查找元素 ===")
nums = [10, 20, 30, 20, 40]
print(20 in nums)           # True，判断是否存在
print(nums.index(20))       # 返回第一个 20 的下标：1
print(nums.count(20))       # 统计出现次数：2

# --- 排序 ---
print("\n=== 排序 ===")
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                 # 原地升序排序
print(nums)

nums.sort(reverse=True)     # 原地降序
print(nums)

nums2 = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums2) # 返回新列表，不修改原列表
print(f"原列表：{nums2}")
print(f"新列表：{sorted_nums}")

# 按字符串长度排序
words = ["banana", "fig", "apple", "kiwi"]
words.sort(key=len)         # key 指定排序依据
print(words)

# --- 其他常用操作 ---
print("\n=== 其他操作 ===")
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)                # 拼接：[1, 2, 3, 4, 5, 6]
print(a * 3)                # 重复：[1, 2, 3, 1, 2, 3, 1, 2, 3]
print(min(a), max(a))       # 最小、最大
print(sum(a))               # 求和

a.reverse()                 # 原地反转
print(a)

c = a.copy()                # 浅拷贝
print(c)

a.clear()                   # 清空列表
print(a)
