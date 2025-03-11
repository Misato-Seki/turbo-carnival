# python -m unittest tests/functional_tests/test_user_registration.py    
import unittest
from User_Registration import UserRegistration

class TestUserRegistrationFunctional(unittest.TestCase):
    
    def setUp(self):
        """
        テスト環境をセットアップ: UserRegistration インスタンスを作成
        """
        self.registration = UserRegistration()

    def test_register_user_successfully(self):
        """
        正しい情報を入力してユーザー登録が成功するかをテストする
        """
        response = self.registration.register("testuser@example.com", "TestPass123", "TestPass123")
        
        # 登録が成功したかを確認
        self.assertTrue(response["success"])
        self.assertEqual(response["message"], "Registration successful, confirmation email sent")

        # 登録されたユーザー情報が正しいか確認
        self.assertIn("testuser@example.com", self.registration.users)
        self.assertEqual(self.registration.users["testuser@example.com"]["password"], "TestPass123")
        self.assertFalse(self.registration.users["testuser@example.com"]["confirmed"])  # 初期状態では confirmed は False

    def test_register_user_with_invalid_email(self):
        """
        無効なメールアドレスを使用した場合に登録が失敗するかをテストする
        """
        response = self.registration.register("invalid-email", "TestPass123", "TestPass123")
        
        # 失敗することを確認
        self.assertFalse(response["success"])
        self.assertEqual(response["error"], "Invalid email format")

    def test_register_user_with_mismatched_passwords(self):
        """
        パスワードと確認用パスワードが一致しない場合に登録が失敗するかをテストする
        """
        response = self.registration.register("testuser@example.com", "TestPass123", "WrongPass123")
        
        # 失敗することを確認
        self.assertFalse(response["success"])
        self.assertEqual(response["error"], "Passwords do not match")

if __name__ == '__main__':
    unittest.main()
