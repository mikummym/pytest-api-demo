# pytest-api-demo

基于 Python + pytest + requests 的接口自动化测试框架 Demo。

## 测试目标

使用 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 作为公开测
试 API，覆盖：
- GET 请求（单个、批量、异常场景）
- POST 请求（创建资源）
- 参数化测试
- 响应数据校验

## 项目结构

pytest-api-demo/    
├── config/          # 全局配置     
├── utils/           # 工具类（HTTP 客户端封装）  
├── testcases/       # 测试用例     
├── conftest.py      # pytest fixtures      
├── pytest.ini       # pytest 配置    
└── .github/         # GitHub Actions CI


## 环境搭建

1. 创建虚拟环境   
────────────────────────────────────────    
python -m venv venv


2. 激活虚拟环境（Windows）  
────────────────────────────────────────    
venv\Scripts\activate


3. 安装依赖  
────────────────────────────────────────     
pip install -r requirements.txt

## 运行测试

运行全部测试  
────────────────────────────────────────    
pytest

运行并显示详细输出   
────────────────────────────────────────    
pytest -v

运行指定文件  
────────────────────────────────────────    
pytest testcases/test_users.py
    
## 技术栈

- Python 3.11+
- pytest
- requests
- GitHub Actions