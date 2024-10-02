def find_product(number1, number2):
	product = 0

	if number1 ==0 or number2 == 0:
		return 0


	if number1 < 0 and number2 < 0:
		number1 = - number1
		number2 = -number2

	elif number1 < 0:
		return -find_product(-number1, number2)

	elif number2 < 0:
		return -find_product(number1, -number2)


	for number in range(number1):
		product += number2

	return product


number1 = int(input("The first number : "))
number2 = int(input("The second number : "))

result = find_product(number1, number2)
print(f"Result: {result}")
