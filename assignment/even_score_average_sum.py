total = 0
count = 0
counter = 1

while (counter <= 10):
	score = int(input("Enter the score: "))
	counter += 1
	if score % 2 == 0:
		total += score
	
		count += 1

if count > 0:
	average = total / count
print(f"The sum of the even score value is ", total)
print(f"The average of the even score is {average:.2f}")