import unittest
from app.main import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'Hello, Devops World!', response.data)


if __name__ == '__main__':
    unittest.main()
