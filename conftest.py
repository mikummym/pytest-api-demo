import pytest
from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    """提供一个全局的 API 客户端实例"""
    return ApiClient()
