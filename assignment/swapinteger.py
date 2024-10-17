def number_sort(numbers):
    for index in range(0, len(numbers) - 1, 2):
        temp = numbers[index]
        numbers[index] = numbers[index + 1]
        numbers[index + 1] = temp
    return numbers


numbers = [1, 2, 3, 4, 5, 6]
result = number_sort(numbers)
print("Output:", result)
