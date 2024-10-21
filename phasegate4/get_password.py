import random
import string

def get_password(length=16):
    if length < 16:
        raise ValueError("Password length must be at least 16.")


    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

   
    output_characters = uppercase + lowercase + numbers + symbols
    password+= random.choices(output_characters, k=length )

  
    random.shuffle(password)

    return "".join(password)

print(get_password())












  
    