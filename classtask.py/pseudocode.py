
#initialiaze radius to 10
#initialiaze the pie to 3.142
#to calculate the area, mulitiply the pie by radius square
#print the result

"""
radius = 10
PI = 3.142
area = PI * (radius ** 2)

print("The area of the circle is ", area)
"""




"""
prompt user for radius
store the value in variable name radius
create a variable name PI
store the value 3.142 in variable pie
calculate the area of the circle using the formular
store the result in a variable name area 
display the result
"""

radius = int(input("Enter radius: "))
name = input("Enter your name: ")
PI = 3.142
area = PI * (radius ** 2)
print("The area of the circle with", radius, "is", round(area, 2))
print("Thank you", name, "for using this app")