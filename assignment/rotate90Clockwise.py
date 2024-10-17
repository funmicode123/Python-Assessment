def rotate90Clockwise(matrix):
    length = len(matrix)

    for row in range(length):
        for column in range(row, length):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

    for row in range(length):
        matrix[row].reverse()

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
printMatrix(matrix)

rotate90Clockwise(matrix)

print("\nMatrix after 90-degree clockwise rotation:")
printMatrix(matrix)
