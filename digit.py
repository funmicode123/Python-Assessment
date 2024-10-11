number = int(input("Enter the number: "))
if number < 0:
    ValueError("Invalid  number")
else:
    digit = number % 10
    print("Last digit is ", digit)