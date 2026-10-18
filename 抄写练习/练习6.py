



person = {"name":"张三","age":25,"city":"北京"}
empty = {}
from_keys = dict.fromkeys(["a","b","c"],0)
print(person)
print(from_keys)

print(person["name"])
print(person.get("name"))
print(person.get("age"))
print(person.get("email"))
print(person.get("email","未填写"))

#添加
person["email"] = "zhangsan@example.com"
#修改已有
person["age"] = 26
print(person)
#批量更新
person.update({"city":"上海","phone":"13922222222"})
print(person)

#删除并返回值
removed = person.pop("phone")
print(f"删除了：{removed}")
print(person)

#删除键值对
del person["email"]
print(person)

#删除并返回最后插入的键值对
last = person.popitem()
print(f"删除了：{last}")


#遍历
scores = {"语文":88,"数学": 95,"英语":72}


for key in scores:
    print(key, end="  ")
print()

for key,value in scores.items():
    print(f"{key}:{value}分")

d = {"a":1,"b":2,"c":3}
print(d.keys())
print(d.values())
print(d.items())
print(list(d.keys()))

print("a" in d)
print(1 in d.values())
print(len(d))

config = {"host":"localhost"}
config.setdefault("prot",3306)
config.setdefault("host","remote")
print(config)


students ={
    "S001":{"name":"小红","score":92},
    "S002":{"name":"小明","score":85},
    "S003":{"name":"小李","score":78},
}

print(students["S001"]["name"])
print(students["S001"]["score"])
print(students.items())
for sid,info in students.items():
    print(f"{sid}:{info['name']}-{info['score']}分")


best = max(students.values(), key=lambda x: x["score"])
print(f"最高分：{best['name']}  {best['score']}分")



a ={"x":1,"y":2}
b ={"y":99,"z":3}
merged = a | b
print(merged)