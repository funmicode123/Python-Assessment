import unittest
import future_investment

class TestFutureInvestment(unittest.TestCase):

    def test_that_future_investment_exists(self):
        investment_amount = 1000
        monthly_interest_rate = (250 / 100) / 12
        years = 1
        self.assertIsNotNone(future_investment.get_future_investment(investment_amount, monthly_interest_rate, years))

    def test_that_future_investment_function_returns_future_investment(self):
        investment_amount = 1000
        monthly_interest_rate = (250 / 100) / 12
        years = 1
        number_of_months = years * 12
        expected_future_investment = investment_amount * (1 + monthly_interest_rate) ** number_of_months
        self.assertEqual(future_investment.get_future_investment(investment_amount, monthly_interest_rate, years), expected_future_investment)

    def test_that_future_investment_function_raises_error_with_negative_amount(self):
        investment_amount = -1000
        monthly_interest_rate = (250 / 100) / 12
        years = 1
        self.assertRaises(ValueError, future_investment.get_future_investment, investment_amount, monthly_interest_rate, years)

    def test_that_future_investment_function_raises_error_with_string_value(self):
        investment_amount = "invalid"
        monthly_interest_rate = (250 / 100) / 12
        years = 1
        self.assertRaises(TypeError, future_investment.get_future_investment, investment_amount, monthly_interest_rate, years)
