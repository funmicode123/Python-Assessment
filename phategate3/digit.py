number = int(input("Enter the number: "))
if number < 0:
    print("Invalid  number")
else:
    digit = number % 10
    print("Last digit is ", digit)