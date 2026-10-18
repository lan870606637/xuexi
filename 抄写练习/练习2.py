s = "Hello, python world!"
#统计字符长度
print(len(s))
#取第一个字符
print(s[0])
#取最后一个字符
print(s[-1])
#取下标7到12的字符
print(s[7:13])
#取前五个字符
print(s[:5])
#取下标第7个字符到结尾
print(s[7:])
#隔一个取一个
print(s[::2])
#所有字符反转后输出，就是从最后往前反着输出
print(s[::-1])
#隔2个字符取一个
print(s[::3])

#全大写
print(s.upper())
#全小写
print(s.lower())
#首字母大写
print(s.title())
#大小写互换
print(s.swapcase())

#查找返回下标7，找不到返回-1
print(s.find("python"))
#返回下标7，找不到报错
print(s.index("python"))
#统计出现次数
print(s.count("l"))
#Python匹配是否在s字符串里，匹配就是True
print("python" in s)
#字符串s是否是Hello开头，是就True
print(s.startswith("Hello"))
#字符串s是否是！结尾，是就True
print(s.endswith("!"))

#替换
print(s.replace("python","world"))
#替换第一个l
print(s.replace("l","L",1))

#按空格返回列表
words = s.split(" ")
print(words)
#按逗号返回列表
csv_line = "a,b,c,d"
print(csv_line.split(","))
#使用-拼接字符
joined = "-".join(["2024","01","01"])
print(joined)

padded = "   hello   "
#去除两端空白
print(padded.strip())
#只去左端
print(padded.lstrip())
#只去右端
print(padded.rstrip())


word = "hi"
print(word.center(10,"*"))
print(word.ljust(10,"-"))
print(word.rjust(10,"-"))
print("42".zfill(5))

#判断全数字，是就True
print("123".isdigit())
#判断全字母，是就True
print("adb".isalpha())
#判断字母或者数字
print("adc123".isalnum())
#判断全是空白
print("   ".isspace())



