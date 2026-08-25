import pytest


class TestUsers:
    """测试 /users 接口"""

    def test_get_all_users(self, api_client):
        """获取所有用户，验证返回 200 且数据非空"""
        response = api_client.get("users")
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_single_user(self, api_client):
        """获取单个用户，验证返回的字段完整"""
        response = api_client.get("users/1")
        assert response.status_code == 200
        user = response.json()
        assert "id" in user
        assert "name" in user
        assert "email" in user

    def test_get_user_not_found(self, api_client):
        """获取不存在的用户，验证返回 404"""
        response = api_client.get("users/9999")
        assert response.status_code == 404

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
        assert "id" in result
