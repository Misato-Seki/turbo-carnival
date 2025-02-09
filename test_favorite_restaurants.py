# python -m unittest test_favorite_restaurants.py
import unittest
from Order_Placement import UserProfile

class TestFavoriteRestaurants(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile(delivery_address="123 Main St")
        self.user_profile.favorites = []

    def test_add_favorite_restaurant(self):
        self.user_profile.add_favorite("Sushi House")
        self.assertIn("Sushi House", self.user_profile.favorites)

    def test_remove_favorite_restaurant(self):
        self.user_profile.add_favorite("Sushi House")
        self.user_profile.remove_favorite("Sushi House")
        self.assertNotIn("Sushi House", self.user_profile.favorites)

    def test_view_favorite_restaurants(self):
        self.user_profile.add_favorite("Sushi House")
        self.user_profile.add_favorite("Burger King")
        favorites = self.user_profile.view_favorites()
        self.assertEqual(favorites, ["Sushi House", "Burger King"])

if __name__ == '__main__':
    unittest.main()
