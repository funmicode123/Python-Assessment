def list_is_empty(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty")
   
def len_function(numbers):
    counter = 0
    for _ in numbers:
        counter += 1
    return counter


def sum_odd_positions(numbers):
    result = 0
    for index in range(1, len(numbers), 2):
        result += numbers[index]
        print(result, end=' ')
    print()

def sum_even_positions(numbers):
    result = 0
    for index in range(0, len(numbers), 2):
        result += numbers[index]
        print(result, end=' ')
    print()

def multiply_every_third_positions(numbers):
    result = 1
    for index in range(0, len(numbers), 3):
        result *= numbers[index]
        print(result, end=' ')
    print()


def calculate_average(numbers):
    total = 0
    average = 0
    for index in range(len(numbers)):
        total += numbers[index]
    average = total / len_function(numbers)
		
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


print(numbers)


print("Sum at odd positions: ", end="")
sum_odd_positions(numbers)

print("Sum at even positions: ", end="")
sum_even_positions(numbers)

print("Multiplication at 3rd positions: ")
multiply_every_third_positions(numbers)

average = calculate_average(numbers)
print(f"The average of numbers in the list: {average}")


