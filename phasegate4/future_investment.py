year = 1
capital = float(input("Enter the principal amount: "))
no_of_year = float(input("Enter the investment year: "))
rate = int(input("percentage rate: "))
rate = rate / 100

if capital < 0:
    print("Negative value is invalid")

print("year\tinterest\tcapital")
while year <= no_of_year:
    interest = capital * rate
    capital += interest
    print(f"{year}\t{interest:,.2f}\t{capital:,.2f}")
    year += 1

