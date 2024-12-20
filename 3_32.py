###
# A program that swaps  the first and the last row of array
#

arr = [
    [1, 2, 3, 4, 5],
    [0, 0, 0, 0, 0],
    [1, 3, 5, 7, 9]
]

print('Before changes:')
for row in arr:
    for i in row:
        print(i, end=' ')
    print()

first_row = []  # array for first row
last_row = []  # array for last row
row = 0  # rows of the matrix
for i in arr:
    if row == 0:
        first_row = i  # get the value from first row
    elif row == len(arr)-1:
        last_row = i  # get the value from last row
    row += 1  # incrementing the row number

row = 0  # rows of the matrix
for i in arr:
    if row == 0:
        arr[0] = last_row  # set the value of the first row
    elif row == len(arr)-1:
        arr[len(arr)-1] = first_row  # set the value of the last row
    row += 1  # incrementing the row number

print('After changes changes:')
for row in arr:
    for i in row:
        print(i, end=' ')
    print()
