def divisible_7(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer value")
    if number < 0:
        raise ValueError("Invalid number")
    if number % 7 != 0:
        result = False
        return result
    else:
        return True



def multiple_3(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer value")
    if number < 0:
        raise ValueError("Invalid number")
    if number % 3 != 0:
        
        return "Bye"
    else:
        return "Hello"

number =int(input("Input the number: "))

print(divisible_7(number))
print(multiple_3(number))