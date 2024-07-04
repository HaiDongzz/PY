import unittest

from login_module import LoginModule


class TestLoginModule(unittest.TestCase):

    def setUp(self):
        self.login_module = LoginModule()

    def test_login_success(self):
        username = "admin"
        password = "password"
        result = self.login_module.login(username, password)
        self.assertTrue(result)

    def test_login_invalid_username(self):
        username = "invalid_username"
        password = "password"
        result = self.login_module.login(username, password)
        self.assertFalse(result)

    def test_login_invalid_password(self):
        username = "admin"
        password = "invalid_password"
        result = self.login_module.login(username, password)
        self.assertFalse(result)

    def test_login_empty_credentials(self):
        username = ""
        password = ""
        result = self.login_module.login(username, password)
        self.assertFalse(result)

    def tearDown(self):
        # 可选的清理方法，在每个测试方法执行后调用
        pass


if __name__ == '__main__':
    unittest.main()
