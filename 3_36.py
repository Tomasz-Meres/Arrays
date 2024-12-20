###
# A function that convert two-dimensional array into one-dimensional
#

def one_dimension(array):
    arr = []
    for row in array:
        for i in row:
            arr.append(i)
    return arr


a1 = [[2, 3], [1, 5]]
a2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
a3 = [[2, 1], [3, 5], [7, 4], [2, 6]]

print(a1)
print(one_dimension(a1))
print(a2)
print(one_dimension(a2))
print(a3)
print(one_dimension(a3))
