###
# A function that creates and returns two-dimensional array with
# values of 0
#


def create_2d_arr(x, y):
    array = [[0 for i in range(y)] for j in range(x)]
    return array


for row in create_2d_arr(3, 5):
    for i in row:
        print(i, end=' ')
    print()
