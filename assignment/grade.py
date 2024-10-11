total = 0
counter = 0

grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
	total += grade
	counter += 1

average = total / counter
print(f'class average is {average}')
print()


for count in range(2):
	value = int(input('Enter integer: '))
	if value % 2 == 0:
		print(f'{value} is an even number')

	else:
		print(f'{value} is an odd number')
		
print()
for count in range(5, 10):
	print(count, end=' ')
	
print()
for number in range(0, 10, 2):
	print(number, end=' ')
	
print()
for number in range(10, 0, -2):
	print(number, end=' ')
	

