point = (3,4)
rgb = (255,128,0)
single = (42,)
empty_tuple = ()

print(point,rgb)
print(type(single))
print(type((42)))

print(rgb[0])
print(rgb[-1])
print(rgb[0:2])

x,y = point
print(f"x={x},y={y}")

r,g,b=rgb
print(f"R={r},G={g},B={b}")


first,*rest = (1,2,3,4,5)
print(f"first={first},rest={rest}")

*init,last = (1,2,3,4,5)
print(f"init ={init},last ={last}")

a,*middle, z = (1,2,3,4,5)
print(f"a={a},middle={middle},z={z}")

nums = (1,2,3,2,4,2)
print(nums.count(2))
print(nums.index(3))
print(len(nums))

#元组转换成列表
lst = list(point)
lst.append(0)
#列表转换成元组
tpl = tuple(lst)
print(tpl)


coords = {(0,0):"原点",(1,0):"右",(0,1):"上"}
print(coords[(0,0)])

fruits = {"苹果","香蕉","橙子","苹果"}
print(fruits)
print(type(fruits))

#创建空集合
empty_set = set()
#从列表创建集合，自动去重
nums_set = set([1,2,2,3,3,3])
print(nums_set)

fruits.add("葡萄")
print(fruits)

fruits.discard("香蕉")
fruits.discard("榴莲") 
print(fruits)


fruits.remove("橙子")
print(fruits)

popped = fruits.pop()
print(f"弹出：{popped}")

A = {1,2,3,4,5}
B = {3,4,5,6,7}

#并集
print(f"{A | B}")
#交集
print(f"{A & B}")
#差集 A有B没有
print(f"{A - B}")
#对称差集：只在一个集合中
print(f"{A ^ B}")


print(A.union(B))#并集
print(A.intersection(B))#交集
print(A.difference(B))#差集 A有B没有
print(A.symmetric_difference(B))#对称差集：只在一个集合中

small = {1,2,3}
big = {1,2,3,4,5}
print(small.issubset(big))
print(big.issuperset(small))
print(small.isdisjoint({6,7}))


data = [1,3,2,3,1,4,2,5]
unique = list(set(data))
print(unique)


