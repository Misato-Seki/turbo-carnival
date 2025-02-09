# python -m unittest test_rating.py
import unittest
from Order_Placement import UserProfile

class TestDishRating(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile(delivery_address="123 Main St")
        self.user_profile.ratings = {}

    def test_add_dish_rating(self):
        self.user_profile.add_rating("Pizza", 5)
        self.assertEqual(self.user_profile.ratings["Pizza"], 5)

    def test_view_dish_rating(self):
        self.user_profile.add_rating("Pizza", 5)
        rating = self.user_profile.view_rating("Pizza")
        self.assertEqual(rating, 5)

    def test_view_nonexistent_dish_rating(self):
        rating = self.user_profile.view_rating("Burger")
        self.assertIsNone(rating)

if __name__ == '__main__':
    unittest.main()
