# -*- coding: utf-8 -*-
"""
Day 19: Day 19
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：ADB基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：ADB基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    ADB (Android Debug Bridge) 命令:
    1. 设备连接
       adb devices              # 列出连接的设备
       adb connect <ip>:<port>  # 连接网络设备
       adb disconnect           # 断开连接
    2. 应用操作
       adb install <apk>        # 安装应用
       adb uninstall <package>  # 卸载应用
       adb shell pm list packages  # 列出所有应用
    3. 文件操作
       adb push <local> <remote>   # 推送文件
       adb pull <remote> <local>   # 拉取文件
    4. Shell命令
       adb shell <command>      # 执行shell命令
       adb shell am start -n <package>/<activity>  # 启动应用
       adb shell am force-stop <package>           # 停止应用
    5. 日志
       adb logcat               # 查看日志
       adb logcat -d > log.txt  # 导出日志
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：性能数据获取"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：性能数据获取")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ADBHelper:
        """ADB辅助类"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.device_id = device_id
            self.adb_cmd = "adb"
            if device_id:
                self.adb_cmd += f" -s {device_id}"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _run_shell():
            """
            运行ADB shell命令
            参数:
                command: shell命令
            返回:
                命令输出
            """
            full_cmd = f"{self.adb_cmd} shell {command}"
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[ADB] {full_cmd}")
            # 模拟执行 (实际环境取消注释)
            # result = subprocess.run(
            #     full_cmd,
            #     shell=True,
            #     capture_output=True,
            #     text=True
            # )
            # return result.stdout
            # 模拟返回
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._mock_output(command)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _mock_output():
            """模拟ADB输出"""
            if "dumpsys meminfo" in command:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._mock_meminfo()
            elif "dumpsys cpuinfo" in command:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._mock_cpuinfo()
            elif "top -n 1" in command:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._mock_top()
            elif "gfxinfo" in command:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._mock_gfxinfo()
            elif "battery" in command:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return self._mock_battery()
            elif "getprop" in command:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return "12\n"
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _mock_meminfo():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return """
    Applications Memory Usage (in Kilobytes):
    Uptime: 1234567 Realtime: 2345678
    ** MEMINFO in pid 1234 [com.example.app] **
                       Pss  Private  Private  SwapPss     Heap     Heap     Heap
                     Total    Dirty    Clean    Dirty     Size    Alloc     Free
                    ------   ------   ------   ------   ------   ------   ------
      Native Heap    54321    54321        0      100    98304    51200    47104
      Dalvik Heap    32109    32109        0      200    65536    45000    20536
     Dalvik Other     5678     5678        0        0
            Stack      456      456        0        0
           Ashmem      234      234        0        0
          Gfx dev    12345    12345        0        0
        Other dev       12       12        0        0
         .so mmap    23456     1234    20000      500
        .apk mmap     3456        0     3000        0
        .ttf mmap      789        0      700        0
        .dex mmap    12345        0    11000        0
        .oat mmap     5678        0     5000        0
        .art mmap    23456    20000     1000      300
       Other mmap      456       45      300        0
       EGL mtrack    45678    45678        0        0
          Unknown     1234     1234        0        0
            TOTAL   245678   173346    41000     1100   163840    96200    67640
     App Summary
                           Pss(KB)
                            ------
               Java Heap:    52109
             Native Heap:    54321
                    Code:    40934
                   Stack:      456
                Graphics:    58023
           Private Other:     6969
                  System:    32866
                   TOTAL:   245678       TOTAL SWAP PSS:     1100
            """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _mock_cpuinfo():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return """
    Load: 2.5 / 2.3 / 2.1
    CPU usage from 0ms to 1000ms later:
      45% 1234/com.example.app: 35% user + 10% kernel
      12% system_server: 8% user + 4% kernel
      10% android.hardware.graphics.composer: 6% user + 4% kernel
      8% surfaceflinger: 5% user + 3% kernel
      ...
            """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _mock_top():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return """
    User 45%, System 15%, IOW 2%, IRQ 0%
    User 450 + Nice 0 + Sys 150 + Idle 380 + IOW 20 + IRQ 0 + SIRQ 0 = 1000
      PID USER     PR  NI CPU% S  #THR     VSS     RSS PCY Name
     1234 u0_a123  10 -10  35% S    45 2345678  245678 FG com.example.app
      567 system   18   0  12% S    89 3456789  456789 FG system_server
            """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _mock_gfxinfo():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return """
    ** Graphics info for pid 1234 [com.example.app] **
    Stats since: 1234567890123
    Total frames rendered: 1200
    Janky frames: 45 (3.75%)
    50th percentile: 12ms
    90th percentile: 24ms
    95th percentile: 32ms
    99th percentile: 48ms
    Number Missed Vsync: 10
    Number High input latency: 5
    Number Slow UI thread: 20
    Number Slow bitmap uploads: 3
    Number Slow issue draw commands: 7
            """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _mock_battery():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return """
    AC powered: false
    USB powered: true
    Wireless powered: false
    Max charging current: 1500000
    status: 2
    health: 2
    present: true
    level: 85
    scale: 100
    voltage: 4201
    temperature: 320
    technology: Li-ion
            """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：内存监控"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：内存监控")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MemoryMonitor:
        """内存监控器"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.adb = adb_helper
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_memory_info():
            """
            获取应用内存信息
            参数:
                package_name: 应用包名
            返回:
                内存信息字典
            """
            output = self.adb._run_shell(f"dumpsys meminfo {package_name}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._parse_meminfo(output)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _parse_meminfo():
            """解析内存信息"""
            mem_info = {
                "timestamp": datetime.now().isoformat(),
                "total_pss_kb": 0,
                "total_private_dirty_kb": 0,
                "java_heap_kb": 0,
                "native_heap_kb": 0,
                "code_kb": 0,
                "graphics_kb": 0,
                "stack_kb": 0,
            }
            # 解析TOTAL
            total_match = re.search(r'TOTAL:\s+(\d+)', output)
            if total_match:
                mem_info["total_pss_kb"] = int(total_match.group(1))
            # 解析Java Heap
            java_heap_match = re.search(r'Java Heap:\s+(\d+)', output)
            if java_heap_match:
                mem_info["java_heap_kb"] = int(java_heap_match.group(1))
            # 解析Native Heap
            native_heap_match = re.search(r'Native Heap:\s+(\d+)', output)
            if native_heap_match:
                mem_info["native_heap_kb"] = int(native_heap_match.group(1))
            # 解析Code
            code_match = re.search(r'Code:\s+(\d+)', output)
            if code_match:
                mem_info["code_kb"] = int(code_match.group(1))
            # 解析Graphics
            graphics_match = re.search(r'Graphics:\s+(\d+)', output)
            if graphics_match:
                mem_info["graphics_kb"] = int(graphics_match.group(1))
            # 解析Stack
            stack_match = re.search(r'Stack:\s+(\d+)', output)
            if stack_match:
                mem_info["stack_kb"] = int(stack_match.group(1))
            # 转换为MB
            for key in mem_info:
                if key.endswith("_kb"):
                    mb_key = key.replace("_kb", "_mb")
                    mem_info[mb_key] = round(mem_info[key] / 1024, 2)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return mem_info
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def monitor_memory():
            """
            持续监控内存
            参数:
                package_name: 应用包名
                duration: 监控时长(秒)
                interval: 采样间隔(秒)
            """
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"\n开始监控内存: {package_name}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"时长: {duration}秒, 间隔: {interval}秒")
            results = []
            start_time = time.time()
            while time.time() - start_time < duration:
                mem_info = self.get_memory_info(package_name)
                # append() - 列表末尾添加元素
                # 语法: 列表.append(元素)
                # 返回值: None（直接修改原列表）
                results.append(mem_info)
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"  Total PSS: {mem_info.get('total_pss_mb', 0)} MB, "
                      f"Java Heap: {mem_info.get('java_heap_mb', 0)} MB")
                time.sleep(interval)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return results
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_memory_summary():
            """获取内存统计摘要"""
            if not results:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {}
            total_pss_values = [r.get("total_pss_mb", 0) for r in results]
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {
                "samples": len(results),
                "avg_total_pss_mb": round(sum(total_pss_values) / len(total_pss_values), 2),
                "max_total_pss_mb": max(total_pss_values),
                "min_total_pss_mb": min(total_pss_values),
            }


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：CPU监控"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：CPU监控")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class CPUMonitor:
        """CPU监控器"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.adb = adb_helper
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cpu_info():
            """
            获取应用CPU信息
            参数:
                package_name: 应用包名
            返回:
                CPU信息字典
            """
            output = self.adb._run_shell(f"dumpsys cpuinfo | grep {package_name}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._parse_cpuinfo(output, package_name)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _parse_cpuinfo():
            """解析CPU信息"""
            cpu_info = {
                "timestamp": datetime.now().isoformat(),
                "package": package_name,
                "cpu_percent": 0,
                "user_percent": 0,
                "kernel_percent": 0,
            }
            # 解析CPU使用率
            # 格式: 45% 1234/com.example.app: 35% user + 10% kernel
            match = re.search(r'(\d+)%\s+\d+/' + re.escape(package_name) + 
                             r':\s+(\d+)%\s+user\s+\+\s+(\d+)%\s+kernel', output)
            if match:
                cpu_info["cpu_percent"] = int(match.group(1))
                cpu_info["user_percent"] = int(match.group(2))
                cpu_info["kernel_percent"] = int(match.group(3))
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return cpu_info
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cpu_info_from_top():
            """
            使用top命令获取CPU信息
            参数:
                package_name: 应用包名
            返回:
                CPU信息字典
            """
            output = self.adb._run_shell("top -n 1 -s cpu")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._parse_top_output(output, package_name)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _parse_top_output():
            """解析top输出"""
            cpu_info = {
                "timestamp": datetime.now().isoformat(),
                "package": package_name,
                "cpu_percent": 0,
                "vss_kb": 0,
                "rss_kb": 0,
                "pid": 0,
            }
            for line in output.split('\n'):
                if package_name in line:
                    # 解析: PID USER PR NI CPU% S #THR VSS RSS PCY Name
                    parts = line.split()
                    if len(parts) >= 10:
                        cpu_info["pid"] = int(parts[0])
                        cpu_info["cpu_percent"] = float(parts[4].replace('%', ''))
                        cpu_info["vss_kb"] = int(parts[6])
                        cpu_info["rss_kb"] = int(parts[7])
                    break
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return cpu_info
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def monitor_cpu():
            """
            持续监控CPU
            参数:
                package_name: 应用包名
                duration: 监控时长(秒)
                interval: 采样间隔(秒)
            """
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"\n开始监控CPU: {package_name}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"时长: {duration}秒, 间隔: {interval}秒")
            results = []
            start_time = time.time()
            while time.time() - start_time < duration:
                cpu_info = self.get_cpu_info_from_top(package_name)
                # append() - 列表末尾添加元素
                # 语法: 列表.append(元素)
                # 返回值: None（直接修改原列表）
                results.append(cpu_info)
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"  CPU: {cpu_info.get('cpu_percent', 0)}%, "
                      f"PID: {cpu_info.get('pid', 0)}")
                time.sleep(interval)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return results
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cpu_summary():
            """获取CPU统计摘要"""
            if not results:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {}
            cpu_values = [r.get("cpu_percent", 0) for r in results]
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return {
                "samples": len(results),
                "avg_cpu_percent": round(sum(cpu_values) / len(cpu_values), 2),
                "max_cpu_percent": max(cpu_values),
                "min_cpu_percent": min(cpu_values),
            }


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：性能监控示例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：性能监控示例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_performance_monitoring():
        """演示性能监控"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("性能监控演示")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # 创建ADB助手
        adb = ADBHelper()
        # 内存监控
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. 内存监控:")
        mem_monitor = MemoryMonitor(adb)
        mem_info = mem_monitor.get_memory_info("com.example.app")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  总PSS: {mem_info.get('total_pss_mb', 0)} MB")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  Java Heap: {mem_info.get('java_heap_mb', 0)} MB")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  Native Heap: {mem_info.get('native_heap_mb', 0)} MB")
        # CPU监控
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. CPU监控:")
        cpu_monitor = CPUMonitor(adb)
        cpu_info = cpu_monitor.get_cpu_info_from_top("com.example.app")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  CPU使用率: {cpu_info.get('cpu_percent', 0)}%")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  PID: {cpu_info.get('pid', 0)}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """实战任务：实现性能监控"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：实现性能监控")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：实现完整的性能监控工具
    要求:
    1. 封装PerformanceMonitor类
    2. 同时监控内存和CPU
    3. 保存结果到文件
    4. 生成统计报告
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MyPerformanceMonitor:
        """
        性能监控器
        要求:
        1. 同时监控内存和CPU
        2. 支持设置阈值报警
        3. 保存监控数据到JSON文件
        4. 生成统计报告
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def start_monitoring():
            """开始监控"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def save_results():
            """保存结果到文件"""
            # 你的代码
            pass
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def generate_report():
            """生成统计报告"""
            # 你的代码
            pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """参考答案（完成后对照）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("参考答案（完成后对照）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MyPerformanceMonitor:
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.package_name = package_name
            self.adb = ADBHelper(device_id)
            self.mem_monitor = MemoryMonitor(self.adb)
            self.cpu_monitor = CPUMonitor(self.adb)
            self.results = []
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def start_monitoring():
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"开始监控: {self.package_name}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"时长: {duration}秒, 间隔: {interval}秒")
            start_time = time.time()
            while time.time() - start_time < duration:
                mem_info = self.mem_monitor.get_memory_info(self.package_name)
                cpu_info = self.cpu_monitor.get_cpu_info_from_top(self.package_name)
                record = {
                    "timestamp": datetime.now().isoformat(),
                    "memory": mem_info,
                    "cpu": cpu_info
                }
                self.results.append(record)
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"  Mem: {mem_info.get('total_pss_mb', 0)} MB, "
                      f"CPU: {cpu_info.get('cpu_percent', 0)}%")
                time.sleep(interval)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.results
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def save_results():
            # 【with 语句】
            # 作用: 自动管理资源，确保文件等正确关闭
            # 原理: 使用上下文管理器 __enter__ 和 __exit__
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"结果已保存: {filename}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def generate_report():
            if not self.results:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return {}
            mem_values = [r['memory'].get('total_pss_mb', 0) for r in self.results]
            cpu_values = [r['cpu'].get('cpu_percent', 0) for r in self.results]
            report = {
                "package": self.package_name,
                "samples": len(self.results),
                "memory": {
                    "avg_mb": round(sum(mem_values) / len(mem_values), 2),
                    "max_mb": max(mem_values),
                    "min_mb": min(mem_values),
                },
                "cpu": {
                    "avg_percent": round(sum(cpu_values) / len(cpu_values), 2),
                    "max_percent": max(cpu_values),
                    "min_percent": min(cpu_values),
                }
            }
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return report
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
    """今日学习要点总结"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("今日学习要点总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    1. ADB基础:
       - adb devices: 查看设备
       - adb shell: 执行shell命令
       - adb install/uninstall: 应用管理
    2. 内存监控:
       - dumpsys meminfo: 获取内存信息
       - 解析PSS、Private Dirty等指标
       - 监控Java Heap、Native Heap
    3. CPU监控:
       - dumpsys cpuinfo: CPU使用率
       - top命令: 实时CPU监控
       - 解析user和kernel时间
    4. 性能监控:
       - 持续采样
       - 数据统计
       - 报告生成
    验证标准：能输出应用的内存和CPU数据
    """
    # 运行演示
    if __name__ == "__main__":
        demo_performance_monitoring()

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section9():
    """第九部分：subprocess模块调用ADB（补充）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第九部分：subprocess模块调用ADB（补充）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import subprocess

    # ---- 1. subprocess基础 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. subprocess基础:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    subprocess模块用于在Python中执行系统命令
    在自动化测试中，常用来调用ADB命令控制Android设备

    核心方法:
    - subprocess.run()       : 执行命令并等待完成 (推荐)
    - subprocess.Popen()     : 更灵活的进程管理
    - subprocess.getoutput() : 快速获取命令输出
    """)

    # ---- 2. subprocess.run() 详解 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. subprocess.run() 详解:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import subprocess

    # 基本用法
    result = subprocess.run(
        ['adb', 'devices'],       # 命令列表
        capture_output=True,       # 捕获输出
        text=True,                 # 以字符串返回 (而非bytes)
        timeout=30                 # 超时时间(秒)
    )

    # 获取结果
    result.returncode  # 返回码 (0=成功)
    result.stdout      # 标准输出
    result.stderr      # 错误输出

    # 也可以用shell=True执行命令字符串 (不推荐，有安全风险)
    result = subprocess.run(
        'adb devices',
        shell=True,
        capture_output=True,
        text=True
    )
    """)

    # 演示: 执行一个简单命令
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("演示 - 执行系统命令:")
    # 【try-except 异常处理】
    # 语法: try: 可能出错的代码 except 异常类型: 处理代码
    # 作用: 捕获并处理异常，防止程序崩溃
    try:
        result = subprocess.run(
            ['python', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  返回码: {result.returncode}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"  输出: {result.stdout.strip()}")
    except FileNotFoundError:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  命令未找到")
    except subprocess.TimeoutExpired:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  命令超时")

    # ---- 3. 封装ADB工具类 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n3. 封装ADB工具类:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import subprocess

    class ADBHelper:
        '''ADB命令封装工具类'''

        def __init__(self, device_id=None):
            self.device_id = device_id
            self.base_cmd = ['adb']
            if device_id:
                self.base_cmd += ['-s', device_id]

        def run_cmd(self, args):
            '''执行ADB命令并返回输出'''
            cmd = self.base_cmd + args
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                if result.returncode != 0:
                    print(f'ADB错误: {result.stderr}')
                return result.stdout.strip()
            except subprocess.TimeoutExpired:
                print(f'ADB命令超时: {" ".join(cmd)}')
                return ''

        def get_devices(self):
            '''获取已连接设备列表'''
            output = self.run_cmd(['devices'])
            devices = []
            for line in output.split('\\n')[1:]:
                if '\\t' in line:
                    devices.append(line.split('\\t')[0])
            return devices

        def install_app(self, apk_path):
            '''安装APK'''
            return self.run_cmd(['install', '-r', apk_path])

        def uninstall_app(self, package):
            '''卸载应用'''
            return self.run_cmd(['uninstall', package])

        def start_app(self, package, activity):
            '''启动应用'''
            component = f'{package}/{activity}'
            return self.run_cmd(['shell', 'am', 'start', '-n', component])

        def stop_app(self, package):
            '''停止应用'''
            return self.run_cmd(['shell', 'am', 'force-stop', package])

        def get_current_activity(self):
            '''获取当前Activity'''
            output = self.run_cmd([
                'shell', 'dumpsys', 'activity', 'activities'
            ])
            for line in output.split('\\n'):
                if 'mResumedActivity' in line:
                    return line.strip()
            return ''

        def screenshot(self, save_path):
            '''截图'''
            self.run_cmd(['shell', 'screencap', '-p', '/sdcard/screen.png'])
            self.run_cmd(['pull', '/sdcard/screen.png', save_path])
            return save_path

        def get_log(self, tag=None, level='I'):
            '''获取logcat日志'''
            cmd = ['logcat', '-d']
            if tag:
                cmd += ['-s', f'{tag}:{level}']
            return self.run_cmd(cmd)

        def push_file(self, local, remote):
            '''推送文件到设备'''
            return self.run_cmd(['push', local, remote])

        def pull_file(self, remote, local):
            '''从设备拉取文件'''
            return self.run_cmd(['pull', remote, local])

    # 使用示例:
    # adb = ADBHelper('emulator-5554')
    # devices = adb.get_devices()
    # adb.install_app('./app-debug.apk')
    # adb.start_app('com.example.app', '.MainActivity')
    # adb.screenshot('./screenshots/home.png')
    """)

    # ---- 4. subprocess.Popen 长时间运行 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. Popen处理长时间运行的命令:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import subprocess
    import time

    # 实时读取logcat输出 (持续运行的命令)
    def monitor_logcat(package, duration=10):
        '''实时监控logcat日志'''
        process = subprocess.Popen(
            ['adb', 'logcat', '-s', f'{package}:I'],
            stdout=subprocess.PIPE,
            text=True
        )

        start = time.time()
        try:
            while time.time() - start < duration:
                line = process.stdout.readline()
                if line:
                    print(f'[LOG] {line.strip()}')
        finally:
            process.terminate()  # 终止进程
            process.wait()       # 等待进程结束

    # 性能数据采集 (后台运行)
    def collect_fps(package, output_file):
        '''后台采集FPS数据'''
        process = subprocess.Popen(
            ['adb', 'shell', 'dumpsys', 'gfxinfo', package],
            stdout=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate(timeout=10)
        with open(output_file, 'w') as f:
            f.write(stdout)
        return output_file
    """)

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def practice_task():
    """实战任务"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请修改代码完成任务...")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def show_answer():
    """显示参考答案"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("参考答案")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请参考原文件中的答案部分")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def show_summary():
    """显示学习总结"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("学习总结")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("请参考原文件中的总结部分")

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def main():
    """主菜单"""
    while True:
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("Day {day_num}: 学习菜单")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("1. 第一部分：ADB基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：性能数据获取")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：内存监控")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：CPU监控")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：性能监控示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 实战任务：实现性能监控")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 今日学习要点总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 补充：subprocess调用ADB")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("10. 实战任务")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 参考答案")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 学习总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("0. 退出")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        
        choice = input("\n请选择 (0-9): ").strip()
        
        if choice == "1":
            section1()
        if choice == "2":
            section2()
        if choice == "3":
            section3()
        if choice == "4":
            section4()
        if choice == "5":
            section5()
        if choice == "6":
            section6()
        if choice == "7":
            section7()
        if choice == "8":
            section8()
        if choice == "9":
            section9()
        elif choice == "10":
            practice_task()
        elif choice == "8":
            show_answer()
        elif choice == "7":
            show_summary()
        elif choice == "0":
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n感谢学习！再见！")
            break
        else:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("\n无效选择，请重新输入")
        
        # input() - 获取用户输入
        # 语法: input(提示信息)
        # 返回值: 用户输入的字符串
        input("\n按回车键继续...")


if __name__ == "__main__":
    main()
