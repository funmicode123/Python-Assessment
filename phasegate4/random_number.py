import random

random1 = random.randrange(1, 100)
random2 = random.randrange(1, 100)


guess = int(input("what's the sum of the guess number: "))

correct_guess = random1 + random2

if correct_guess == guess:
    print("True")
else:
    print("False")