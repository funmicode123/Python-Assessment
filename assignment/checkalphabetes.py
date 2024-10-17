import string

LETTER = string.ascii_lowercase
sentence = "The quick brown fox jumps over the lazy dog%^*8".lower()
count = 0
letters = [word for word in LETTER]

for letter in LETTER:
    if letter in sentence:
        count += 1

if count == 26:
    print(True)

else:
    print(False)




