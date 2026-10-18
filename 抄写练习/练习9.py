count = 0
while count < 5:
    print(count,end="")
    count +=1
print()


n = 5
while n > 0:
    print(f"{n}....")
    n -= 1
print("发射！")

total = 0
i = 1
while i <=100:
    total +=i
    i += 1
print(f"1到100的和：{total}")


secret =42
guess = 0
attempts = 0
guesses = [10,55,42,30]

for g in guesses:
    guess = g
    attempts += 1
    if guess == secret:
        print(f"猜对了！答案是{secret}，用了{attempts}次")
        break
    elif guess < secret:
        print(f"{guess}太小了")
    else:
        print(f"{guess}太大了")

#跳过3的倍数
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue
    print(n, end=" ")
print()


items = [3,7,2,8,1]
target = 6
i = 0
while i < len(items):
    if items[i] == target:
        print(f"找到了{target}，在下标{i}")
        break
    i+=1
else:
    print(f"{target}不在列表中")


commands = ["open","save","quit"]
index = 0
while True:
    cmd = commands[index]
    index += 1
    print(f"执行命令：{cmd}")
    if cmd == "quit":
        print("程序退出")
        break

num = 12345
digits = []
n
while num > 0:
    digits.append(num % 10)
    num //=10
digits.reverse()
print(digits)


a,b = 48,18
while b != 0:
    a,b =b,a % b
print(f"最大公约数{a}")


count = 0 
while True:
    count+=1
    print(f"第{count}次执行")
    if count >= 3:
        break


     



