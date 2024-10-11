today_day = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

print(today_day)
todays_day = int(input("Enter today's day: "))
day_number = int(input("Enter the number of days elapsed since today: "))

days_number = todays_day + day_number

equivalent_day = days_number % 7  

print(f"The day is: {today_day[equivalent_day]}")
