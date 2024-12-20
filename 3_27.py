###
# A program that prints array values in rows and columns
#

matrix = [
    [2, 4, 6, 2],
    [3, 5, 2, 6],
    [1, 2, 4, 5]
]

for row in matrix:
    for i in row:
        print(i, end=' ')
    print()
    