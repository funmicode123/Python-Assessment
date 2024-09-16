def getNumber(uppercase_letter):
    match uppercase_letter:
        case 'A' | 'B' | 'C':
            return 2
        case 'D' | 'E' | 'F':
            return 3
        case 'G' | 'H' | 'I':
            return 4
        case 'J' | 'K' | 'L':
            return 5
        case 'M' | 'N' | 'O':
            return 6
        case 'P' | 'Q' | 'R' | 'S':
            return 7
        case 'T' | 'U' | 'V':
            return 8
        case 'W' | 'X' | 'Y' | 'Z':
            return 9
        case _:
            return -1


string_input = input("Enter a string: ").upper()  

for letter in string_input:
    if letter.isalpha():  
        print(getNumber(letter), end='')  
    else:
        print(letter, end='')  

print()  