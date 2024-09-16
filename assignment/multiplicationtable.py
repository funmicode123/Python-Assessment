"""

multiplication_number = int(input("times number: ")) 
number_times = int(input("number times: ")) 

for number in range (1,number_times,1):
	print(multiplication_number, "*", number, "=", multiplication_number * number)
"""

def print_multiplication(number):
    for count in range(1, 13):  
        for counter in range(1, number + 1):  
            print(f"{counter} * {count} = {counter * count:>4}", end='\t')  
        print()  