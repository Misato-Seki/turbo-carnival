import time
import unittest
from Order_Placement import Cart, UserProfile, RestaurantMenu, OrderPlacement, PaymentMethod

class TestPerformance(unittest.TestCase):
    def test_add_items_to_cart_performance(self):
        # Set up a large number of items to simulate load
        cart = Cart()
        
        # Simulate adding 1000 items to the cart
        start_time = time.time()
        
        for i in range(1000):
            cart.add_item(f"Item {i}", 10.0, 1)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Assert that adding 1000 items should take less than 5 seconds (for example)
        self.assertLess(elapsed_time, 5, f"Adding 1000 items took too long: {elapsed_time:.2f} seconds")
        
    def test_checkout_performance(self):
        # Simulate a full checkout process for performance testing
        cart = Cart()
        cart.add_item("Burger", 5.0, 2)
        cart.add_item("Pizza", 8.0, 3)
        
        user_profile = UserProfile("123 Main St")
        restaurant_menu = RestaurantMenu(["Burger", "Pizza", "Pasta"])
        
        order_placement = OrderPlacement(cart, user_profile, restaurant_menu)
        
        start_time = time.time()
        
        # Simulate the checkout process
        order_placement.validate_order()
        order_placement.proceed_to_checkout()
        order_placement.confirm_order(PaymentMethod())
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Assert that the checkout process completes within a reasonable time (e.g., 2 seconds)
        self.assertLess(elapsed_time, 2, f"Checkout took too long: {elapsed_time:.2f} seconds")

if __name__ == '__main__':
    unittest.main()
