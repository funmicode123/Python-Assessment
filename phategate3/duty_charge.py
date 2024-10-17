try:
    cost_of_car = int(input("Enter the cost of the car: "))

    if cost_of_car < 0:
        print("Please input a valid amount")

    elif cost_of_car >= 10000000:
        duty_charge = cost_of_car * 0.2
    elif cost_of_car >= 5000000:
        duty_charge = cost_of_car * 0.15
    elif cost_of_car >= 2500000:
        duty_charge = cost_of_car * 0.10
    else:
        duty_charge = cost_of_car * 0.05

    print(f"Duty charge: {duty_charge:.2f}")

except ValueError:
    print("Please enter a numeric value")
