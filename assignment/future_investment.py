def get_future_investment(investment_amount, monthly_interest_rate, years):
     if not isinstance(investment_amount, (int, float)) or not isinstance(monthly_interest_rate, (int, float)) or not isinstance(years, (int, float)):
        raise TypeError("All input values must be numbers")
     if investment_amount < 0 or years < 0:
        raise ValueError("Investment amount and years cannot be negative")
     number_of_months = years * MONTHS_PER_YEAR
     
     future_investment = investment_amount * (1 + monthly_interest_rate)**  number_of_months
     return future_investment

investment_amount = float(input("Enter the capital amount: "))
rate = float(input("Enter the annual interest rate(%): "))
years = int(input("Enter the number of years to calculate: "))
PERCENTAGE = 100
MONTHS_PER_YEAR = 12
monthly_interest_rate = (rate/PERCENTAGE) / MONTHS_PER_YEAR

future_investment = get_future_investment(investment_amount, monthly_interest_rate, years)
print(f"The future investment value is: {future_investment:.2f}")


