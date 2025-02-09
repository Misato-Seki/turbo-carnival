# python -m unittest test_order_history.py
import unittest
from User_Registration import UserRegistration
from order_history import OrderHistory

class TestOrderHistory(unittest.TestCase):
    
    def setUp(self):
        """
        テスト環境をセットアップするため、UserRegistration と OrderHistory を初期化します。
        """
        self.registration = UserRegistration()  # UserRegistrationクラスを初期化
        self.order_history = OrderHistory()  # OrderHistoryクラスを初期化
        self.registration.register("user@example.com", "Password123", "Password123")  # 新規ユーザーを登録

    def test_view_order_history(self):
        """
        ユーザーが過去の注文履歴を確認できるかをテストします。
        """
        result = self.order_history.view_order_history("user@example.com")
        self.assertEqual(result['success'], False)  # 注文履歴がまだないので、失敗を期待
        self.assertEqual(result['error'], "No orders found")  # 注文履歴がないエラーを確認

    def test_add_order_and_view_history(self):
        """
        注文を追加し、その後注文履歴が正しく表示されるかをテストします。
        """
        # 注文をシミュレート
        self.order_history.add_order("user@example.com", {"item": "Pizza", "price": 12.99})
        
        result = self.order_history.view_order_history("user@example.com")
        self.assertEqual(result['success'], True)  # 注文履歴が表示されることを期待
        self.assertEqual(len(result['orders']), 1)  # 1つの注文があることを確認
        self.assertEqual(result['orders'][0]['item'], "Pizza")  # 注文内容が正しいことを確認
