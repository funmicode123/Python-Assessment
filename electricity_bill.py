bill_unit = int(input("Enter the bill unit: "))

if bill_unit < 0:
    print("Invalid unit number")

if bill_unit > 0 and bill_unit <= 100:
    print("No charge")
elif bill_unit > 100 and bill_unit <= 200:
    charges = 50
    print(f"{charges * bill_unit:.2f}")
else:
    charges = 100

    print(f"{charges * bill_unit:.2f}")