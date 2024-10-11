def future_investment(capital, no_of_years, rate):
    if capital < 0:
        return "Negative value is invalid"

    if no_of_years < 0:
        return "Negative value is invalid"

    year = 1
    print("years\tinterest\tfuture_yield")
    while year <= no_of_years:
        interest = capital * rate
        capital += interest
        print(f"{year}\t{interest:.2f}\t{capital:.2f}")
        year += 1
    return capital

capital = int(input("Enter the principal amount: "))
no_of_years = int(input("Enter the number of years to invest: "))
rate = int(input("Percentage rate: "))
rate = rate / 100



final_amount = future_investment(capital, no_of_years, rate)
print(f"Final amount after {no_of_years} years: {final_amount:.2f}")
