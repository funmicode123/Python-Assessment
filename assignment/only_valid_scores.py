total = 0
count = 0
counter = 0
while (counter < 10):
	score = int(input("Enter the score: "))
	counter += 1
	if score > 0 and score < 100:
		total += score
		count +=1
		
print(f"The sum of valid number from 10 entries is {total}")
	
	
	
