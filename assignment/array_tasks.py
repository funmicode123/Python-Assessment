def largest_number(values):
    if len(values) == 0:
        raise ValueError("The list is empty")
   
    return max(values)

def reverse_list(values):
    return values[::-1]

def is_element_present(values, element):
    return element in values  

def print_odd_position_elements(values):
    for index in range(1, len(values), 2):
        print(values[index], end=' ')
    print()

def print_even_position_elements(values):
    for index in range(0, len(values), 2):
        print(values[index], end=' ')
    print()

def compute_total(values):
    total = 0
    for index in range(len(values)): 
        total += values[index]
    return total

def is_string_palindrome(string_element):
    return string_element == string_element[::-1]

def compute_sum_while(values):
    total, index = 0, 0
    while index < len(values):  
        total += values[index]
        index += 1
    return total

def compute_sum_do(values):
    total, index = 0, 0
    if len(values) == 0:
        return total
    while True:
        total += values[index]
        index += 1
        if index >= len(values):
            break
    return total

def concatenate_sets(values, sets):
    return [values + sets]

def merge_alternating(values, sets):
    merged_list = []
    min_length = min(len(values), len(sets))
    for index in range (min_length):          
        merged_list.append((values[index]))         
        merged_list.append(sets[index]) 

    if len(values) > len(sets):
        merged_list.extend(values[min_length:])
    elif len(sets) > len(values):
        merged_list.extend(sets[min_length:])
   
    return merged_list

def extract_digits(number):
    return [int(digit) for digit in str(abs(number))]


values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
number = 23456


print(values)

largest = largest_number(values)
print(f"Largest number: {largest}")

reversed_values = reverse_list(values)
print(f"Reversed array: {reversed_values}")

element_to_find = 30
is_present = is_element_present(values, element_to_find)
print(f"Is {element_to_find} present?: {is_present}")

print("Elements at odd positions: ", end="")
print_odd_position_elements(values)

print("Elements at even positions: ", end="")
print_even_position_elements(values)

list_total = compute_total(values)
print(f"The total of numbers in the list: {list_total}")

string_element = str(values[5])
print(f"Is {string_element} a palindrome?: {is_string_palindrome(string_element)}")

list_sum_while = compute_sum_while(values)
print(f"The sum of numbers in the list using a while loop: {list_sum_while}")

list_sum_do = compute_sum_do(values)
print(f"The sum of numbers in the list using a do-while loop: {list_sum_do}")

merged_result = concatenate_sets(values, sets)
print(f"The concatenated list: {merged_result}")

merged_list = merge_alternating(values, sets)
print(f"The alternating merged list: {merged_list}")

digits = extract_digits(number)
print(f"Digits of {number}: {digits}")
