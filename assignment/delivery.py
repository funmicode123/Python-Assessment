rate_for_less_50 = 160
rate_for_50_to_59 = 200
rate_for_60_to_69 = 250
rate_for_above_70 = 500
BASE_PAY = 5000


def calculate_wages(successful_deliveries):
    if successful_deliveries < 50:
        rate = (successful_deliveries * rate_for_less_50) + BASE_PAY
    elif successful_deliveries >= 50 and successful_deliveries < 60:
        rate = (successful_deliveries * rate_for_50_to_59) + BASE_PAY
    elif successful_deliveries >= 60 and successful_deliveries < 70:
        rate = (successful_deliveries * rate_for_60_to_69) + BASE_PAY
    else:
        rate = (successful_deliveries * rate_for_above_70) + BASE_PAY
    
    return rate

successful_delivery = int(input("Enter amount of successful delivery: "))
print(calculate_wages(successful_delivery))

