import unittest
from string_int import string_to_number  

class TestStringInt(unittest.TestCase):

    def test_that_string_to_number_function_exists(self):
        result = string_to_number('50', '0')
        self.assertEqual(result, '50')

    def test_positive_numbers(self):
        self.assertEqual(string_to_number('34', '25'), '59')

    def test_zero(self):
        self.assertEqual(string_to_number('0', '0'), '0')

    def test_large_numbers(self):
        self.assertEqual(string_to_number('123', '456'), '579')

    def test_negative_and_positive(self):
        self.assertEqual(string_to_number('-5', '10'), '5')

    def test_result_with_carry(self):
        self.assertEqual(string_to_number('99', '1'), '100')

