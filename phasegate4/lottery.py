import random

lottery = [random.randint(1, 100) for _ in range(3)]
print(f"Lottery numbers are: {lottery}")  

user_input = input("Enter your guess numbers separated by spaces (e.g., 31 15 61): ")

user_input_list = [int(num) for num in user_input.split()]

def count_correct_in_order(lottery, user_input):
    count = 0
    for index in range(len(lottery)):
        if lottery[index] == user_input[index]:
            count += 1 
    return count

def count_correct_not_in_order(lottery, user_input):
    count = 0
    for element in lottery:  
        if element in user_input:  
            count += 1
    return count

if user_input_list == lottery:
    print("You won $5,000")

elif sorted(user_input_list) == sorted(lottery):
    print("You won $4,000")

else:
    correct_in_order = count_correct_in_order(lottery, user_input_list)
    correct_not_in_order = count_correct_not_in_order(lottery, user_input_list)

    if correct_in_order == 2:
        print("You won $3,000")

    elif correct_not_in_order == 2:
        print("You won $2,000")

    else:
        print("Better luck next time!")
