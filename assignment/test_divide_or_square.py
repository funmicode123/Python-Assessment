import unittest
import math
import divide_or_square  

class TestDivideOrSquare(unittest.TestCase):

    def test_that_divide_or_square_function_exists(self):
        divide_or_square.get_divide(5)

    def test_that_divide_function_returns_divide(self):
        number = 12
        expected_result = number % 5
        self.assertEqual(divide_or_square.get_divide(number), expected_result)

    def test_that_square_function_returns_squareroot(self):
        number = 25
        expected_result = math.sqrt(number)
        self.assertEqual(divide_or_square.get_square(number), expected_result)

    def test_that_divide_function_returns_no_remainder_message(self):
        number = 15
        expected_result = "Number is divisible by 5, no remainder."
        self.assertEqual(divide_or_square.get_divide(number), expected_result)

    def test_that_divide_function_raises_error_with_negative_amount(self):
        self.assertRaises(ValueError, divide_or_square.get_divide, -3)

    def test_that_square_function_raises_error_with_negative_amount(self):
        self.assertRaises(ValueError, divide_or_square.get_square, -3)

    def test_that_divide_function_raises_error_with_string_value(self):
        with self.assertRaises(TypeError):
            divide_or_square.get_divide("byte")

    def test_that_square_function_raises_error_with_string_value(self):
        with self.assertRaises(TypeError):
            divide_or_square.get_square("byte")


