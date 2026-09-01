import logging
from urllib.parse import urljoin

import requests
from config.settings import BASE_URL, TIMEOUT


logger = logging.getLogger(__name__)


class ApiClient:
    """轻量 HTTP 客户端，统一处理 URL、请求日志和超时。"""

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def request(self, method, endpoint, **kwargs):
        url = urljoin(f"{self.base_url}/", endpoint.lstrip("/"))
        logger.info("%s %s", method.upper(), url)
        response = self.session.request(method, url, timeout=TIMEOUT, **kwargs)
        logger.info("%s %s -> %s", method.upper(), url, response.status_code)
        if not response.ok:
            logger.warning("响应体: %s", response.text[:500])
        return response

    def get(self, endpoint, params=None):
        """发送 GET 请求"""
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint, data=None):
        """发送 POST 请求"""
        return self.request("POST", endpoint, json=data)
