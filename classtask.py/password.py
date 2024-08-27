"""
prompt user to enter the second input
save the input as password
count the number of words inputed
display the password in astericks
"""

password = input("Sample input: ")
length = len(password)
password = '*' * length
print("Sample output: ", password)