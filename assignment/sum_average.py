total = 0
counter = 1

while (counter <= 10):
	score = int(input("Enter the score: "))
	total += score
	counter += 1
	
	average = total / 10
print(f"The sum of the score is ", total)
print(f"The average score is {average:.2f}")