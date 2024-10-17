import unittest
import swapinteger  

class TestSwapInteger(unittest.TestCase):

    def test_that_numbersort_function_exists(self):
        number = [1, 2, 3, 4, 5, 6]
        expected_output = swapinteger.number_sort(number)  
        self.assertIsNotNone(expected_output)  

    def test_that_numbersort_function_returns_correct_result(self):
        number = [1, 2, 3, 4, 5, 6]
        expected_output = [2, 1, 4, 3, 6, 5]
        self.assertListEqual(swapinteger.number_sort(number), expected_output)
