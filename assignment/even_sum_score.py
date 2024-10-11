total = 0;
counter = 1;

while (counter <= 10):
	score = int(input("Enter the score: "))
	if counter % 2 == 0:
		total += score
	counter += 1
	
print(f"The sum of the even index score is ", total)