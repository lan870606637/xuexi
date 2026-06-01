# ============================================
# 题目35：综合项目——命令行待办清单
# 知识点：综合运用所有基础知识 + JSON持久化
# ============================================

import json
import os
from datetime import datetime, date

# --- 数据模型 ---
class Task:
    _id_counter = 0

    def __init__(self, title, priority="中", due_date=None, tags=None):
        Task._id_counter += 1
        self.id = Task._id_counter
        self.title = title
        self.priority = priority            # 高 / 中 / 低
        self.done = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.due_date = due_date            # 字符串 "YYYY-MM-DD" 或 None
        self.tags = tags or []

    def complete(self):
        self.done = True

    def is_overdue(self):
        if not self.due_date or self.done:
            return False
        return date.today() > date.fromisoformat(self.due_date)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "done": self.done,
            "created_at": self.created_at,
            "due_date": self.due_date,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls.__new__(cls)
        task.id = data["id"]
        task.title = data["title"]
        task.priority = data["priority"]
        task.done = data["done"]
        task.created_at = data["created_at"]
        task.due_date = data["due_date"]
        task.tags = data["tags"]
        return task

    def __str__(self):
        status = "✓" if self.done else "○"
        priority_icons = {"高": "🔴", "中": "🟡", "低": "🟢"}
        icon = priority_icons.get(self.priority, "○")
        overdue = " [逾期！]" if self.is_overdue() else ""
        due = f" (截止: {self.due_date})" if self.due_date else ""
        tags = f" #{' #'.join(self.tags)}" if self.tags else ""
        return f"[{status}] #{self.id:03d} {icon} {self.title}{due}{overdue}{tags}"


# --- 任务管理器 ---
class TaskManager:
    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
        self.tasks = []
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
                    Task._id_counter = data.get("id_counter", 0)
            except (json.JSONDecodeError, KeyError):
                self.tasks = []

    def _save(self):
        data = {
            "tasks": [t.to_dict() for t in self.tasks],
            "id_counter": Task._id_counter,
        }
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self, title, priority="中", due_date=None, tags=None):
        task = Task(title, priority, due_date, tags)
        self.tasks.append(task)
        self._save()
        print(f"✅ 已添加：{task}")
        return task

    def complete(self, task_id):
        task = self._find(task_id)
        if task:
            task.complete()
            self._save()
            print(f"✅ 已完成：{task.title}")
        else:
            print(f"❌ 未找到任务 #{task_id:03d}")

    def delete(self, task_id):
        task = self._find(task_id)
        if task:
            self.tasks.remove(task)
            self._save()
            print(f"🗑️ 已删除：{task.title}")
        else:
            print(f"❌ 未找到任务 #{task_id:03d}")

    def _find(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)

    def list_tasks(self, show_done=False, priority=None, tag=None, sort_by="id"):
        filtered = self.tasks

        if not show_done:
            filtered = [t for t in filtered if not t.done]
        if priority:
            filtered = [t for t in filtered if t.priority == priority]
        if tag:
            filtered = [t for t in filtered if tag in t.tags]

        sort_keys = {
            "id": lambda t: t.id,
            "priority": lambda t: {"高": 0, "中": 1, "低": 2}.get(t.priority, 3),
            "due": lambda t: t.due_date or "9999-99-99",
        }
        key = sort_keys.get(sort_by, sort_keys["id"])
        filtered = sorted(filtered, key=key)

        return filtered

    def print_list(self, show_done=False, priority=None, tag=None, sort_by="id"):
        tasks = self.list_tasks(show_done, priority, tag, sort_by)
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.done)
        overdue = sum(1 for t in self.tasks if t.is_overdue())

        print(f"\n{'='*50}")
        print(f"  待办清单  总计:{total}  已完成:{done}  逾期:{overdue}")
        print(f"{'='*50}")

        if not tasks:
            print("  (暂无任务)")
        else:
            for task in tasks:
                print(f"  {task}")
        print(f"{'='*50}\n")

    def stats(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.done)
        overdue = sum(1 for t in self.tasks if t.is_overdue())
        pending = total - done

        from collections import Counter
        priority_count = Counter(t.priority for t in self.tasks if not t.done)
        tag_count = Counter(tag for t in self.tasks for tag in t.tags)

        print(f"\n📊 统计信息：")
        print(f"  总任务：{total}")
        print(f"  已完成：{done} ({done/total*100:.0f}%)" if total else "  无任务")
        print(f"  待完成：{pending}")
        print(f"  已逾期：{overdue}")
        print(f"\n  待完成优先级分布：")
        for p, count in sorted(priority_count.items(),
                                key=lambda x: {"高":0,"中":1,"低":2}.get(x[0], 3)):
            bar = "█" * count
            print(f"    {p}：{bar} ({count})")
        if tag_count:
            print(f"\n  热门标签：{tag_count.most_common(5)}")


# --- 主程序 ---
if __name__ == "__main__":
    manager = TaskManager("tasks.json")

    # 添加任务
    manager.add("学习 Python 装饰器", priority="高", tags=["学习", "Python"])
    manager.add("阅读《流畅的 Python》第3章", priority="中", tags=["学习"])
    manager.add("写周报", priority="高", due_date="2024-06-20", tags=["工作"])
    manager.add("回复邮件", priority="中", due_date="2024-06-15", tags=["工作"])
    manager.add("整理桌面", priority="低", tags=["生活"])
    manager.add("买菜", priority="中", tags=["生活"])

    # 完成一些任务
    manager.complete(3)
    manager.complete(5)

    # 列出所有待完成任务
    manager.print_list()

    # 只显示高优先级
    print("📌 高优先级任务：")
    high = manager.list_tasks(priority="高")
    for t in high:
        print(f"  {t}")

    # 按标签筛选
    print("\n🏷️ 工作相关：")
    work = manager.list_tasks(tag="工作", show_done=True)
    for t in work:
        print(f"  {t}")

    # 统计
    manager.stats()

    # 显示所有（包括已完成）
    manager.print_list(show_done=True, sort_by="priority")

    # 清理
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
        print("已删除测试文件 tasks.json")
