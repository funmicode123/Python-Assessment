def credit_card(account_number, new_balance, credit_limit):
	if (new_balance > credit_limit):
	    print("Account {account_number:} Credit limit is exceeded")
	else:
	    print("Account {account_number:} Within credit limit ")

account_number = int(input("The new account number is: "))
		
balance = float(input("The balance at the beginning of the month is: "))

total_charges = float(input("The total charges is: "))

total_credit = float(input("The total credit: "))

credit_limit = float(input("The credit limit: "))
	
new_balance =float( balance + total_charges - total_credit)

print(f"The new balance is {new_balance:.2f} "  )

credit_card(account_number, new_balance, credit_limit)

