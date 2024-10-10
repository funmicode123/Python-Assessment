characters = "iaoi"
vowels = "aeiou"


def vowel_consonant_check(characters):
    for character in characters:
        if character in vowels:
            return True
        elif character in consonants:
            return False
        else:
            return f"{char} is neither a vowel nor a consonant"

print(vowel_consonant_check(characters))