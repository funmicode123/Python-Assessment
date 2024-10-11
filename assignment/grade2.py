passes = 0
failures = 0

for student in range(10):
    result = int(input('Enter result (pass = 1, fail = 2): '))

    if result == 1:
        passes += 1
    else:
        failures += 1

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to the facilitator')