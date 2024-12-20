###
# A program that calculates the sum of values in the last column
#

matrix = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

sum_of_last_col = 0
for row in matrix:
    sum_of_last_col += row[-1]

for row in matrix:
    for i in row:
        print(i, end=' ')
    print()

print('Sum of values in the last column:', sum_of_last_col)
