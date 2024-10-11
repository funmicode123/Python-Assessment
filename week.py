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

equivalent_day = todays_day % 7  

print(f"The day is: {today_day[equivalent_day]}")
