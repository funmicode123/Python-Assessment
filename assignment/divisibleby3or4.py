lineCounter = 0

for number in range(100, 200, 1):
    if number % 3 == 0 or number % 4 == 0:
        print(number, end=" ")
        lineCounter += 1 
        if lineCounter == 10:
            print() 
            lineCounter = 0
