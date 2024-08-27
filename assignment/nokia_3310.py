print("Welcome to your Nokia phone");

menu  =	"""
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminder
11. Clock
12. Profiles
13. SIM services
"""
menu_option = int(input(menu))

match (menu_option):
	case 1: print("phone book")
phone_book = """
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags """

phone_book = int(input(phone_book))

match (phone_book):
	case 1: 
		print("Search")
	case 2: 
		print("Service Nos")
	case 3: 
		print("Add name")
	case 4: 
		print("Erase")
	case 5: 
		print("Edit")
	case 6: 
		print("Assign tone")
	case 7: 
		print("Send b'card")
	case 8: 
		print("Options")
options = """
1. Type of view
2. Memory status """

print ("Options", options)
options = int(input("select an option (1-2): "))

match (options):
	case 1: 
		print("Type of view")
	case 2: 
		print("Memory status")	
	case 9: 
		print("Speed dials")
	case 10: 
		print("Voice tags")














