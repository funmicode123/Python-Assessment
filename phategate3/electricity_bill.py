try:
    bill_unit = int(input("Enter the bill unit: "))

    if bill_unit < 0:
        print("Invalid unit number")

    elif bill_unit <= 100:
        amount_to_pay = 0
        print(f"No charge")
    elif bill_unit <= 200:
        charges = 50
        amount_to_pay = (bill_unit - 100) * charges
        print(f"{amount_to_pay:.2f}")
    else:
        charges = 100
        amount_to_pay = (200 - 100) * 50 + (bill_unit -200) * charges
        print(f"{amount_to_pay:.2f}")

except ValueError:
    print("Invalid input! please enter a numeric value")



