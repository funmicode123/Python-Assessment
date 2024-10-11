number = 6
factorial = 1

if number < 0:
    print("Negative number is not valid")


for index in range(1, number, 1):
    factorial *= index
    print(factorial)