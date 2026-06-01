# ============================================
# 题目32：数据处理实战
# 知识点：综合运用字典/列表/推导式/排序/统计
# ============================================

import statistics
from collections import Counter, defaultdict

# --- 原始数据：学生成绩单 ---
students = [
    {"name": "张三", "class": "A班", "age": 20, "scores": {"语文": 85, "数学": 92, "英语": 78}},
    {"name": "李四", "class": "B班", "age": 22, "scores": {"语文": 91, "数学": 65, "英语": 88}},
    {"name": "王五", "class": "A班", "age": 19, "scores": {"语文": 72, "数学": 88, "英语": 76}},
    {"name": "赵六", "class": "B班", "age": 21, "scores": {"语文": 95, "数学": 73, "英语": 82}},
    {"name": "小明", "class": "A班", "age": 20, "scores": {"语文": 68, "数学": 95, "英语": 90}},
    {"name": "小红", "class": "B班", "age": 23, "scores": {"语文": 88, "数学": 79, "英语": 93}},
    {"name": "小李", "class": "A班", "age": 21, "scores": {"语文": 76, "数学": 84, "英语": 69}},
    {"name": "小王", "class": "B班", "age": 20, "scores": {"语文": 82, "数学": 90, "英语": 77}},
]

# --- 1. 计算每个学生的总分和平均分 ---
print("=== 1. 个人成绩 ===")
for s in students:
    total = sum(s["scores"].values())
    avg = total / len(s["scores"])
    s["total"] = total
    s["avg"] = round(avg, 1)

for s in sorted(students, key=lambda x: x["total"], reverse=True):
    print(f"  {s['name']}（{s['class']}）：{s['total']}分，平均 {s['avg']}分")

# --- 2. 各班排名 ---
print("\n=== 2. 各班排名 ===")
by_class = defaultdict(list)
for s in students:
    by_class[s["class"]].append(s)

for cls in sorted(by_class.keys()):
    print(f"\n{cls}：")
    ranked = sorted(by_class[cls], key=lambda x: x["total"], reverse=True)
    for rank, s in enumerate(ranked, 1):
        print(f"  第{rank}名：{s['name']}，{s['total']}分")

# --- 3. 各科目统计 ---
print("\n=== 3. 各科目统计 ===")
subjects = ["语文", "数学", "英语"]
for subject in subjects:
    scores = [s["scores"][subject] for s in students]
    print(f"\n{subject}：")
    print(f"  最高分：{max(scores)} ({next(s['name'] for s in students if s['scores'][subject] == max(scores))})")
    print(f"  最低分：{min(scores)} ({next(s['name'] for s in students if s['scores'][subject] == min(scores))})")
    print(f"  平均分：{statistics.mean(scores):.1f}")
    print(f"  中位数：{statistics.median(scores):.1f}")
    print(f"  标准差：{statistics.stdev(scores):.1f}")

# --- 4. 成绩等级分布 ---
print("\n=== 4. 成绩等级分布 ===")
def get_grade(score):
    if score >= 90: return "A（优秀）"
    elif score >= 80: return "B（良好）"
    elif score >= 70: return "C（中等）"
    elif score >= 60: return "D（及格）"
    else: return "F（不及格）"

all_scores = [score for s in students for score in s["scores"].values()]
grade_counts = Counter(get_grade(score) for score in all_scores)
for grade, count in sorted(grade_counts.items()):
    bar = "█" * count
    print(f"  {grade}: {bar} ({count}人)")

# --- 5. 找出偏科严重的学生 ---
print("\n=== 5. 偏科分析 ===")
for s in students:
    scores = list(s["scores"].values())
    spread = max(scores) - min(scores)
    if spread >= 20:
        subjects_detail = ", ".join(f"{k}:{v}" for k, v in s["scores"].items())
        print(f"  {s['name']}：最高-最低差距 {spread}分 ({subjects_detail})")

# --- 6. 年龄与成绩相关性 ---
print("\n=== 6. 按年龄分组 ===")
by_age = defaultdict(list)
for s in students:
    by_age[s["age"]].append(s)

for age in sorted(by_age.keys()):
    group = by_age[age]
    avg_score = statistics.mean(s["avg"] for s in group)
    names = ", ".join(s["name"] for s in group)
    print(f"  {age}岁（{names}）：平均分 {avg_score:.1f}")

# --- 7. 综合排行榜 ---
print("\n=== 7. 全校排行榜 ===")
header = f"{'排名':>4}  {'姓名':>6}  {'班级':>4}  {'语文':>4}  {'数学':>4}  {'英语':>4}  {'总分':>4}  {'等级':>8}"
print(header)
print("-" * len(header))

overall = sorted(students, key=lambda x: x["total"], reverse=True)
for rank, s in enumerate(overall, 1):
    grade = get_grade(s["avg"])
    print(f"  {rank:>2}  {s['name']:>4}  {s['class']:>4}  "
          f"{s['scores']['语文']:>4}  {s['scores']['数学']:>4}  "
          f"{s['scores']['英语']:>4}  {s['total']:>4}  {grade}")
