def sort_squared_numbers(numbers):
    squared_numbers = [num ** 2 for num in numbers]


    for count in range(len(squared_numbers) - 1):
        swapped = False
        for index in range(len(squared_numbers) - count - 1):
            if squared_numbers[index] > squared_numbers[index + 1]:
                squared_numbers[index], squared_numbers[index + 1] = squared_numbers[index + 1], squared_numbers[index]
                swapped = True
        if not swapped:
            break

    return squared_numbers


def main():
    numbers = [2, 1, 4, 3, 5, 9]
    sorted_squares = sort_squared_numbers(numbers)

    print("Squared numbers in ascending order: [", end="")
    for index, num in enumerate(sorted_squares):
        print(f"{num}{',' if index < len(sorted_squares) - 1 else ']'}", end=" ")
    print()


