###
# A program that modifies the array values to create a multiplication table
#


def create_2d_arr(x, y):
    array = [[0 for i in range(y)] for j in range(x)]
    return array


def fill_2d_arr(array):
    # set first column with values
    n = 1
    for row in array:
        row[0] = n
        n += 1

    # set other values
    for row in array:
        for i in range(1,len(row)):
            row[i] = row[0] * (i+1)
    return array


matrix = create_2d_arr(5, 5)
fill_2d_arr(matrix)
for row in matrix:
    for i in row:
        print(i, end=' ')
    print()
