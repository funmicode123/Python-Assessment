numbers = 5


for index in range(1, numbers + 1):
    line = ""
    for count in range(1, index + 1):
        if count % 2 != 0:
            print(count, end=" ")
        else:
            print("*", end=" ")
    print()
        

for index in range(numbers, 0, -1):
    for count in range(1, index + 1):
        if count % 2 != 0:
            print(count, end=" ")
        else:
            print("*", end=" ")
    print()



