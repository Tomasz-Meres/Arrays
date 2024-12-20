###
# A program that finds the smallest and largest values in the array
# and in which row and column they are located
#

matrix = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

# Finding the maximum number
row_max = 1
col_max = 0
max_num = 0
row = 1
for i in matrix:
    for j in range(len(i)):
        if i[j] > max_num:
            max_num = i[j]
            row_max = row
            col_max = j+1
    row += 1

# Finding the minimum number
row_min = 1
col_min = 0
min_num = 0
row = 1
for i in matrix:
    for j in range(len(i)):
        if i[j] < min_num:
            min_num = i[j]
            row_min = row
            col_min = j+1
    row += 1

print('Maximum value:', max_num)
print('Row:', row_max)
print('Column:', col_max)

print('Minimum value:', min_num)
print('Row:', row_min)
print('Column:', col_min)
