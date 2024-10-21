def multiply_third_position_elements(numbers):
    product = 1
    for index in range(2, len(numbers), 3):
        print(numbers[index] , end=' ')
        product *= numbers[index]
    print()
    return product

def square_each_element(numbers):
    square_element = []
    for index in range(len(numbers)):
        square_element.append(numbers[index] * numbers[index])
    return square_element

def is_ascending(numbers):
    for index in range(len(numbers) - 1): 
        for count in range(len(numbers) - 1 - index): 
            if numbers[count] > numbers[count + 1]: 
                temp = numbers[count]
                numbers[count] = numbers[count + 1]
                numbers[count + 1] = temp
    
    return numbers == sorted(numbers)

def is_descending(numbers):
    for index in range(len(numbers) - 1):
        for count in range(len(numbers) -1 - index):
            if numbers[count] < numbers[count + 1]: 
                temp = numbers[count]
                numbers[count] = numbers[count + 1]
                numbers[count + 1] = temp
    
    return numbers == sorted(numbers, reverse=True)



numbers = [5, 2, 7, 1, 8, 2]

print("Original list:", numbers)
result = multiply_third_position_elements(numbers)
print("The product of the third element is ", result)

squared_element = square_each_element(numbers)
print("The squared elements: ", squared_element)

is_ascending(numbers) 
print("Ascending order:", numbers) 

is_descending(numbers) 
print("Descending order:", numbers) 


