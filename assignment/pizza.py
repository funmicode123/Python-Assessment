def return_price(pizza_category):
    prices = {
        1: 2000,
        2: 2400,
        3: 3000,
        4: 4200
    }
    return prices.get(pizza_category, 0)

def number_of_slices(pizza_category):
    slices = {
        1: 4,
        2: 6,
        3: 8,
        4: 12
    }
    return slices.get(pizza_category, 0)

def pizza_name(pizza_category):
    name = {
        1: "Sapa",
        2: "Small Money",
        3: "Big boys",
        4: "Odogwu"
    }
    return name.get(pizza_category, "unknown")

def number_of_pizza_boxes(guest_number, slices_per_box):
    return (guest_number + slices_per_box - 1) // slices_per_box

def left_over(boxes_needed, slices_per_box, guest_number):
    return boxes_needed * slices_per_box - guest_number

def customer_price(boxes_needed, price_per_box):
    return boxes_needed * price_per_box


customer_name = input("Please, enter your name: ")
print(f"Welcome {customer_name}, to Iya Afeez Pizza joint, Ajegunle")

guest_number = int(input("Enter number of guests: "))

pizza_category_menu = """ 
Pizza type  Name	 Number Of Slices        Price Per Box
----------------------------------------------------------------
1           Sapa	    4                        2000
2           Small Money	    6                        2400
3           Big boys	    8                        3000
4      	    odogwu	    12                       4200
"""

print("Pizza Category: ")
print(pizza_category_menu)

pizza_category = int(input("Enter the Pizza category (1-4): "))
if pizza_category < 1 or pizza_category > 4:
    print("Invalid pizza category.")
else:
    price_per_box = return_price(pizza_category)
    slices_per_box = number_of_slices(pizza_category)

    boxes_needed = number_of_pizza_boxes(guest_number, slices_per_box)
    print(f"Number of boxes of Pizza to buy: {boxes_needed}")

    left_over_slices = left_over(boxes_needed, slices_per_box, guest_number)
    print(f"Number of leftover slices: {left_over_slices} slices")

    total_price = customer_price(boxes_needed, price_per_box)
    print(f"Cost of the Pizza: {total_price}")
