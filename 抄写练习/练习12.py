#普通函数
from functools import reduce


def square(x):
    return x * x


square_l = lambda x: x * x
print(square(5))
print(square_l(5))


add = lambda a,b:a+b
print(add(3,4))

is_even = lambda x: x%2==0
print(is_even(4))
print(is_even(7))



students = [
    {"name":"张三","score":85,"age":20},
    {"name":"李四","score":92,"age":22},
    {"name":"王五","score":78,"age":19},
    {"name":"赵六","score":92,"age":21},

]

#按成绩排序
by_score = sorted(students,key=lambda s: s["score"])
for st in by_score:
    print(f"{st['name']}:{st['score']}")


#按成绩降序，成绩相同按年龄升序
by_multi = sorted(students, key=lambda s: (-s["score"],s["age"]))
for st in by_multi:
    print(f"{st['name']}:{st['score']},{st['age']}岁")

#字符串处理
nums = [1,2,3,4,5]

squared = list(map(lambda x:x**2,nums))
print(squared)


words = ["hello","world","python"]
upper = list(map(str.upper,words))
print(upper)

a = [1,2,3]
b = [10,20,30]
sums = list(map(lambda x,y:x+y,a,b))
print(sums)


#filter()过滤元素
nums = range(1,11)

evens = list(filter(lambda x:x%2==0,nums))
print(evens)

names = ["Alice","","Bob",None,"Charlie",""]
valid = list(filter(None,names))
print(valid)

mixed = [-3,-1,0,2,4,-5,6]
positives = list(filter(lambda x: x >0,mixed))
print(positives)

#累积计算reduce
nums = [1,2,3,4,5]

product = reduce(lambda a,b : a*b,nums)
print(f"连乘{product}")

#求最大值
maximum = reduce (lambda a,b: a if a>b else b,nums)
print(f"最大值：{maximum}")

#带初始值
total = reduce(lambda a,b:a+b,nums,100)
print(f"从100开始累加：{total}")


#sorted()的高级用法
words = ["banana","fig","apple","cherry","date"]
#按长度排序
print(sorted(words,key=len))

#按最后一个字母排序
print(sorted(words,key=lambda w:w[-1]))

mixed_case = ["Banana","apple","Cherry","date"]
print(sorted(mixed_case,key=str.lower))


#链式使用
data = [5,-3,8,-1,2,-7,4]

result = sorted(
    map(lambda x: x**2 ,filter(lambda x: x>0,data)),
    reverse=True

)
print(result)

result2 = sorted ([x**2 for x in data if x>0],reverse=True)
print(result2)


