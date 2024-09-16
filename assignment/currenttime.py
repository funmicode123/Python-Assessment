
import time

current_time = time.time()
seconds_per_hour = 3600
minutes_per_hour = 60
seconds_per_minute = 60

total_seconds = int(current_time)
hours = total_seconds // seconds_per_hour
minutes = (total_seconds % seconds_per_hour) // minutes_per_hour
seconds = total_seconds % seconds_per_minute
class_time = (f"{hours:02}:{minutes:02}:{seconds:02}")

print(class_time)
