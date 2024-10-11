number = 50
if number < 0:
    print("Negative number is invalid")

for index in range(1, number + 1):
    if index % 15 == 0:
        print("fizzbuzz")
    elif index % 3 == 0:
        print("fizz")
    elif index % 5 == 0:
        print("buzz")
    else:
        print(index)


