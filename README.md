# pytest-api-demo

基于 Python + pytest + requests 的接口自动化测试框架 Demo，使用 JSONPlaceholder 公开 API 演示接口封装、参数化、异常场景、日志和 CI 测试产物。

## 覆盖范围

- `GET /users`：列表、详情、字段完整性
- `GET /users/9999`：资源不存在的 404 异常场景
- `POST /users`：创建数据与响应字段校验
- `GET /posts`：列表数量、响应结构、参数化详情校验
- `POST /posts`：创建数据与响应字段校验

## 项目结构

```text
pytest-api-demo/
├── config/settings.py       # 环境变量与默认配置
├── utils/api_client.py      # requests.Session 与统一请求日志
├── testcases/               # 接口测试用例
├── conftest.py              # fixture、资源释放、pytest marker
├── pytest.ini               # 测试发现与日志配置
└── .github/workflows/       # GitHub Actions CI
```

## 本地运行

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

生成 JUnit 与 Allure 原始数据：

```powershell
pytest --junitxml=test-results/junit.xml --alluredir=test-results/allure-results
```

可通过环境变量切换测试地址和超时时间：

```powershell
$env:API_BASE_URL = "https://jsonplaceholder.typicode.com"
$env:API_TIMEOUT = "10"
```

## CI

GitHub Actions 会在 push / pull request 时安装依赖、执行测试，并上传 JUnit 与 Allure 原始测试产物，便于定位失败原因。

## 技术栈

Python 3.11+、pytest、requests、Allure Pytest、GitHub Actions
