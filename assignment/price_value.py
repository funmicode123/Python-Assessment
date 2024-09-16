"""
1. Collect float input from user and save variable as price
2. Collect float input from user and save variable as discount
3. Convert discount_percentage, discount / 100
4. Calculation,result = price * discount_perceentage
5. Discounted_price = price - result
6. display Discounted_price
"""


def get_my_discount(price, discount):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
       raise TypeError("All input values must be numbers")
    if price < 0 or discount < 0:
        raise ValueError("price of a product and discount cannot be negative")
    discount = discount / PERCENTAGE
    result = price * discount
    discounted_price = price - result
    return discounted_price


price = float(input("Enter the product price: "))
discount = float(input("Enter the discount: "))
PERCENTAGE =100

discount = discount / PERCENTAGE
result = price * discount
discounted_price = price - result
print(f"My discount for the product is {discounted_price:.2f}")
