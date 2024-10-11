
for counter in range(6, 0, -1):
    row = ''
    for space in range(counter - 1):
        row += " "
    for inner in range(6 - counter + 1):
        row += "* "
    print(row)


for counter in range(6, 0, -1):
    row = ''
    for space in range(6 - counter):
        row += " "
    for inner in range(counter):
        row += "* "
    print(row)
