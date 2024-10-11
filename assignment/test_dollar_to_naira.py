import unittest
import dollar_to_naira


class TestDollarToNaira(unittest.TestCase):

	def test_that_dollar_to_naira_funtion_exist(self):
		dollar_to_naira.get_naira(1550)

	def test_that_dollar_to_naira_function_returns_naira(self):
		dollar = 10
		expected_naira = dollar * 1550
		self.assertEqual(dollar_to_naira.get_naira(dollar), expected_naira)

	def test_that_dollar_to_naira_function_raises_error_with_negative_amount(self):
		self.assertRaises(ValueError, dollar_to_naira.get_naira, -3)
	
	def test_that_dollar_to_naira_function_raises_error_with_string_value(self):
		self.assertRaises(TypeError, dollar_to_naira.get_naira, "byte")