fruits = ["苹果","香蕉","橙子","葡萄"]
for fruit in fruits:
    print(fruit)


for i in range(5):
    print(i, end="")
print()


#步长为2
for i in range(0,10,2):
    print(i,end=" ")
print()



for i in range(1,6):
    print(i,end="")
print()


#倒序
for i in range(10,0,-1):
    print(i,end="")
print()

#enumerate同时取下标和值
for index, fruit in enumerate[str](fruits):
    print(f"{index}:{fruit}")

for index,fruit in enumerate[str](fruits,start=1):
    print(f"{index}.{fruit}")


#zip同时遍历多个序列
names = ["张三","李四","王五"]
scores = [85,92,78]
grades = ["B","A","C"]


for name, score,grade in zip(names,scores,grades):
        print(f"{name}：{score}分（{grade}）")


#zip以最短的为准
a =[1,2,3,4]
b= ["a","b","c"]
for x,y in zip(a,b):
    print(x,y)

for i  in range(10):
    if i == 5:
        print(f"找到了{i}，停止搜索")
        break
    print(i,end="")
print()

for i in range(10):
    if i%2 ==0:
        continue
    print(i,end="")
print()


target = 7

for i in range(5):
    if i == target:
        print(f"找到{target}")
        break
else:
    print(f"没有找到{target}")

#嵌套循环，乘法表
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}*{j}={i*j}",end="  ")
    print()

#遍历字符串
for char in "Python":
    print(char,end=" ")
print()

#遍历字典
config = {"host":"localhost","port":3306,"db":"mydb"}
for key, value in config.items():
    print(f"{key}={value}")

#求和
total = 0
for i in range(1, 101):
    total +=i
print(f"1到100的和：{total}")


#收集平方到列表
squares = []
for i in range(1,6):
    squares.append(i ** 2)
print(squares)


