import unittest
import price_value

class TestPriceValue(unittest.TestCase):

    def test_that_my_discount_function_exists(self):
        price = 150
        discount = 15 
        self.assertIsNotNone(price_value.get_my_discount(price, discount))

    def test_that_my_discount_function_returns_discounted_price(self):
        price = 150
        discount = 15
        expected_discounted_price = price_value.get_my_discount(price, discount)
        self.assertEqual(expected_discounted_price, 127.5)

    def test_that_my_discount_function_raises_error_with_negative_amount(self):
        price = -150
        discount = 15 
        self.assertRaises(ValueError, price_value.get_my_discount, price, discount)

    def test_that_my_discount_function_raises_error_with_string_value(self):
        price = "byte"
        discount = 15 
        self.assertRaises(TypeError, price_value.get_my_discount, price, discount)





