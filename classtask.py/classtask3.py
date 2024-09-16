"""
miles = 175
kilometers = 1.609 * miles
print("The kilometer is ", kilometers)
"""

"""
1. collect the budget value from the user
2. save in a variable named budget
3. price per litre is #855
4. calculate the litres to be bought, budget / 855
5. display the result
"""



budget = int(input("Enter your budget: #"))
PRICE_PER_LITRE = 855

litres_to_be_bought = budget / PRICE_PER_LITRE
print(f"Your budget will covers {litres_to_be_bought:.2f} litres")
