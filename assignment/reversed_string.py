def reverse_string(array_string, ends_with_period):
    reverse_string = ""
    for index in range(len(array_string)):
        reverse_string = array_string[index] + " " + reverse_string
    reversed_string = reverse_string.strip()
    
    if ends_with_period:
        reversed_string += "."
    
    return reversed_string

def check_full_stop(original_string):
    return original_string.endswith(".")

example = "There is a tide in the affairs of men"
array_string = example.split(" ")

ends_with_period = check_full_stop(example)

reversed_sentence = reverse_string(array_string, ends_with_period)

full_stop_check = check_full_stop(reversed_sentence)

print("Reversed sentence is:", reversed_sentence)

print("Ends with a full stop:", full_stop_check)