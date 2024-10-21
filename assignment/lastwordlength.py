def last_word_length(user_input):
    user_input = user_input.strip()
        
    last_space_index = user_input.rfind(' ')
        
    return len(user_input) - 1 - last_space_kindex


user_input = "Hello World   "
print("The index of the last word is ", last_word_length(user_input))