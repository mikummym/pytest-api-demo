import pytest


class TestPosts:
    """测试 /posts 接口"""

    def test_get_all_posts(self, api_client):
        """获取所有文章，验证返回 200 且数据量正确"""
        response = api_client.get("posts")
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == 100  # JSONPlaceholder 固定返回 100 条

    @pytest.mark.parametrize("post_id", [1, 2, 3, 10, 50])
    def test_get_post_by_id(self, api_client, post_id):
        """参数化测试：验证不同 ID 的文章都能正常获取"""
        response = api_client.get(f"posts/{post_id}")
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert "title" in post
        assert "body" in post

    def test_create_post(self, api_client):
        """创建文章，验证返回 201"""
        new_post = {
            "title": "测试文章标题",
            "body": "这是测试文章的内容",
            "userId": 1
        }
        response = api_client.post("posts", data=new_post)
        assert response.status_code == 201
