def get_prime(number):
    if number <= 1:
        return False
    count = 0
    for counter in range(1, number + 1):
        if number % counter == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def get_palindrome(number):
    number_to_string = str(number)
    reversed_str = number_to_string[::-1]  
    return number_to_string == reversed_str

number =int(input("enter the number "))

def get_palindromic_prime(number)
    number = 2
    found = 0
    lineCount = 0
    while found < count:
        if getPrime(number) and getPalindrome(number):
            print(number, end=" ")
            found += 1
            lineCount += 1

            if lineCount % 10 == 0: 
                println()
                    
        number += 1



number =int(input("Enter the number of palindromic prime to find: "))
get_palindromic_prime(number)