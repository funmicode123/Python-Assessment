numbers = 5

for number in range(numbers):
    line = ""
    for count in range(number + 1):
        line += str(2 * count + 1)
        if count != number:
            line+= " * "
    print(line)




   