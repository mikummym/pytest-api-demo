import pytest
from utils.api_client import ApiClient


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: 核心接口冒烟用例")


@pytest.fixture(scope="session")
def api_client():
    """提供一个全局的 API 客户端实例"""
    client = ApiClient()
    yield client
    client.session.close()
