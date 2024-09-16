def milli_seconds(milli_seconds)
    return time_string

milli_seconds = int(input("Enter the Milli Seconds:  "))
seconds_per_hour = 3600
minutes_per_hour = 60
seconds_per_minute = 60

total_seconds = milli_seconds // 1000
hours = total_seconds // seconds_per_hour
minutes = (total_seconds % seconds_per_hour) // minutes_per_hour
seconds = total_seconds % seconds_per_minute
time_string = (f"{hours:02}:{minutes:02}:{seconds:02}")

print(time_string)



