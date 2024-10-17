numbers = [10,3,6,5,1,8,2,4,7,9]
letters = 'ghiyzracdbjlxeknomrqpustwv'
numbers = sorted(numbers)
letters = sorted(letters)
descending_numbers = numbers.sort(reverse=True)
descending_letters = letters.sort(reverse=True)

numbers.extend(letters)


print(descending_numbers)
print(numbers)

numbers_list = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = []
for number in numbers_list:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
