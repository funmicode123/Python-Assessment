import unittest
import product



class TestCube(unittest.TestCase):

	def test_that_product_funtion_exit(self):
		product.find_product(2, 3)


	def test_that_product_funtion_return_product_result(self):
		self.assertEqual(product.find_product(2, 3), 6)
		self.assertEqual(product.find_product(5, 4), 20)

	def test_that_product_function_return_product_with_negative_value(self):
		self.assertEqual(product.find_product(-2, 3), -6)
		self.assertEqual(product.find_product(5, -4), -20)
		self.assertEqual(product.find_product(-2, -3), 6)

	def test_that_product_function_return_zero_with_zero_value(self):
		self.assertEqual(product.find_product(3, 0), 0)
		self.assertEqual(product.find_product(0, 5), 0)

	def test_that_product_function_return_error_with_string_value(self):
		self.assertRaises(TypeError, product.find_product, "byte")
