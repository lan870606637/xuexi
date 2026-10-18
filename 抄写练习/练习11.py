
#普通写法
squares = []
for i in range(1,6):
    squares.append(i ** 2)
print(squares)

#推导式写法
squares = [i ** 2 for i in range(1,6)]
print(squares)

# 带条件的推导式
evens = [i for i in range(20) if i % 2 == 0]
print(evens)

#字符串操作
words = ["hello","world","python"]
upper_words =[w.upper() for w in words]
print(upper_words)

#过滤空字符串
names = ["Alice","Bob","","Charlie","","Dave"]
non_empty = [name for name in names if name]
print(non_empty)


nums =[-3,-2,-1,0,1,2,3]
result = [x if x>0 else 0 for x in nums]
print(result)

labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1,7)]
print(labels)

# 二维列表展平 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

#创建二维矩阵
grid = [[i * j for j in range(1,4)] for i in range(1,4)]
for row in grid:
    print(row)

#字典推导式
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)

#键值互换
original = {"a":1,"b":2,"c":3}
inverted = {v: K for  K, v in original.items()}
print(inverted)

#带条件过滤
scores = {"张三": 55, "李四": 82, "王五": 91, "赵六": 67}
pass_scores = {name: s for name, s in scores.items() if s>=60}
print(pass_scores)

#统计字符频率
text = "hello world"
char_count = {c:text.count(c) for c in set(text) if c !=" "}
print(char_count)

#集合推导式，自动去重    {表达式  for 变量 in  可迭代对象}
unique_squares = {x**2 for x in [-3,-2,-1,0,1,2,3]}
print(unique_squares)

#生成器表达式，不立即计算所以值，按需生成
gen = (x**2 for x in range(1, 6))
print(gen)

for val in gen:
    print(val,end=" ")
print()

# any() 和 all() 配合生成器表达式
nums = [2,4,5,6,-7]
print(any(n%2 !=0 for n in nums))  #any一个是真则真
print(all(n>0 for n in nums))   #all 全都是真则真

# 找出所有 3 位回文数
palindromes = [n for n in range(100, 1000) if str(n) == str(n)[::-1]]
print(f"3位回文数个数：{len(palindromes)}")
print(f"前10个：{palindromes[:10]}")








