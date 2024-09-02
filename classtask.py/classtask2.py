"""
Prompt user to enter a variable
save as deposit
Get balance by adding the deposits together
Prompt user to enter a variable
save as withdraw
Sum the deposits
Save as total
Check the difference by minus


deposit = float(input("Enter deposit amount: "))
balance = 0
total = 0
deposit_counter = 0

while deposit != -1:
	balance += deposit
	deposit = float(input("Enter deposit amount: "))
	deposit_counter+=1

if deposit == -1:
	withdraw = float(input("Enter withdraw amount: "))
	total = balance - withdraw
	print(f"The balance is {total}")

"""

menu = print('''
-> 1. Deposit
-> 2. Withdraw
-> 3. Balance
-> 0. Back
''')
balance = 0

option = input ('Select an option: ')

while option != 0:
	if option == '1':
		deposit = float(input("Enter deposit amount: "))
		balance += deposit
		option = input (menu)
	elif option == '2':
		withdraw  = float(input("Enter withdraw amount: "))
		if withdraw <= balance:
			balance -= withdraw
			option = input (menu)
			
		else:
			print("Insufficient balance")
			option = input (menu)
	elif option == '3':
		print("Your balance is ", balance)
		option = input (menu)
		break

print("Thanks for banking with us")