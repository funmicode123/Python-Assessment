def reverse(number):
	reverse = 0
	return str(number)[:: -1]
	

def is_number_palindrome(number):
    if number == int(reverse(number)):
        return True
    else:
        return False

number = 454

print(reverse(number)) 

print(is_number_palindrome(number))