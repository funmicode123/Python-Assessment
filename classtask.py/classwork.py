"""
def double_number(number1, number2):

	merge_number = f"{number1}{number2}"

	return int(merge_number[::-1])
	


print (double_number(1, 2))
"""
"""
number1 = 1
number2 = 2
number1, number2 = number2, number1
print(number1, number2, sep=' , ')
"""

def reversed_string(name):
	reverse_word = ''
	for number in range(len(name) -1, -1, -1):
		reverse_word += name[number]
		
	return reverse_word
print(reversed_string("funmilola"))


def palindrome(number):
	return str(number) == reversed_string(str(number))

print(palindrome("2112"))
print(palindrome("hannah"))


def even_odd(number)
	for number in range(1,1000, 1)
	return palindrome("number") 


