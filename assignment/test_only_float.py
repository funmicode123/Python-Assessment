import unittest
import only_float

class TestOnlyFloat(unittest.TestCase):

    def test_that_only_float_exists(self):
        number1 = 3.4
        number2 = 12
        self.assertIsNotNone(only_float.check_for_float(number1))
        self.assertIsNotNone(only_float.check_for_float(number2))

    def test_that_get_both_float_funtion_return_int(self):
        number1 = 3.4
        number2 = 12.5
        result = only_float.get_both_float(number1, number2)
        self.assertIsInstance(result, int)

    def test_that_get_one_float_funtion_return_int(self):
        number1 = 3.4
        number2 = 12
        result = only_float.get_one_float(number1, number2)
        self.assertIsInstance(result, int)

    def test_that_get_none_float_funtion_return_int(self):
        number1 = 3
        number2 = 12
        result = only_float.get_none_float(number1, number2)
        self.assertIsInstance(result, int)

    def test_that_check_for_float_function_return_error_with_string_value(self):
        number1 = "Invalid"
        number2 = 12.5
        self.assertRaises(TypeError, only_float.check_for_float, number1, number2)


