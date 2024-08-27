principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
duration = int(input("Enter the duration in years: "))
PERCENTAGE = 100
MONTHS = 12


monthly_rate = (rate/PERCENTAGE) / MONTHS
no_of_months = duration * MONTHS
	

mortagage_result = float(principal * (monthly_rate * (1 + monthly_rate) ** no_of_months) / ((1 + monthly_rate) ** no_of_months - 1))


print(f"Your monthly payment is {mortagage_result:.2f}")