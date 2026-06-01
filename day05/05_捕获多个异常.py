# -*- coding: utf-8 -*-
"""
05 - 捕获多个异常

3 种写法：
    A. 多个 except     —— 每种异常单独处理
    B. 合并捕获 (X, Y) —— 多种异常同样处理
    C. Exception 兜底  —— 抓所有（慎用）
"""

# ============================================================
# 准备：一个会抛各种异常的函数
# ============================================================
def parse_age(s):
    """把字符串转成 0-150 之间的整数；不合法就抛异常"""
    n = int(s)                      # 可能抛 ValueError
    if n < 0 or n > 150:
        raise ValueError("年龄超出范围")
    return n


# ============================================================
# 写法 A：多个 except —— 不同异常做不同处理
# ============================================================
def read_config_v1(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"  [A] 文件不存在: {path}")
        return ""
    except PermissionError:
        print(f"  [A] 没权限读: {path}")
        return ""
    except UnicodeDecodeError as e:
        print(f"  [A] 编码错误: {e}")
        return ""


print("--- 写法 A：多个 except ---")
read_config_v1("/tmp/不存在.txt")


# ============================================================
# 写法 B：合并捕获 —— 几种异常做同样处理
# ============================================================
def read_config_v2(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, PermissionError) as e:
        # 注意：要用 元组 (X, Y) 包起来
        print(f"  [B] 读取失败 [{type(e).__name__}]: {e}")
        return ""


print("\n--- 写法 B：合并捕获 ---")
read_config_v2("/tmp/不存在.txt")


# ============================================================
# 写法 C：Exception 兜底 —— 抓所有"业务异常"
# ============================================================
# 适合"无论什么错都要记日志 / 通知 / 重抛"的场景
def read_config_v3(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        # type(e).__name__ 把异常类型名打出来，方便排查
        print(f"  [C] 出错了 [{type(e).__name__}]: {e}")
        return ""


print("\n--- 写法 C：Exception 兜底 ---")
read_config_v3("/tmp/不存在.txt")


# ============================================================
# ⚠️ 兜底的危险：会把所有错误吞掉，bug 藏起来
# ============================================================
def evil_function():
    """这段写法是反面教材，不要学"""
    try:
        x = undefined_variable + 1     # 笔误：变量根本没定义
    except Exception:
        pass                            # 啥也不做
    # 写完上线后，永远不会报错，但功能完全失效


print("\n--- 反面教材：吞异常 ---")
evil_function()
print("看，毫无声响地'成功'了。这就是 except Exception: pass 的危害")


# ============================================================
# 多个 except 的"匹配顺序"—— 从上往下找
# ============================================================
# 重要：异常有继承关系。父类 except 会"挡住"子类 except。
#       要把"具体的"放上面，"通用的"放下面。

def try_match():
    try:
        raise FileNotFoundError("文件不存在")     # 它是 OSError 的子类
    except OSError:                              # ← 父类放上面，会先匹配
        print("  匹配到 OSError")
    except FileNotFoundError:                    # ← 这一行永远跑不到！
        print("  匹配到 FileNotFoundError")


print("\n--- 顺序错了的反例 ---")
try_match()


def try_match_correct():
    try:
        raise FileNotFoundError("文件不存在")
    except FileNotFoundError:                    # ← 具体的放上面
        print("  匹配到 FileNotFoundError ✓")
    except OSError:
        print("  匹配到 OSError")


print("--- 正确顺序 ---")
try_match_correct()


# ============================================================
# 一句话总结：
#   - 不同异常不同处理 → 多个 except
#   - 几个异常同样处理 → 合并 (X, Y)
#   - 想抓所有        → except Exception as e，但**一定要打 log 或重抛**
#   - 永远把"具体类型"放在"父类"之前
# ============================================================
