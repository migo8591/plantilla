import unittest


from app.auth.models import Users
from app.admin.models import Post
from . import BaseTestClass


class BlogClientTestCase(BaseTestClass):
    def test_index_with_no_posts(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'No posts available', res.data)
        
if __name__ == '__main__':
    unittest.main()
