def right_angle_triangle():
    for outter in range (1, 10):
        for inner in range (outter):
            print("*", end = "")
        print()

def inverted_right_angle_triangle():
    for outter in range (9, 0, -1):
        for inner in range (outter):
            print("*", end = "")
        print()

def inverted_left_angle_triangle():
    row = 10
    for outter in range (row, 0, -1):
        print(" " * (row - outter), end = "")
        print("*" * outter)

def left_angle_triangle():
    for outter in range (1, 10):
        print(" " * (9 - outter), end = "")
        print("*" * outter)


print("Right-Angle Triangle:")
right_angle_triangle()

print("\nInverted Right-Angle Triangle:")
inverted_right_angle_triangle()

print("\nInverted Left-Angle Triangle:")
inverted_left_angle_triangle()

print("\nLeft-Angle Triangle:")
left_angle_triangle()