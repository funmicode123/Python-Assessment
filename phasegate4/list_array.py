rows = int(input("Row: "))
columns = int(input("Column: "))

if rows < 0 and columns < 0:
    print("Negative number is invalid")
else:
    numbers = [[index * count for count in range (columns)] for index in range(rows)]
    for row in numbers:
        print(row)








