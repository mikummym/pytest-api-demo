import pytest


REQUIRED_USER_FIELDS = {"id", "name", "username", "email"}


class TestUsers:
    """测试 /users 接口"""

    def test_get_all_users(self, api_client):
        """获取所有用户，验证返回 200 且数据非空"""
        response = api_client.get("users")
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert users
        assert REQUIRED_USER_FIELDS <= users[0].keys()

    def test_get_single_user(self, api_client):
        """获取单个用户，验证返回的字段完整"""
        response = api_client.get("users/1")
        assert response.status_code == 200
        user = response.json()
        assert REQUIRED_USER_FIELDS <= user.keys()

    def test_get_user_not_found(self, api_client):
        """获取不存在的用户，验证返回 404"""
        response = api_client.get("users/9999")
        assert response.status_code == 404
        assert response.json() == {}

    def test_create_user(self, api_client):
        """创建用户，验证返回 201 且包含新用户数据"""
        new_user = {
            "name": "测试用户",
            "username": "testuser",
            "email": "test@example.com"
        }
        response = api_client.post("users", data=new_user)
        assert response.status_code == 201
        result = response.json()
        assert result["name"] == new_user["name"]
        assert result["username"] == new_user["username"]
        assert result["email"] == new_user["email"]
        assert "id" in result
