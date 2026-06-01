# ============================================
# 题目22：日期与时间
# 知识点：datetime / date / time / timedelta / strftime
# ============================================

from datetime import datetime, date, time, timedelta
import time as time_module

# --- date 对象 ---
print("=== date 对象 ===")
today = date.today()
print(f"今天：{today}")
print(f"年：{today.year}，月：{today.month}，日：{today.day}")
print(f"星期几（0=周一）：{today.weekday()}")
print(f"ISO 星期几（1=周一）：{today.isoweekday()}")

d = date(2024, 1, 15)
print(f"指定日期：{d}")
print(f"ISO 格式：{d.isoformat()}")

# --- time 对象 ---
print("\n=== time 对象 ===")
t = time(14, 30, 45)
print(f"时间：{t}")
print(f"小时：{t.hour}，分钟：{t.minute}，秒：{t.second}")

t2 = time(9, 0, 0, microsecond=500000)
print(f"带微秒：{t2}")

# --- datetime 对象（日期+时间）---
print("\n=== datetime 对象 ===")
now = datetime.now()
print(f"当前时间：{now}")
print(f"年：{now.year}，月：{now.month}，日：{now.day}")
print(f"时：{now.hour}，分：{now.minute}，秒：{now.second}")

dt = datetime(2024, 6, 15, 14, 30, 0)
print(f"指定时间：{dt}")

# 从 date 和 time 合并
combined = datetime.combine(date(2024, 6, 15), time(14, 30))
print(f"合并：{combined}")

# --- 格式化输出 strftime ---
print("\n=== strftime 格式化 ===")
dt = datetime(2024, 6, 15, 14, 30, 45)

# 常用格式码
formats = [
    ("%Y-%m-%d", "ISO 日期"),
    ("%d/%m/%Y", "欧式日期"),
    ("%Y年%m月%d日", "中文日期"),
    ("%H:%M:%S", "24小时时间"),
    ("%I:%M:%S %p", "12小时时间"),
    ("%Y-%m-%d %H:%M:%S", "完整日期时间"),
    ("%A", "英文星期"),
    ("%B %d, %Y", "英文月份"),
    ("%j", "一年中的第几天"),
    ("%W", "一年中的第几周"),
]
for fmt, desc in formats:
    print(f"  {desc}: {dt.strftime(fmt)}")

# --- 解析字符串 strptime ---
print("\n=== strptime 解析 ===")
date_str = "2024-06-15 14:30:45"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"解析结果：{parsed}")
print(f"类型：{type(parsed)}")

# 各种格式
formats_to_parse = [
    ("15/06/2024", "%d/%m/%Y"),
    ("June 15, 2024", "%B %d, %Y"),
    ("2024年06月15日", "%Y年%m月%d日"),
]
for s, fmt in formats_to_parse:
    d = datetime.strptime(s, fmt)
    print(f"  '{s}' -> {d.date()}")

# --- timedelta（时间差）---
print("\n=== timedelta ===")
delta1 = timedelta(days=30)
delta2 = timedelta(hours=2, minutes=30)
delta3 = timedelta(weeks=1, days=3)

print(f"30天后：{datetime.now() + delta1}")
print(f"2小时30分：{delta2}")
print(f"1周3天 = {delta3.days} 天")

# 计算两个日期之差
start = date(2024, 1, 1)
end = date(2024, 12, 31)
diff = end - start
print(f"相差 {diff.days} 天")

# 判断是否已过期
deadline = datetime(2024, 12, 31, 23, 59, 59)
now = datetime(2024, 6, 15, 10, 0, 0)     # 模拟当前时间
if now < deadline:
    remaining = deadline - now
    print(f"距离截止还有 {remaining.days} 天")
else:
    print("已过期")

# --- 时间戳 ---
print("\n=== 时间戳 ===")
import time as t
ts = t.time()               # Unix 时间戳（秒数）
print(f"时间戳：{ts:.0f}")

# 时间戳 -> datetime
dt = datetime.fromtimestamp(ts)
print(f"datetime：{dt}")

# datetime -> 时间戳
ts2 = datetime(2024, 6, 15).timestamp()
print(f"时间戳：{ts2:.0f}")

# --- 实用案例：计算年龄 ---
print("\n=== 计算年龄 ===")
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1            # 今年还没过生日
    return age

birthday = date(1995, 8, 20)
print(f"生日 {birthday}，年龄：{calculate_age(birthday)} 岁")

# --- 性能计时 ---
print("\n=== 性能计时 ===")
import time
start = time.perf_counter()
result = sum(range(1000000))
end = time.perf_counter()
print(f"计算耗时：{(end - start)*1000:.2f} 毫秒")
