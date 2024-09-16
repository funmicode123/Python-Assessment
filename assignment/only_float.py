"""
1. Collect input from user
2. Save variable as number1
3. Collect input from user
4. Save variable as number2
5. Check if the input is string
5a. Check if the string contain decimal point, convert to float if has a dot
5b. Else return the value as int
6. Else return value if its float or int already
7. Check if number1 and number2 is float
8. If true return 2
9. Check if number1 or number2 is float
10. if true return 1
11. Check if neither number1 and number2 is float
12. if true return 0
"""
def check_for_float(value):
    if isinstance(value, str):
        if '.' in value:
            try:
               return float(value)
            except ValueError:
               raise ValueError(f"Invalid input: {value}")

        else:
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Invalid input: {value}")
    else:
        return value

def get_both_float(number1, number2):
    if isinstance(number1, float) and isinstance(number2, float):
       return 2

def get_one_float(number1, number2):
    if isinstance(number1, float) or isinstance(number2, float):
       return 1

def get_none_float(number1, number2):
    if not isinstance(number1, float) and not isinstance(number2, float):
       return 0


number1 = input("Enter first input: ")
number2 = input("Enter second input: ")

number1 = check_for_float(number1)
number2 = check_for_float(number2)

if get_both_float(number1, number2):
    print("Both numbers are floats: ", get_both_float(number1, number2))

elif get_one_float(number1, number2):
    print("One of the numbers is float: ", get_one_float(number1, number2))

else:
    print("None of the numbers are float: ", get_none_float(number1, number2))