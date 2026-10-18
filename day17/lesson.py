# -*- coding: utf-8 -*-
"""
Day 17: Day 17
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：HTTP基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：HTTP基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    HTTP请求方法:
    - GET: 获取资源
    - POST: 创建资源
    - PUT: 更新资源 (完整更新)
    - PATCH: 部分更新
    - DELETE: 删除资源
    HTTP状态码:
    - 2xx: 成功 (200 OK, 201 Created, 204 No Content)
    - 3xx: 重定向 (301 Moved, 302 Found)
    - 4xx: 客户端错误 (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
    - 5xx: 服务器错误 (500 Internal Error, 502 Bad Gateway, 503 Service Unavailable)
    常见Content-Type:
    - application/json: JSON数据
    - application/x-www-form-urlencoded: 表单数据
    - multipart/form-data: 文件上传
    - text/html: HTML文档
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：Requests基础"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：Requests基础")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    安装: pip install requests
    基本用法:
    # import - 导入模块
    # 作用: 引入其他模块的功能使用
    import requests
    # GET请求
    response = requests.get("https://api.example.com/users")
    # POST请求
    response = requests.post(
        "https://api.example.com/users",
        json={"name": "John", "age": 30}
    )
    """
    # 模拟requests (无网络环境)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockResponse:
        """模拟HTTP响应"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.status_code = status_code
            self._json = json_data or {}
            self.text = text
            self.headers = headers or {}
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def json():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._json
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def raise_for_status():
            if self.status_code >= 400:
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise Exception(f"HTTP Error: {self.status_code}")
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockRequests:
        """模拟requests库"""
        _users = {
            1: {"id": 1, "username": "admin", "email": "admin@example.com"},
            2: {"id": 2, "username": "user", "email": "user@example.com"},
        }
        _tokens = {}
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get():
            """GET请求"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[GET] {url}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  Params: {params}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  Headers: {headers}")
            # 模拟/users接口
            if "/users" in url and "/users/" not in url:
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return MockResponse(200, {"users": list(cls._users.values())})
            # 模拟/users/{id}接口
            if "/users/" in url:
                user_id = int(url.split("/")[-1])
                user = cls._users.get(user_id)
                if user:
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return MockResponse(200, user)
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return MockResponse(404, {"error": "User not found"})
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockResponse(404)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def post():
            """POST请求"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[POST] {url}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  Data: {data}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  JSON: {json}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"  Headers: {headers}")
            # 模拟登录接口
            if "/login" in url:
                username = (json or data or {}).get("username")
                password = (json or data or {}).get("password")
                if username == "admin" and password == "123456":
                    token = "fake_token_12345"
                    cls._tokens[token] = username
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return MockResponse(200, {
                        "success": True,
                        "token": token,
                        "user": {"username": username}
                    })
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return MockResponse(401, {
                    "success": False,
                    "error": "Invalid credentials"
                })
            # 模拟创建用户
            if "/users" in url:
                new_id = max(cls._users.keys()) + 1
                new_user = {"id": new_id, **(json or {})}
                cls._users[new_id] = new_user
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return MockResponse(201, new_user)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockResponse(404)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def put():
            """PUT请求"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[PUT] {url}")
            # 模拟更新用户
            if "/users/" in url:
                user_id = int(url.split("/")[-1])
                if user_id in cls._users:
                    cls._users[user_id].update(json or {})
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return MockResponse(200, cls._users[user_id])
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return MockResponse(404)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockResponse(404)
        # 【装饰器 @classmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @classmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def delete():
            """DELETE请求"""
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"[DELETE] {url}")
            # 模拟删除用户
            if "/users/" in url:
                user_id = int(url.split("/")[-1])
                if user_id in cls._users:
                    del cls._users[user_id]
                    # return - 返回值
                    # 作用: 将结果返回给调用者，结束函数执行
                    return MockResponse(204)
                # return - 返回值
                # 作用: 将结果返回给调用者，结束函数执行
                return MockResponse(404)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockResponse(404)
    # 使用模拟requests
    requests = MockRequests


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：接口请求示例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：接口请求示例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_requests():
        """演示requests用法"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("Requests用法演示")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # 1. GET请求
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. GET请求:")
        response = requests.get("https://api.example.com/users")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Status: {response.status_code}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Data: {response.json()}")
        # 2. GET带参数
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. GET带参数:")
        response = requests.get(
            "https://api.example.com/users",
            params={"page": 1, "limit": 10}
        )
        # 3. POST请求 (JSON)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n3. POST请求 (JSON):")
        response = requests.post(
            "https://api.example.com/users",
            json={"username": "newuser", "email": "new@example.com"}
        )
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Status: {response.status_code}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Data: {response.json()}")
        # 4. POST请求 (表单)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n4. POST请求 (表单):")
        response = requests.post(
            "https://api.example.com/login",
            data={"username": "admin", "password": "123456"}
        )
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Status: {response.status_code}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Data: {response.json()}")
        # 5. 带Header的请求
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n5. 带Header的请求:")
        response = requests.get(
            "https://api.example.com/users/1",
            headers={
                "Authorization": "Bearer fake_token",
                "Accept": "application/json"
            }
        )
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Data: {response.json()}")
        # 6. PUT请求
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n6. PUT请求:")
        response = requests.put(
            "https://api.example.com/users/1",
            json={"email": "updated@example.com"}
        )
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Data: {response.json()}")
        # 7. DELETE请求
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n7. DELETE请求:")
        response = requests.delete("https://api.example.com/users/2")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"Status: {response.status_code}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section4():
    """第四部分：响应处理"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：响应处理")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_response_handling():
        """演示响应处理"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("响应处理演示")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        response = requests.get("https://api.example.com/users")
        # 状态码检查
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"\n状态码: {response.status_code}")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"是否成功: {response.status_code == 200}")
        # JSON解析
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            data = response.json()
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"JSON数据: {data}")
        except:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("响应不是JSON格式")
        # 原始文本
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"原始文本: {response.text}")
        # 响应头
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print(f"响应头: {response.headers}")
        # 错误处理
        # 【异常处理 try-except】
        # 语法: try: ... except 异常类型: ...
        # 作用: 捕获并处理可能发生的错误，防止程序崩溃
        try:
            response.raise_for_status()
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print("请求成功")
        except Exception as e:
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"请求失败: {e}")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：接口测试封装"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：接口测试封装")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class APIClient:
        """
        API客户端
        封装常用的HTTP请求
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.base_url = base_url.rstrip("/")
            self.session = MockRequests  # 实际: requests.Session()
            self.headers = headers or {}
            self.last_response = None
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _make_url():
            """构建完整URL"""
            endpoint = endpoint.lstrip("/")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return f"{self.base_url}/{endpoint}"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get():
            """GET请求"""
            url = self._make_url(endpoint)
            merged_headers = {**self.headers, **(headers or {})}
            self.last_response = self.session.get(url, params=params, headers=merged_headers)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.last_response
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def post():
            """POST请求"""
            url = self._make_url(endpoint)
            merged_headers = {**self.headers, **(headers or {})}
            self.last_response = self.session.post(url, data=data, json=json, headers=merged_headers)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.last_response
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def put():
            """PUT请求"""
            url = self._make_url(endpoint)
            merged_headers = {**self.headers, **(headers or {})}
            self.last_response = self.session.put(url, data=data, json=json, headers=merged_headers)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.last_response
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def delete():
            """DELETE请求"""
            url = self._make_url(endpoint)
            merged_headers = {**self.headers, **(headers or {})}
            self.last_response = self.session.delete(url, headers=merged_headers)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.last_response
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def set_token():
            """设置认证Token"""
            self.headers["Authorization"] = f"Bearer {token}"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_status():
            """断言状态码"""
            actual = self.last_response.status_code
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert actual == expected_status, f"期望状态码: {expected_status}, 实际: {actual}"
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_json_path():
            """
            断言JSON路径
            path: 点号分隔的路径 (如 "data.user.name")
            """
            data = self.last_response.json()
            keys = path.split(".")
            for key in keys:
                if isinstance(data, dict):
                    data = data.get(key)
                else:
                    # raise - 主动抛出异常
                    # 作用: 当遇到错误条件时，主动抛出异常
                    raise AssertionError(f"无法访问路径: {path}")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert data == expected_value, f"路径 {path}: 期望 {expected_value}, 实际 {data}"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：接口测试用例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：接口测试用例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestAPI:
        """接口测试类"""
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def client():
            """API客户端"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return APIClient("https://api.example.com")
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def auth_client():
            """已认证的客户端"""
            # 登录获取token
            response = client.post("/login", json={
                "username": "admin",
                "password": "123456"
            })
            token = response.json().get("token")
            client.set_token(token)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return client
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_users():
            """测试获取用户列表"""
            response = client.get("/users")
            client.assert_status(200)
            data = response.json()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "users" in data
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_user_by_id():
            """测试获取单个用户"""
            response = client.get("/users/1")
            client.assert_status(200)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.json()["id"] == 1
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_success():
            """测试登录成功"""
            response = client.post("/login", json={
                "username": "admin",
                "password": "123456"
            })
            client.assert_status(200)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.json()["success"] is True
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "token" in response.json()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_failure():
            """测试登录失败"""
            response = client.post("/login", json={
                "username": "admin",
                "password": "wrong"
            })
            client.assert_status(401)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.json()["success"] is False
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_create_user():
            """测试创建用户"""
            response = auth_client.post("/users", json={
                "username": "testuser",
                "email": "test@example.com"
            })
            auth_client.assert_status(201)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.json()["username"] == "testuser"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """实战任务：编写接口测试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：编写接口测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为以下接口编写测试用例
    接口列表:
    1. GET /api/products - 获取商品列表
    2. GET /api/products/{id} - 获取商品详情
    3. POST /api/cart - 添加商品到购物车
    4. GET /api/cart - 获取购物车
    5. POST /api/orders - 创建订单
    6. GET /api/orders/{id} - 获取订单详情
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ProductAPIClient(APIClient):
        """商品API客户端"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_products():
            """获取商品列表"""
            params = {"category": category} if category else None
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get("/api/products", params=params)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_product():
            """获取商品详情"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get(f"/api/products/{product_id}")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def add_to_cart():
            """添加到购物车"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.post("/api/cart", json={
                "product_id": product_id,
                "quantity": quantity
            })
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_cart():
            """获取购物车"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get("/api/cart")
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def create_order():
            """创建订单"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.post("/api/orders", json={
                "address": address,
                "items": items
            })
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_order():
            """获取订单详情"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get(f"/api/orders/{order_id}")
    # 请完成下面的测试用例
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestProductAPI:
        """商品接口测试"""
        # 你的代码写在这里
        pass


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section8():
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
    class TestProductAPI:
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def client():
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return ProductAPIClient("https://api.example.com")
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def auth_client():
            client.post("/login", json={"username": "admin", "password": "123456"})
            client.set_token("fake_token")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return client
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_products():
            response = client.get_products()
            client.assert_status(200)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "products" in response.json()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_product_detail():
            response = client.get_product(1)
            client.assert_status(200)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.json()["id"] == 1
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_add_to_cart():
            response = auth_client.add_to_cart(1, 2)
            client.assert_status(200)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.json()["success"] is True
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_cart():
            auth_client.add_to_cart(1, 1)
            response = auth_client.get_cart()
            client.assert_status(200)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "items" in response.json()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_create_order():
            response = auth_client.create_order(
                address="北京市",
                items=[{"product_id": 1, "quantity": 2}]
            )
            client.assert_status(201)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "order_id" in response.json()
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section9():
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
    1. HTTP基础:
       - 请求方法: GET, POST, PUT, DELETE
       - 状态码: 2xx成功, 4xx客户端错误, 5xx服务器错误
       - Content-Type
    2. Requests库:
       - requests.get(), requests.post()
       - params, json, data, headers参数
       - response.status_code, response.json()
    3. 响应处理:
       - 状态码检查
       - JSON解析
       - 错误处理
    4. 接口封装:
       - APIClient类
       - 统一处理base_url和headers
       - 断言方法封装
    5. 测试用例:
       - 认证处理
       - 参数化测试
       - 链式调用
    验证标准：能完成3-5个接口的自动化测试
    """
    # 运行演示
    if __name__ == "__main__":
        demo_requests()
        demo_response_handling()

# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section10():
    """第十部分：Requests实战练习（补充）"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第十部分：Requests实战练习（补充）")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)

    # ---- 1. requests常用方法速查 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n1. requests常用方法速查:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import requests

    # GET请求
    resp = requests.get(url, params={'key': 'value'}, headers={})

    # POST请求 - JSON数据
    resp = requests.post(url, json={'name': 'test'}, headers={})

    # POST请求 - 表单数据
    resp = requests.post(url, data={'name': 'test'})

    # POST请求 - 文件上传
    resp = requests.post(url, files={'file': open('test.png', 'rb')})

    # PUT请求
    resp = requests.put(url, json={'name': 'updated'})

    # DELETE请求
    resp = requests.delete(url)

    # 通用参数:
    # params  - URL查询参数 (GET用)
    # json    - JSON请求体 (自动设置Content-Type)
    # data    - 表单请求体
    # headers - 请求头
    # timeout - 超时时间(秒)
    # cookies - Cookie
    """)

    # ---- 2. 响应对象详解 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("2. 响应对象(Response)详解:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    resp = requests.get('https://api.example.com/users/1')

    # 状态码
    resp.status_code        # 200, 404, 500 等
    resp.ok                 # True if 200 <= status_code < 400
    resp.raise_for_status() # 非2xx时抛出HTTPError异常

    # 响应体
    resp.text               # 字符串格式
    resp.json()             # 自动解析JSON为dict/list
    resp.content            # 二进制格式 (下载文件用)

    # 响应头
    resp.headers            # 响应头字典
    resp.headers['Content-Type']

    # 其他
    resp.url                # 最终请求的URL
    resp.elapsed            # 响应时间 (timedelta对象)
    resp.elapsed.total_seconds()  # 响应时间(秒)
    resp.cookies            # 响应Cookie
    resp.encoding           # 编码
    """)

    # ---- 3. 接口断言模式 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("3. 接口测试断言模式:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    import requests

    def test_get_user():
        resp = requests.get('https://api.example.com/users/1')

        # 断言状态码
        assert resp.status_code == 200

        # 断言响应时间 (接口性能)
        assert resp.elapsed.total_seconds() < 3, '接口响应超过3秒'

        # 断言响应体
        data = resp.json()
        assert data['code'] == 0, f"业务码错误: {data['code']}"
        assert data['data']['name'] == '张三'
        assert 'id' in data['data'], '响应缺少id字段'
        assert isinstance(data['data']['age'], int), 'age应为整数'

    def test_create_user():
        payload = {'name': '新用户', 'age': 25}
        resp = requests.post(
            'https://api.example.com/users',
            json=payload
        )

        assert resp.status_code == 201  # Created
        data = resp.json()
        assert data['data']['id'] > 0, '应返回新建用户ID'
        assert data['data']['name'] == payload['name']
    """)

    # ---- 4. Session会话保持 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("4. Session会话保持:")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("""
    # Session可以自动保持Cookie，适合需要登录的接口测试

    session = requests.Session()

    # 登录 - Session自动保存Cookie
    session.post('https://api.example.com/login', json={
        'username': 'admin', 'password': '123456'
    })

    # 后续请求自动携带Cookie
    resp = session.get('https://api.example.com/user/profile')
    print(resp.json())

    # 也可以设置公共请求头
    session.headers.update({
        'Authorization': 'Bearer token123',
        'Content-Type': 'application/json'
    })
    """)

    # ---- 5. 模拟实战演练 ----
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("5. 模拟接口测试实战:")
    # 模拟API响应
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self._json = json_data
            self.ok = 200 <= status_code < 400
        def json(self):
            return self._json

    # 模拟GET请求
    resp = MockResponse(200, {
        'code': 0,
        'message': 'success',
        'data': {
            'id': 1,
            'name': '张三',
            'age': 28
        }
    })

    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"状态码: {resp.status_code}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"是否成功: {resp.ok}")
    data = resp.json()
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"业务码: {data['code']}")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print(f"用户名: {data['data']['name']}")

    # 断言验证
    assert resp.status_code == 200, "状态码应为200"
    assert data['code'] == 0, "业务码应为0"
    assert data['data']['name'] == '张三', "用户名不匹配"
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n所有断言通过!")


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
        print("1. 第一部分：HTTP基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：Requests基础")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：接口请求示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：响应处理")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：接口测试封装")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：接口测试用例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 实战任务：编写接口测试")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("8. 参考答案（完成后对照）")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("9. 今日学习要点总结")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("10. 补充：Requests实战练习")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("11. 实战任务")
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
        if choice == "10":
            section10()
        elif choice == "11":
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
