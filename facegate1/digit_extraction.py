number = int(input("The integer number: "))

if (number < 0):
    print("Negative integers are invalid")
       

if (number >= 0):
    digit1 = number % 10
    number = number // 10
    digit2= number % 10
    number = number // 10
    digit3 = number % 10
    number = number //10

sum = digit1 + digit2 + digit3

print("Sum ", sum)