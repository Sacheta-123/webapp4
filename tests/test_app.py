import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username', response.data)

    def test_login_success(self):
        response = self.client.post('/login', data=dict(
            username='admin', password='admin'
        ), follow_redirects=True)
        self.assertIn(b'You are logged in', response.data)

    def test_login_fail(self):
        response = self.client.post('/login', data=dict(
            username='wrong', password='wrong'
        ), follow_redirects=True)
        self.assertIn(b'Login failed', response.data)

if __name__ == '__main__':
    unittest.main()
