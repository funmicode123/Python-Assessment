"""
1. Collect float input from user and save variable as price
2. Collect float input from user and save variable as discount
3. Convert discount_percentage, discount / 100
4. Calculation, discounted_price = price - (price * discount_percentage)
5. display Discounted_price
"""


def get_my_discount(price, discount):
    PERCENTAGE =100
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
       raise TypeError("All input values must be numbers")
    if price < 0 or discount < 0:
        raise ValueError("Price of a product and discount cannot be negative")
    discount = discount / PERCENTAGE
    discounted_price = price - (price * discount)
    return discounted_price


price = float(input("Enter the product price: "))
discount = float(input("Enter the discount: "))

discounted_price = get_my_discount(price, discount)
print(f"My discounted price for the product is {discounted_price:.2f}")
