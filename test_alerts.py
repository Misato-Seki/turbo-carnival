# python -m unittest test_alerts.py
import unittest
from Order_Placement import OrderPlacement, Cart, UserProfile, RestaurantMenu

class TestOrderStatusUpdates(unittest.TestCase):
    def setUp(self):
        self.order = OrderPlacement(Cart(), UserProfile("123 Main St"), RestaurantMenu(["Pizza", "Burger"]))
        self.order.status = "Pending"

    def test_update_order_status(self):
        self.order.update_status("Preparing")
        self.assertEqual(self.order.status, "Preparing")

    def test_receive_order_status_notification(self):
        notifications = []
        def mock_notify(status):
            notifications.append(status)
        
        self.order.notify = mock_notify
        self.order.update_status("Out for Delivery")
        self.assertIn("Out for Delivery", notifications)

if __name__ == '__main__':
    unittest.main()
