"""
collect the temperature in celsius
save the variable as celsius
perform calculation, (9/5) * celsius + 32
save result as fahrenheit
display the result
"""

celsius = float(input("Enter the temperature in celsius: "))
NINE = 9
FIVE = 5
TEMP = 32

fahrenheit = (NINE/FIVE) * celsius + TEMP

print(f"Fahrenheit conversion is {fahrenheit:.1f}")