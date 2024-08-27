"""
score = int(input("Enter score: "))

result = ""

if score >= 40:

	result = "passed"
	print ("really ", result)

if score < 40:

	result = "failed"
	print ("really ", result)
"""
	
"""
prompt user to enter a variable
save the variable as a name
declare an empty variable
save the variable as blank
compare the two variables,
if it's equal
display the name
if the variable is not equal
display the error message
"""
"""
name = input("Enter your name: ")
blank = ""
if name != blank:
	print("Hi, ", name)

else:
	print("Sorry you have entered an invalid name") 
"""

"""
score = int(input("Enter score: "))

if score > 100:
	print("Invalid score")
elif score >= 75 and  score <= 100:
	print("Your grade is A")
elif score  >= 65 and score < 74:
	print("Your grade is B")
elif score  >= 50 and score <= 64:
	print("Your grade is C")
elif score  >= 40 and score <= 49:
	print("Your grade is D")

else:
	print("failed")
"""

language = input("Enter preferred language: ")

match language:
	case "java":
		print("Chibuzor and jennifer")
	case "python":
		print("Mr Sikiru")
	case "javascript":
		print("Mr Peter")
	case _:
		print("It executes this when there's no valid case")













