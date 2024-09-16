"""
PSEUDOCODE

1. Collect input from the user 
2. Save variable as number
3. To calculate, if number % 5 = 0
4. Return math.sqrt(number)
5. Else(if number%5 != 0), return number % 5
"""
import math

def get_divide(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer value")
    if number < 0:
        raise ValueError("Invalid number")
    if number % 5 != 0:
        result = number % 5
        return result
    else:
        return "Number is divisible by 5, no remainder."


def get_square(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer value")
    if number < 0:
        raise ValueError("Invalid number")
    if number % 5 == 0:
        result = math.sqrt(number)
        return result
    else:
        return "Number is not divisible by 5, no square root calculation."


number = int(input("Enter the integer: "))

if number % 5 == 0:
    print(f"The square root of the number is {get_square(number):.3}")
else:
    print("The remainder when divided by 5 is", get_divide(number))
