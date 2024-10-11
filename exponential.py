"""
1. print the header line
2. get the count variable starting from 1 and saved as 'a'
3. get the count variable from 2 and saved as 'b'
4. calculate the exponential of 'a' by 'b' 
5. save the result as 'a**b'
""" 

number_times = int(input("number of times: "))
multiple_number = int(input("multiple number: "))

print(f"a\tb\ta**b")
for count in range(1, number_times + 1):
    print(count, multiple_number, "=", count ** multiple_number)
    multiple_number +=1