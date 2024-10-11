def is_armstrong(number):
    digits = str(number)
    number_digits = len(digits)
    sum_of_powers = 0  

    for digit in digits:  
        sum_of_powers += int(digit) ** number_digits  
    return sum_of_powers == number

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
