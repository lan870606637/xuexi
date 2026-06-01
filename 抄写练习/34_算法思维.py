# ============================================
# 题目34：经典算法思维
# 知识点：双指针 / 滑动窗口 / 哈希表 / 贪心
# ============================================

# --- 双指针：两数之和（有序数组）---
print("=== 双指针：两数之和 ===")
def two_sum_sorted(arr, target):
    """在有序数组中找两个数使其和等于 target"""
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return left, right
        elif current < target:
            left += 1           # 总和太小，移动左指针
        else:
            right -= 1          # 总和太大，移动右指针
    return None

arr = [1, 2, 3, 4, 6, 8, 9]
result = two_sum_sorted(arr, 10)
if result:
    l, r = result
    print(f"找到：{arr[l]} + {arr[r]} = 10，下标：({l}, {r})")

# 哈希表法：无序数组，O(n) 时间
def two_sum(arr, target):
    seen = {}                   # value -> index
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None

arr2 = [3, 6, 2, 8, 1, 9]
l, r = two_sum(arr2, 10)
print(f"无序找到：{arr2[l]} + {arr2[r]} = 10，下标：({l}, {r})")

# --- 双指针：反转字符串中的单词 ---
print("\n=== 反转单词 ===")
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("  hello world Python  "))

# --- 滑动窗口：最长无重复子串 ---
print("\n=== 滑动窗口：最长无重复子串 ===")
def length_of_longest_substring(s):
    char_index = {}
    max_len = 0
    left = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1     # 移动左边界跳过重复字符
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

tests = ["abcabcbb", "bbbbb", "pwwkew", ""]
for t in tests:
    print(f"  '{t}' -> {length_of_longest_substring(t)}")

# --- 滑动窗口：定长窗口最大和 ---
print("\n=== 固定窗口：连续 k 个数的最大和 ===")
def max_sum_k(arr, k):
    if len(arr) < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_start = 0
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # 滑动：加新元素，去旧元素
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1
    return max_sum, arr[max_start:max_start + k]

arr = [2, 1, 5, 1, 3, 2]
result = max_sum_k(arr, 3)
print(f"连续3个最大和：{result[0]}，子数组：{result[1]}")

# --- 哈希表：字符频率 / 变位词 ---
print("\n=== 变位词判断 ===")
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    from collections import Counter
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False
print(is_anagram("anagram", "nagaram")) # True

# --- 贪心：找零钱（最少硬币数）---
print("\n=== 贪心：找零 ===")
def min_coins_greedy(amount, coins):
    """贪心法：优先用大面值硬币（仅适用于特定面值组合）"""
    coins = sorted(coins, reverse=True)
    result = []
    remaining = amount
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    return result if remaining == 0 else None

coins = [1, 5, 10, 25, 50]
change = min_coins_greedy(87, coins)
print(f"87分 = {change}")               # [50, 25, 10, 1, 1]

# --- 动态规划：零钱问题（通用解法）---
print("\n=== DP：最少硬币数 ===")
def coin_change_dp(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    return dp[amount] if dp[amount] != float('inf') else -1

print(f"11分最少硬币数：{coin_change_dp(11, [1, 5, 6, 9])}")  # 2（5+6）

# --- 二分查找：找峰值 ---
print("\n=== 找峰值 ===")
def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1          # 右侧更大，峰值在右边
        else:
            right = mid             # 峰值在左边（包括 mid）
    return left, arr[left]

arr = [1, 3, 7, 5, 2, 8, 4]
idx, val = find_peak(arr)
print(f"峰值：{val}，下标：{idx}")

# --- 前缀和：区间求和 ---
print("\n=== 前缀和 ===")
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix

def range_sum(prefix, left, right):   # 查询 [left, right] 的和，O(1)
    return prefix[right + 1] - prefix[left]

arr = [3, 1, 4, 1, 5, 9, 2, 6]
prefix = build_prefix(arr)
print(f"原数组：{arr}")
print(f"[2, 5] 区间和：{range_sum(prefix, 2, 5)}")   # 4+1+5+9 = 19
print(f"[0, 3] 区间和：{range_sum(prefix, 0, 3)}")   # 3+1+4+1 = 9
