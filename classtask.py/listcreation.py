"""
1. keep requesting numbers from user using iteration
2. stop the iteration when user enter -1
3. Save the numbers collected in a variable as list
4. print the list
5. Add the elements in the list 
6. Save in a variable as total
7. Divide total by number of element in a list
8. Save the result as average
9. Display the average
""" 
def compute_average(list):
    if len(numbers) == 0:
        return 0
    total = 0
    average = 0
    for index in numbers:
        total += index
        average = total / len(numbers)
    return average

numbers = []
number = 0

while number != -1:
	number = int(input("Enter the numbers, -1 to stop: "))

	if number != -1:
		numbers += [number]
print(numbers)

average = compute_average(numbers)
print(f"Average: {average:.2f}")


