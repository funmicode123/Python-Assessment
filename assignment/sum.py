total = 0
counter = 1

while counter <= 10:
	score = int(input("Enter the score: "))
	total += score
	counter += 1

print(f"The sum of the score is ", total)