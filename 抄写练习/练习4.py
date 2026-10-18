fruits = ["苹果","香蕉","橙子","葡萄","芒果"]
numbers = [3,1,4,1,5,9,2,6]
mixed = [1,"hello",True,3.14,None]
empty = []

print(fruits)
print(numbers)
print(len(fruits))

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[::-1])

#末尾插入append
fruits.append("草莓")
print(fruits)
#insert，下标处插入
fruits.insert(1,"西瓜")
print(fruits)
#批量添加
others = ["柠檬","樱桃"]
fruits.extend(others)
print(fruits)


#删除第一个匹配值
fruits.remove("西瓜") 
print(fruits)

#弹出最后一个元素
poppen = fruits.pop()
print(f"弹出了：{poppen}")
print(fruits)

#弹出下标1的元素
popped2 = fruits.pop(1)
print(f"弹出了：{popped2}")
print(fruits)


del fruits[0]
print(fruits)


fruits[0] = "蓝莓"
print(fruits)

fruits[1:3] = ["桃子","梨"]
print(fruits)


nums = [10,20,30,20,40]
#判断是否存在
print(20 in nums)
#返回第一个20的下标：1
print(nums.index(20))
#统计出现次数：2
print(nums.count(20))
#升序
nums =[3,1,4,1,5,9,2,6]
nums.sort()
print(nums)
#降序
nums.sort(reverse=True)
print(nums)

#创建新列表
nums2 = [3,1,4,1,5]
sorted_nums = sorted(nums2)
print(f"原列表：{nums2}")
print(f"新列表：{sorted_nums}")
#按字符串长度排序
words = ["banana","fig","apple","kiwi"]
words.sort(key=len)
print(words)

a = [1,2,3]
b = [4,5,6]
print(a + b) #拼接
print(a * 3) #重复
print(min(a),max(a))
print(sum(a))

a.reverse() #原地反转
print(a)

c = a.copy() #浅拷贝
print(c)

a.clear()  #清空列表
print(a)


