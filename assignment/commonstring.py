def longest_common_prefix(user_input):
    if not user_input:
        return ""

    prefix = user_input[0]

    for string in user_input[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]  
            if not prefix:
                return ""

    return prefix

user_input = ["closet", "closes", "closure"]
input = ["dog", "racecar", "car"]
print("Logest common prefix: ", longest_common_prefix(user_input))
print("There's no common prefix.", longest_common_prefix(input))