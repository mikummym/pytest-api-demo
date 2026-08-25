import requests
from config.settings import BASE_URL, TIMEOUT

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, params=None):
        """发送 GET 请求"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params, timeout=TIMEOUT)
        return response

    def post(self, endpoint, data=None):
        """发送 POST 请求"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data, timeout=TIMEOUT)
        return response
