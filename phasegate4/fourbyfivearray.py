'''
zeros_list = [ [0] * 4 ]
for _ in range (5):
    for row in range(len(zeros_list)):
        for column in range(len(zeros_list[row])):
            print(zeros_list[row][column], end=" ")
        print()
'''
'''
zeros_list = [ [1, 2, 3 ,4] ]
for _ in range (5):
    for row in range(len(zeros_list)):
        for column in range(len(zeros_list[row])):
            print(zeros_list[row][column], end=" ")
        print()
'''
import random

zeros_list = [ [random.rand] * 4]
for _ in range (5):
    for row in range(len(zeros_list)):
        for column in range(len(zeros_list[row])):
            print(zeros_list[row][column], end=" ")
        print()
