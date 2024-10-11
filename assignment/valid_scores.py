total = 0
count = 0
	
while (count < 10):
	score = int(input("Enter the score: "))
	if score > 0 and score < 100:
		total += score
		count +=1
		
print(f"The sum of valid 10 scores is {total}")
	
	
	
