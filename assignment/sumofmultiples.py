def sum_multiple(start, end, multiple):
	total = 0
	for number in range(start, end, multiple):
		if number % multiple == 0:
			total += number
	return total

print(sum_multiple(0, 200, 10))