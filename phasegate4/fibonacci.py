'''
x = 0
y = 1
fibonacci_number = 10

for number in range(fibonacci_number):
    print(x, end=" ")
    x, y = y, x + y
'''

x = 0
y = 1
limit = int(input("Enter the upper limit for Fibonacci numbers: "))

while x <= limit:
    print(x, end=" ")
    x, y = y, x + y  
