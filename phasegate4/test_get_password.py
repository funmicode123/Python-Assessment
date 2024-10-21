import unittest
import string
from get_password import get_password  

class TestGetPassword(unittest.TestCase):

    def test_that_get_password_function_contain_uppercase(self):
        uppercase = string.ascii_uppercase
        password = get_password()
        self.assertTrue(any(char in uppercase for char in password))

    def test_that_get_password_function_contain_lowercase(self):
        lowercase = string.ascii_lowercase
        password = get_password()  
        self.assertTrue(any(char in lowercase for char in password))

    def test_that_get_password_function_contain_symbols(self):
        symbols = string.punctuation
        password = get_password()
        self.assertTrue(any(char in symbols for char in password))

    def test_that_get_password_function_contain_digits(self):
        digits = string.digits
        password = get_password()
        self.assertTrue(any(char in digits for char in password))

    def test_that_get_password_function_exist(self):
        get_password()
