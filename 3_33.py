###
# A program that swaps the first and last column in the array
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

tmp = 0
row = 0
for i in arr:
    first_col = i[0]  # get the value from first column
    last_col = i[len(i)-1]  # get the value from last column
    arr[row][0] = last_col  # set value of the first column
    arr[row][len(i)-1] = first_col  # set value the of last column
    row += 1


print('After changes:')
for row in arr:
    for i in row:
        print(i, end=' ')
    print()