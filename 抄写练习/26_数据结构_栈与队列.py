# ============================================
# 题目26：常用数据结构——栈与队列
# 知识点：用 list 实现栈 / deque 实现队列 / 应用场景
# ============================================

from collections import deque

# ====== 栈（Stack）======
# LIFO - Last In, First Out（后进先出）
# 操作：push（入栈）、pop（出栈）、peek（查看栈顶）

print("====== 栈 ======")

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("栈为空")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Stack({self._data})"


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)                        # Stack([1, 2, 3])
print(f"栈顶：{s.peek()}")      # 3
print(f"弹出：{s.pop()}")       # 3
print(f"弹出：{s.pop()}")       # 2
print(s)                        # Stack([1])

# --- 应用1：括号匹配 ---
print("\n=== 括号匹配 ===")
def is_balanced(text):
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

tests = ["(())", "()[]{}", "(]", "([)]", "{[]}"]
for t in tests:
    print(f"  '{t}': {'✓ 平衡' if is_balanced(t) else '✗ 不平衡'}")

# --- 应用2：进制转换 ---
print("\n=== 进制转换 ===")
def to_base(num, base):
    digits = "0123456789ABCDEF"
    stack = Stack()
    while num > 0:
        stack.push(num % base)
        num //= base
    result = ""
    while not stack.is_empty():
        result += digits[stack.pop()]
    return result or "0"

print(f"十进制 255 -> 二进制 {to_base(255, 2)}")
print(f"十进制 255 -> 八进制 {to_base(255, 8)}")
print(f"十进制 255 -> 十六进制 {to_base(255, 16)}")

# --- 应用3：计算后缀表达式（逆波兰）---
print("\n=== 后缀表达式 ===")
def eval_rpn(tokens):
    stack = Stack()
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.push(ops[token](a, b))
        else:
            stack.push(float(token))
    return stack.pop()

# "3 4 + 2 *" = (3 + 4) * 2 = 14
print(eval_rpn(["3", "4", "+", "2", "*"]))  # 14.0
# "5 1 2 + 4 * + 3 -" = 5 + (1+2)*4 - 3 = 14
print(eval_rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"]))  # 14.0


# ====== 队列（Queue）======
# FIFO - First In, First Out（先进先出）
# 操作：enqueue（入队）、dequeue（出队）

print("\n====== 队列 ======")

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)     # 右端入队

    def dequeue(self):
        if self.is_empty():
            raise IndexError("队列为空")
        return self._data.popleft() # 左端出队

    def front(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Queue({list(self._data)})"


q = Queue()
q.enqueue("任务A")
q.enqueue("任务B")
q.enqueue("任务C")
print(q)                            # Queue(['任务A', '任务B', '任务C'])
print(f"处理：{q.dequeue()}")       # 任务A（先进先出）
print(f"处理：{q.dequeue()}")       # 任务B
print(q)                            # Queue(['任务C'])

# --- 应用：BFS（广度优先搜索）---
print("\n=== BFS 最短路径 ===")
# 迷宫：0=可通行，1=墙壁
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
end = (4, 4)

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])   # (当前位置, 路径)
    visited = {start}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右左下上

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and maze[nr][nc] == 0
                    and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

path = bfs_shortest_path(maze, start, end)
print(f"从 {start} 到 {end} 的路径：")
for step in path:
    print(f"  {step}")
print(f"路径长度：{len(path) - 1} 步")
