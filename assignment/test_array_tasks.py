import unittest
import array_tasks

class TestArrayTasks(unittest.TestCase):

    def test_that_array_tasks_function_return_largest(self):
        values = [10, 20, 30, 40, 50]
        largest_element = 50
        self.assertEqual(array_tasks.largest_number(values), largest_element)

    def test_that_array_tasks_function_return_largest_with_negative_integer(self):
        values = [-10, -20, -30, -40, -50]
        largest_element = -10
        self.assertEqual(array_tasks.largest_number(values), largest_element)

    def test_that_array_tasks_function_return_largest_with_single_integer(self):
        values = [10]
        largest_element = 10
        self.assertEqual(array_tasks.largest_number(values), largest_element)

    def test_empty_list_raises_value_error(self):
        values = []
        with self.assertRaises(ValueError): array_tasks.largest_number(values)

    def test_that_the_list_reverse_basic_list(self):
        values = [1, 2, 3, 4, 5]
        expected_result = [5, 4, 3, 2, 1]
        self.assertEqual(array_tasks.reverse_list(values), expected_result)

    def test_reverse_single_element_list(self):
        values = [10]
        expected_result = [10]
        self.assertEqual(array_tasks.reverse_list(values), expected_result)

    def test_reverse_empty_list(self):
        values = []
        expected_result = []
        self.assertEqual(array_tasks.reverse_list(values), expected_result)

    def test_reverse_mixed_element_list(self):
        values = [1, "apple", 2.5, True]
        expected_result = [True, 2.5, "apple", 1]
        self.assertEqual(array_tasks.reverse_list(values), expected_result)

    def test_element_present(self):
        values = [1, 2, 3, 4, 5]
        element = 3
        self.assertTrue(array_tasks.is_element_present(values, element))

    def test_element_not_present(self): 
        values = [1, 2, 3, 4, 5]
        element = 8
        self.assertFalse(array_tasks.is_element_present(values, element))

    def test_element_present_in_empty_list(self):
        values = []
        element = 3
        self.assertFalse(array_tasks.is_element_present(values, element))

    def test_element_present_in_mixed_elements(self):
        values = [1, "apple", 2.5, True]
        element = "apple"
        self.assertTrue(array_tasks.is_element_present(values, element))

    def test_element_not_present_in_mixed_elements(self):
        values = [1, "apple", 2.5, True]
        element = False
        self.assertFalse(array_tasks.is_element_present(values, element))


#ODD & EVEN


    def test_compute_total_list(self):
        values = [1, 2, 3, 4, 5]
        expected_total = 15
        self.assertEqual(array_tasks.compute_total(values), expected_total)

    def test_compute_total_with_negative_numbers(self):
        values = [-1, -2, -3, -4, -5]
        expected_total = -15
        self.assertEqual(array_tasks.compute_total(values), expected_total)

    def test_compute_total_empty_list(self):
        values = []
        expected_total = 0
        self.assertEqual(array_tasks.compute_total(values), expected_total)

    def test_compute_total_mixed_numbers(self):
        values = [1, -2, 3, -4, 5]
        expected_total = 3
        self.assertEqual(array_tasks.compute_total(values), expected_total)

    def test_compute_total_single_element(self):
        values = [10]
        expected_total = 10
        self.assertEqual(array_tasks.compute_total(values), expected_total)

    def test_palindrome_basic(self):
        string_element = "madam"
        self.assertTrue(array_tasks.is_string_palindrome(string_element))

    def test_non_palindrome(self):
        string_element = "hello"
        self.assertFalse(array_tasks.is_string_palindrome(string_element))

    def test_empty_string(self):
        string_element = ""
        self.assertTrue(array_tasks.is_string_palindrome(string_element))

    def test_single_character_string(self):
        string_element = "a"
        self.assertTrue(array_tasks.is_string_palindrome(string_element))

    def test_palindrome_mixed_case(self):
        string_element = "Madam"
        self.assertTrue(array_tasks.is_string_palindrome(string_element.lower()))

    def test_compute_total_list(self):
        values = [1, 2, 3, 4, 5]
        expected_total = 15
        self.assertEqual(array_tasks.compute_sum_while(values), expected_total)

    def test_compute_total_with_negative_numbers(self):
        values = [-1, -2, -3, -4, -5]
        expected_total = -15
        self.assertEqual(array_tasks.compute_sum_while(values), expected_total)

    def test_compute_total_empty_list(self):
        values = []
        expected_total = 0
        self.assertEqual(array_tasks.compute_sum_while(values), expected_total)

    def test_compute_total_mixed_numbers(self):
        values = [1, -2, 3, -4, 5]
        expected_total = 3
        self.assertEqual(array_tasks.compute_sum_while(values), expected_total)

    def test_compute_total_single_element(self):
        values = [10]
        expected_total = 10
        self.assertEqual(array_tasks.compute_sum_while(values), expected_total)

    def test_compute_total_list(self):
        values = [1, 2, 3, 4, 5]
        expected_total = 15
        self.assertEqual(array_tasks.compute_sum_do(values), expected_total)

    def test_compute_total_with_negative_numbers(self):
        values = [-1, -2, -3, -4, -5]
        expected_total = -15
        self.assertEqual(array_tasks.compute_sum_do(values), expected_total)

    def test_compute_total_empty_list(self):
        values = []
        expected_total = 0
        self.assertEqual(array_tasks.compute_sum_do(values), expected_total)

    def test_compute_total_mixed_numbers(self):
        values = [1, -2, 3, -4, 5]
        expected_total = 3
        self.assertEqual(array_tasks.compute_sum_do(values), expected_total)

    def test_compute_total_single_element(self):
        values = [10]
        expected_total = 10
        self.assertEqual(array_tasks.compute_sum_do(values), expected_total)

    def test_concatenate_non_empty_values_and_sets(self):
        values = [1, 2, 3]
        sets = [4, 5, 6]
        expected_result = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(array_tasks.concatenate_sets(values, sets), expected_result)

    def test_concatenate_empty_values_and_non_empty_sets(self):
        values = []
        sets = [4, 5, 6]
        expected_result = [[4, 5, 6]]
        self.assertEqual(array_tasks.concatenate_sets(values, sets), expected_result)

    def test_concatenate_non_empty_values_and_empty_sets(self):
        values = [1, 2, 3]
        sets = []
        expected_result = [[1, 2, 3]]
        self.assertEqual(array_tasks.concatenate_sets(values, sets), expected_result)

    def test_concatenate_both_empty(self):
        values = []
        sets = []
        expected_result = [[]]
        self.assertEqual(array_tasks.concatenate_sets(values, sets), expected_result)

    def test_concatenate_mixed_data_types(self):
        values = [1, "apple", 2.5]
        sets = ["banana", True]
        expected_result = [[1, "apple", 2.5, "banana", True]]
        self.assertEqual(array_tasks.concatenate_sets(values, sets), expected_result)

    def test_merge_alternating_equal_length(self):
        values = [1, 2, 3]
        sets = ['a', 'b', 'c']
        expected_result = [1, 'a', 2, 'b', 3, 'c']
        self.assertEqual(array_tasks.merge_alternating(values, sets), expected_result)

    def test_merge_alternating_values_longer(self):
        values = [1, 2, 3, 4]
        sets = ['a', 'b']
        expected_result = [1, 'a', 2, 'b', 3, 4]
        self.assertEqual(array_tasks.merge_alternating(values, sets), expected_result)

    def test_merge_alternating_sets_longer(self):
        values = [1, 2]
        sets = ['a', 'b', 'c', 'd']
        expected_result = [1, 'a', 2, 'b', 'c', 'd']
        self.assertEqual(array_tasks.merge_alternating(values, sets), expected_result)

    def test_merge_alternating_both_empty(self):
        values = []
        sets = []
        expected_result = []
        self.assertEqual(array_tasks.merge_alternating(values, sets), expected_result)

    def test_merge_alternating_mixed_data_types(self):
        values = [1, "apple", True]
        sets = [2.5, None, False]
        expected_result = [1, 2.5, "apple", None, True, False]
        self.assertEqual(array_tasks.merge_alternating(values, sets), expected_result)

    def test_extract_digits_positive_integer(self):
        number = 12345
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(array_tasks.extract_digits(number), expected_result)

    def test_extract_digits_negative_integer(self):
        number = -6789
        expected_result = [6, 7, 8, 9]  
        self.assertEqual(array_tasks.extract_digits(number), expected_result)

    def test_extract_digits_zero(self):
        number = 0
        expected_result = [0]
        self.assertEqual(array_tasks.extract_digits(number), expected_result)

    def test_extract_digits_single_digit(self):
        number = 5
        expected_result = [5]
        self.assertEqual(array_tasks.extract_digits(number), expected_result)

    def test_extract_digits_large_number(self):
        number = 9876543210
        expected_result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(array_tasks.extract_digits(number), expected_result)




































