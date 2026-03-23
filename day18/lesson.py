# -*- coding: utf-8 -*-
"""
Day 18: Day 18
"""


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section1():
    """第一部分：接口鉴权方式"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第一部分：接口鉴权方式")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    常见接口鉴权方式:
    1. Basic Auth (基本认证)
       - 用户名:密码的Base64编码
       - Authorization: Basic dXNlcjpwYXNz
    2. Bearer Token (令牌认证)
       - 最常用的方式
       - Authorization: Bearer <token>
    3. API Key
       - 在Header或Query参数中传递
       - X-API-Key: your_api_key
    4. OAuth 2.0
       - 授权码模式
       - 简化模式
       - 密码凭证模式
       - 客户端凭证模式
    5. HMAC (哈希消息认证码)
       - 使用密钥生成签名
       - 防止请求被篡改
    """


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section2():
    """第二部分：鉴权实现"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第二部分：鉴权实现")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class AuthHelper:
        """鉴权辅助类"""
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def basic_auth():
            """
            生成Basic Auth头
            参数:
                username: 用户名
                password: 密码
            返回:
                Authorization头值
            """
            credentials = f"{username}:{password}"
            encoded = base64.b64encode(credentials.encode()).decode()
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return f"Basic {encoded}"
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def bearer_token():
            """
            生成Bearer Token头
            参数:
                token: 访问令牌
            返回:
                Authorization头值
            """
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return f"Bearer {token}"
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def hmac_signature():
            """
            生成HMAC签名
            参数:
                secret_key: 密钥
                message: 消息内容
                algorithm: 哈希算法
            返回:
                签名值
            """
            key = secret_key.encode()
            msg = message.encode()
            if algorithm == 'sha256':
                signature = hmac.new(key, msg, hashlib.sha256).hexdigest()
            elif algorithm == 'sha512':
                signature = hmac.new(key, msg, hashlib.sha512).hexdigest()
            else:
                # raise - 主动抛出异常
                # 作用: 当遇到错误条件时，主动抛出异常
                raise ValueError(f"不支持的算法: {algorithm}")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return signature
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def generate_timestamp():
            """生成时间戳"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section3():
    """第三部分：带鉴权的API客户端"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第三部分：带鉴权的API客户端")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class AuthenticatedAPIClient:
        """
        带鉴权的API客户端
        """
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.base_url = base_url.rstrip("/")
            self.headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            self.auth_token = None
            self.refresh_token = None
            self.token_expires_at = None
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def set_basic_auth():
            """设置Basic Auth"""
            auth_header = AuthHelper.basic_auth(username, password)
            self.headers["Authorization"] = auth_header
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def set_bearer_token():
            """设置Bearer Token"""
            self.auth_token = token
            self.headers["Authorization"] = AuthHelper.bearer_token(token)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def set_api_key():
            """设置API Key"""
            self.headers[header_name] = api_key
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def set_hmac_auth():
            """
            设置HMAC认证
            每次请求都会生成新的签名
            """
            self.hmac_secret = secret_key
            self.hmac_access_key = access_key
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _add_hmac_headers():
            """添加HMAC签名头"""
            timestamp = AuthHelper.generate_timestamp()
            # 构建待签名字符串
            message_parts = [method.upper(), endpoint, timestamp]
            if body:
                body_str = json.dumps(body) if isinstance(body, dict) else str(body)
                # append() - 列表末尾添加元素
                # 语法: 列表.append(元素)
                # 返回值: None（直接修改原列表）
                message_parts.append(body_str)
            message = "|".join(message_parts)
            signature = AuthHelper.hmac_signature(self.hmac_secret, message)
            self.headers["X-Access-Key"] = self.hmac_access_key
            self.headers["X-Timestamp"] = timestamp
            self.headers["X-Signature"] = signature
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def _request():
            """发送请求"""
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            # 如果有HMAC认证，生成签名
            if hasattr(self, 'hmac_secret'):
                body = kwargs.get('json') or kwargs.get('data')
                self._add_hmac_headers(method, endpoint, body)
            # 合并headers
            headers = {**self.headers, **kwargs.pop('headers', {})}
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"\n[{method}] {url}")
            # print() - 打印输出
            # 语法: print(值1, 值2, ..., sep=" ", end="\n")
            # 作用: 把内容输出到控制台
            print(f"Headers: {headers}")
            if 'json' in kwargs:
                # print() - 打印输出
                # 语法: print(值1, 值2, ..., sep=" ", end="\n")
                # 作用: 把内容输出到控制台
                print(f"Body: {kwargs['json']}")
            # 模拟请求 (实际使用requests)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return MockResponse(200, {"success": True})
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get():
            """GET请求"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._request("GET", endpoint, **kwargs)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def post():
            """POST请求"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._request("POST", endpoint, **kwargs)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def put():
            """PUT请求"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._request("PUT", endpoint, **kwargs)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def delete():
            """DELETE请求"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self._request("DELETE", endpoint, **kwargs)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class MockResponse:
        """模拟响应"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def __init__():
            self.status_code = status_code
            self._json = json_data
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
def section4():
    """第四部分：高级断言"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第四部分：高级断言")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class APIAssertions:
        """
        接口测试高级断言
        """
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_schema():
            """
            断言JSON Schema
            参数:
                data: 实际数据
                schema: 期望的schema
            示例schema:
            {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
                "required": ["id", "name"]
            }
            """
            # 简化版schema检查
            if schema.get("type") == "object":
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert isinstance(data, dict), f"期望对象类型，实际: {type(data)}"
                # 检查必需字段
                for field in schema.get("required", []):
                    # assert - 断言
                    # 语法: assert 条件, 错误信息
                    # 作用: 条件为False时抛出AssertionError
                    assert field in data, f"缺少必需字段: {field}"
                # 检查字段类型
                for field, field_schema in schema.get("properties", {}).items():
                    if field in data:
                        expected_type = field_schema.get("type")
                        if expected_type == "string":
                            # assert - 断言
                            # 语法: assert 条件, 错误信息
                            # 作用: 条件为False时抛出AssertionError
                            assert isinstance(data[field], str)
                        elif expected_type == "integer":
                            # assert - 断言
                            # 语法: assert 条件, 错误信息
                            # 作用: 条件为False时抛出AssertionError
                            assert isinstance(data[field], int)
                        elif expected_type == "array":
                            # assert - 断言
                            # 语法: assert 条件, 错误信息
                            # 作用: 条件为False时抛出AssertionError
                            assert isinstance(data[field], list)
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_response_time():
            """
            断言响应时间
            参数:
                response_time: 实际响应时间(秒)
                max_time: 最大允许时间
            """
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response_time <= max_time, \
                f"响应时间 {response_time}s 超过阈值 {max_time}s"
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_pagination():
            """
            断言分页数据
            参数:
                data: 响应数据
                expected_keys: 期望包含的键
            """
            expected_keys = expected_keys or ["items", "total", "page", "per_page"]
            for key in expected_keys:
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert key in data, f"分页数据缺少字段: {key}"
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_error_response():
            """
            断言错误响应
            参数:
                response: 响应对象
                expected_status: 期望状态码
                expected_code: 期望错误码
            """
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == expected_status, \
                f"期望状态码 {expected_status}, 实际 {response.status_code}"
            data = response.json()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "error" in data or "message" in data, "错误响应应包含error或message"
            if expected_code:
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert data.get("code") == expected_code, \
                    f"期望错误码 {expected_code}, 实际 {data.get('code')}"
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_list_not_empty():
            """断言列表不为空"""
            items = data.get(list_key, [])
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert len(items) > 0, f"列表 {list_key} 为空"
        # 【装饰器 @staticmethod】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @staticmethod
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def assert_field_types():
            """
            断言字段类型
            参数:
                data: 数据字典
                field_types: 字段类型映射 {field: type}
            """
            for field, expected_type in field_types.items():
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert field in data, f"缺少字段: {field}"
                actual_type = type(data[field])
                # assert - 断言
                # 语法: assert 条件, 错误信息
                # 作用: 条件为False时抛出AssertionError
                assert actual_type == expected_type, \
                    f"字段 {field}: 期望类型 {expected_type}, 实际 {actual_type}"


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section5():
    """第五部分：测试示例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第五部分：测试示例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_auth():
        """演示鉴权"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("鉴权演示")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # 1. Basic Auth
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. Basic Auth:")
        client = AuthenticatedAPIClient("https://api.example.com")
        client.set_basic_auth("admin", "password123")
        # get() - 安全获取字典值
        # 语法: 字典.get(键, 默认值)
        # 作用: 获取键对应的值，不存在返回默认值（不会报错）
        client.get("/users")
        # 2. Bearer Token
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. Bearer Token:")
        client = AuthenticatedAPIClient("https://api.example.com")
        client.set_bearer_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
        # get() - 安全获取字典值
        # 语法: 字典.get(键, 默认值)
        # 作用: 获取键对应的值，不存在返回默认值（不会报错）
        client.get("/users")
        # 3. API Key
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n3. API Key:")
        client = AuthenticatedAPIClient("https://api.example.com")
        client.set_api_key("sk_live_1234567890abcdef")
        # get() - 安全获取字典值
        # 语法: 字典.get(键, 默认值)
        # 作用: 获取键对应的值，不存在返回默认值（不会报错）
        client.get("/users")
        # 4. HMAC
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n4. HMAC认证:")
        client = AuthenticatedAPIClient("https://api.example.com")
        client.set_hmac_auth(
            secret_key="my_secret_key",
            access_key="my_access_key"
        )
        client.post("/orders", json={"product_id": 1, "quantity": 2})
    # 【函数定义】
    # 语法: def 函数名(参数):
    # 作用: 封装可复用的代码块
    # 调用: 函数名(参数)
    def demo_assertions():
        """演示高级断言"""
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n" + "="*60)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("高级断言演示")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("="*60)
        # Schema断言
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n1. Schema断言:")
        user_data = {
            "id": 1,
            "name": "John",
            "email": "john@example.com"
        }
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "email": {"type": "string"}
            },
            "required": ["id", "name"]
        }
        APIAssertions.assert_schema(user_data, schema)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  Schema检查通过")
        # 分页断言
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n2. 分页断言:")
        paginated_data = {
            "items": [{"id": 1}, {"id": 2}],
            "total": 100,
            "page": 1,
            "per_page": 10
        }
        APIAssertions.assert_pagination(paginated_data)
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  分页数据检查通过")
        # 字段类型断言
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("\n3. 字段类型断言:")
        APIAssertions.assert_field_types(user_data, {
            "id": int,
            "name": str,
            "email": str
        })
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("  字段类型检查通过")


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section6():
    """第六部分：完整的接口测试用例"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("第六部分：完整的接口测试用例")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestAuthAPI:
        """带鉴权的接口测试"""
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def client():
            """未认证客户端"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return AuthenticatedAPIClient("https://api.example.com")
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def auth_client():
            """已认证客户端"""
            # 模拟登录获取token
            client.set_bearer_token("fake_access_token")
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return client
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_public_endpoint():
            """测试公开接口"""
            response = client.get("/public/info")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_protected_endpoint_without_auth():
            """测试未认证访问受保护接口"""
            response = client.get("/protected/user")
            # 应该返回401
            APIAssertions.assert_error_response(response, 401)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_protected_endpoint_with_auth():
            """测试已认证访问受保护接口"""
            response = auth_client.get("/protected/user")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
            data = response.json()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "user" in data
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_api_key_auth():
            """测试API Key认证"""
            client.set_api_key("valid_api_key")
            response = client.get("/api/v1/data")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_hmac_auth():
            """测试HMAC认证"""
            client.set_hmac_auth("secret_key", "access_key")
            response = client.post("/api/v1/orders", json={
                "product_id": 1,
                "quantity": 2
            })
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200


# 【函数定义】
# 语法: def 函数名(参数):
# 作用: 封装可复用的代码块
# 调用: 函数名(参数)
def section7():
    """实战任务：完整的接口测试"""
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("\n" + "="*60)
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("实战任务：完整的接口测试")
    # print() - 打印输出
    # 语法: print(值1, 值2, ..., sep=" ", end="\n")
    # 作用: 把内容输出到控制台
    print("="*60)
    """
    任务：为电商系统编写完整的接口测试
    要求:
    1. 实现登录获取token
    2. 使用token访问需要认证的接口
    3. 测试商品CRUD
    4. 测试订单创建和查询
    5. 使用高级断言验证响应
    """
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class ECommerceAPIClient(AuthenticatedAPIClient):
        """电商API客户端"""
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def login():
            """登录并设置token"""
            response = self.post("/auth/login", json={
                "username": username,
                "password": password
            })
            if response.status_code == 200:
                token = response.json().get("token")
                self.set_bearer_token(token)
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return response
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_products():
            """获取商品列表"""
            params = {"category": category} if category else None
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get("/products", params=params)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def create_product():
            """创建商品 (需要管理员权限)"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.post("/admin/products", json={
                "name": name,
                "price": price,
                "stock": stock
            })
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def create_order():
            """创建订单"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.post("/orders", json={
                "items": items,
                "address": address
            })
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def get_order():
            """获取订单详情"""
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return self.get(f"/orders/{order_id}")
    # 请完成下面的测试用例
    # 【类定义】
    # 语法: class 类名:
    # 作用: 创建对象模板，封装数据和方法
    class TestECommerceAPI:
        """电商接口测试"""
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
    class TestECommerceAPI:
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
            return ECommerceAPIClient("https://api.example.com")
        # 【装饰器 @pytest】
        # 作用: 在不修改原函数的情况下，添加额外功能
        # 原理: 接收函数作为参数，返回新函数
        @pytest.fixture
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def logged_in_client():
            response = client.login("admin", "123456")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
            # return - 返回值
            # 作用: 将结果返回给调用者，结束函数执行
            return client
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_success():
            response = client.login("admin", "123456")
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "token" in response.json()
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_login_failure():
            response = client.login("admin", "wrong_password")
            APIAssertions.assert_error_response(response, 401)
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_get_products():
            response = client.get_products()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
            APIAssertions.assert_pagination(response.json())
            APIAssertions.assert_list_not_empty(response.json())
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_create_product():
            response = logged_in_client.create_product(
                name="iPhone 15",
                price=9999,
                stock=100
            )
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 201
            data = response.json()
            APIAssertions.assert_field_types(data, {
                "id": int,
                "name": str,
                "price": (int, float),
                "stock": int
            })
        # 【函数定义】
        # 语法: def 函数名(参数):
        # 作用: 封装可复用的代码块
        # 调用: 函数名(参数)
        def test_create_order():
            # 创建订单
            response = logged_in_client.create_order(
                items=[{"product_id": 1, "quantity": 2}],
                address="北京市朝阳区"
            )
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 201
            order_id = response.json().get("order_id")
            # 查询订单
            response = logged_in_client.get_order(order_id)
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert response.status_code == 200
            order = response.json()
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert order["id"] == order_id
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "items" in order
            # assert - 断言
            # 语法: assert 条件, 错误信息
            # 作用: 条件为False时抛出AssertionError
            assert "total" in order
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
    1. 接口鉴权:
       - Basic Auth: 用户名密码Base64编码
       - Bearer Token: 最常用的token认证
       - API Key: 简单密钥认证
       - HMAC: 签名认证，防篡改
    2. 鉴权实现:
       - 封装AuthHelper类
       - APIClient支持多种认证方式
       - 自动添加认证头
    3. 高级断言:
       - Schema验证
       - 响应时间断言
       - 分页数据断言
       - 错误响应断言
       - 字段类型断言
    4. 测试实践:
       - 登录获取token
       - 使用fixture共享认证客户端
       - 测试认证和未认证场景
    验证标准：能完成带鉴权的接口自动化测试
    """
    # 运行演示
    if __name__ == "__main__":
        demo_auth()
        demo_assertions()

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
        print("1. 第一部分：接口鉴权方式")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("2. 第二部分：鉴权实现")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("3. 第三部分：带鉴权的API客户端")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("4. 第四部分：高级断言")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("5. 第五部分：测试示例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("6. 第六部分：完整的接口测试用例")
        # print() - 打印输出
        # 语法: print(值1, 值2, ..., sep=" ", end="\n")
        # 作用: 把内容输出到控制台
        print("7. 实战任务：完整的接口测试")
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
        print("9. 实战任务")
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
        elif choice == "9":
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
