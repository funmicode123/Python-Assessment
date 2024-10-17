number = int(input("The integer number: "))

if (number < 0):
    print("Negative integers are invalid")
    exit()

else:

    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number = number // 10

print("Sum of the digits: ", sum_digits)