 
 #基础try/except

try:
    x =int("adb")
    print(x)
except ValueError:
    print("转换失败：不是有效的整数")

print("程序正常继续")


#捕获多种异常
def safe_divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误：参数类型不对")
        return None
print(safe_divide(10,2))
print(safe_divide(10,0))
print(safe_divide("10",2))


#获取异常信息
try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常信息：{e}")

#捕获所有异常，慎用
def risky_operation(data):
    try:
        return data["key"] * 10
    except Exception as e:
        print(f"发生异常：{type(e).__name__}:{e}")
        return None
risky_operation({"key": 5})
risky_operation({"other": 5})  
risky_operation("not a dict")  

#else子句（没有异常时执行）
def  read_number(s):
    try:
        num = int(s)
    except ValueError:
        print(f"'{s}'不是有效数字") 
    else:
        print(f"成功破解：{num*2}")

read_number("42")
read_number("adb")

# --- finally 子句（无论如何都执行）---
def process_file(filename):
    f = None
    try:
        f = open(filename,"r",encoding="utf-8")
        content = f.read()
        print(f"读取成功，{len(content)}个字符")
    except FileNotFoundError:
        print(f"文件不存在：{filename}")
    finally:
        if f:
            f.close()
            print("文件已关闭")


process_file("不存在的文件.txt")



# --- raise（主动抛出异常）---
def set_age(age):
    if not isinstance(age,int):
        raise TypeError(f"年龄必须是整数，收到：{type(age)}")
    if age < 0 or age > 150:
        raise ValueError(f"年龄{age}不在合理范围内（0-150）")
    return age

try:
    set_age(25)
    set_age(-5)
except ValueError as e:
    print(f"ValueError:{e}")

try:
    set_age("twenty")
except TypeError as e:
    print(f"TypeError:{e}")

# --- 自定义异常 ---
class InsufficientFundsError(Exception):
    def __init__(self,balance,amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：余额{balance},需要{amount}")

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance,amount)
        self.balance -= amount
        return amount

account = BankAccount("张三",100)


try:
    account.withdraw(50)
    print(f"取款成功，余额：{account.balance}")
    account.withdraw(80)
except InsufficientFundsError as e:
    print(f"操作失败：{e}")
    print(f"余额：{e.balance},尝试取款：{e.amount}")


#异常链（raise from）
def load_config(path):
    try:
        with open(path) as f:
            return  f.read()
    except  FileNotFoundError as e :
        raise RuntimeError(f"加载配置失败{path}") from e

try:
    load_config("config.json")
except RuntimeError as e:
    print(f"错误：{e}")
    print(f"原因：{e.__cause__}")