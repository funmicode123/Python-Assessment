def compareNumbers(number1, number2):
    if number1 == number2:
       return 0 
    elif number1 > number2:
       return 1
    else:
       return -1

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = compareNumbers(number1, number2)
print(f"Result is: {result}")

        
