import random

failed = 0
passed = 0

for count in range(10):
    random1 = random.randrange(1, 10)
    random2 = random.randrange(1, 10)
    print(random1, random2)
    if random1 < random2:
        result = random2 - random1
    elif random2 < random1:
        result = random1 - random2
    else:
        result = 0  # In case both numbers are equal
    
    answer = int(input("Result: "))
    if result == answer:
        passed += 1
    else:
        failed += 1

print("Failed:", failed)
print("Passed:", passed)
