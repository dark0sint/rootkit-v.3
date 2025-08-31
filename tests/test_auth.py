# tests/test_auth.py

import unittest
from app.auth import Auth

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()

    def test_login_success(self):
        self.assertTrue(self.auth.login("admin", "admin123"))
        self.assertEqual(self.auth.get_current_user(), "admin")

    def test_login_fail(self):
        self.assertFalse(self.auth.login("admin", "wrongpass"))
        self.assertIsNone(self.auth.get_current_user())

    def test_logout(self):
        self.auth.login("user1", "password1")
        self.auth.logout()
        self.assertIsNone(self.auth.get_current_user())

if __name__ == "__main__":
    unittest.main()
