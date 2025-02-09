# python -m unittest test_multi_address.py
import unittest
from Order_Placement import UserProfile

class TestMultipleAddresses(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile(delivery_address="123 Main St")

    def test_add_address(self):
        self.user_profile.add_address("Home", "123 Main St")
        self.assertIn("Home", self.user_profile.addresses)
        self.assertEqual(self.user_profile.addresses["Home"], "123 Main St")

    def test_switch_address(self):
        self.user_profile.add_address("Home", "123 Main St")
        self.user_profile.add_address("Work", "456 Office Rd")
        self.user_profile.switch_address("Work")
        self.assertEqual(self.user_profile.current_address, "456 Office Rd")

    def test_remove_address(self):
        self.user_profile.add_address("Home", "123 Main St")
        self.user_profile.remove_address("Home")
        self.assertNotIn("Home", self.user_profile.addresses)

if __name__ == '__main__':
    unittest.main()
