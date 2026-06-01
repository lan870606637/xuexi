# ============================================
# 题目20：collections 模块
# 知识点：Counter / defaultdict / OrderedDict / deque / namedtuple
# ============================================

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

# --- Counter（计数器）---
print("=== Counter ===")
text = "hello world python programming"
char_count = Counter(text.replace(" ", ""))
print(char_count)

# 最常见的元素
print("\n最常见的5个字符：")
for char, count in char_count.most_common(5):
    print(f"  '{char}': {count}次")

# 单词频率
words = "the quick brown fox jumps over the lazy dog the fox".split()
word_count = Counter(words)
print(f"\n单词频率：{word_count}")
print(f"'the' 出现次数：{word_count['the']}")
print(f"最常见3个：{word_count.most_common(3)}")

# Counter 支持运算
c1 = Counter("aabbc")
c2 = Counter("bbbcc")
print(f"\nc1 + c2 = {c1 + c2}")    # 合并
print(f"c1 - c2 = {c1 - c2}")    # 差集（只保留正数）
print(f"c1 & c2 = {c1 & c2}")    # 交集（取最小值）
print(f"c1 | c2 = {c1 | c2}")    # 并集（取最大值）

# --- defaultdict（默认值字典）---
print("\n=== defaultdict ===")
# 普通字典访问不存在的键会报错
# defaultdict 会自动创建默认值

# 用 list 作为默认值
groups = defaultdict(list)
students = [("张三", "A班"), ("李四", "B班"), ("王五", "A班"), ("赵六", "B班"), ("小明", "A班")]
for name, cls in students:
    groups[cls].append(name)    # 不用先判断键是否存在

for cls, names in sorted(groups.items()):
    print(f"{cls}: {names}")

# 用 int 作为默认值（默认0，方便计数）
vote_count = defaultdict(int)
votes = ["A", "B", "A", "C", "A", "B", "A"]
for v in votes:
    vote_count[v] += 1          # 不用先判断键是否存在
print(f"\n投票结果：{dict(vote_count)}")

# 用 set 避免重复
tags = defaultdict(set)
items = [("item1", "red"), ("item2", "blue"), ("item1", "big"), ("item2", "red")]
for item, tag in items:
    tags[item].add(tag)
print(f"\n标签：{dict(tags)}")

# --- OrderedDict（有序字典）---
print("\n=== OrderedDict ===")
# Python 3.7+ 普通 dict 已经是有序的，但 OrderedDict 有额外功能
od = OrderedDict()
od["banana"] = 3
od["apple"] = 5
od["cherry"] = 1

# move_to_end：移到末尾或开头
od.move_to_end("banana")            # 移到末尾
print(f"移到末尾：{list(od.keys())}")

od.move_to_end("cherry", last=False)  # 移到开头
print(f"移到开头：{list(od.keys())}")

# --- deque（双端队列）---
print("\n=== deque ===")
dq = deque([1, 2, 3, 4, 5])
print(f"初始：{dq}")

dq.appendleft(0)        # 左端添加，O(1)
dq.append(6)            # 右端添加，O(1)
print(f"两端添加：{dq}")

dq.popleft()            # 左端弹出，O(1)
dq.pop()                # 右端弹出，O(1)
print(f"两端弹出：{dq}")

# 旋转
dq.rotate(2)            # 向右旋转2步
print(f"右旋转2：{dq}")
dq.rotate(-2)
print(f"左旋转2：{dq}")

# 限制大小的队列（固定长度）
buffer = deque(maxlen=3)  # 最多保留3个，超出从另一端自动删除
for i in range(6):
    buffer.append(i)
    print(f"  添加{i}：{buffer}")

# 用作队列（先进先出 FIFO）
print("\n队列 FIFO：")
queue = deque()
queue.append("任务1")
queue.append("任务2")
queue.append("任务3")
while queue:
    task = queue.popleft()
    print(f"  处理：{task}")

# --- namedtuple（命名元组）---
print("\n=== namedtuple ===")
# 像元组但字段有名字，比普通元组更可读
Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", "red green blue")  # 也可以用空格分隔字符串

p = Point(3, 4)
print(f"点：{p}")
print(f"x={p.x}, y={p.y}")     # 用名字访问
print(f"x={p[0]}, y={p[1]}")   # 也可以用下标

c = Color(255, 128, 0)
print(f"颜色：R={c.red}, G={c.green}, B={c.blue}")

# 转换为字典
print(p._asdict())              # {'x': 3, 'y': 4}

# 创建修改版本
p2 = p._replace(x=10)
print(p2)                       # Point(x=10, y=4)，原对象不变

# 实用案例：处理 CSV 数据
Student = namedtuple("Student", "name age score")
students = [
    Student("张三", 20, 85),
    Student("李四", 22, 92),
    Student("王五", 19, 78),
]
for s in students:
    print(f"{s.name}：{s.score}分")

top = max(students, key=lambda s: s.score)
print(f"最高分：{top.name}")
