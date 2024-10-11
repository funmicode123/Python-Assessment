total = 0;
counter = 1;

while (counter <= 10):
	score = int(input("Enter the score: "))
	if score % 2 == 0:
		total += score
	counter += 1
	
print(f"The sum of the even score value is ", total)