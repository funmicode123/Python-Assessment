def print_even_number():
    for index in range(1000, 3001, 2):
        if index < 3000:  
            print(index, end=', ')
        else:
            print(index)  

print_even_number()
