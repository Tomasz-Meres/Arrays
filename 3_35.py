###
# A function that returns transposed matrix
#

def transpose_matrix(m):

    transposed = []
    if isinstance(m[0], list):  # Check if it's already a 2D matrix
        for row in zip(*m):  # zip(*m) groups elements column-wise and returns tuple
            new_row = list(row)  # Convert the tuple to a list
            transposed.append(new_row)  # Append the list to the transposed matrix
        return transposed
    else:
        return [[i] for i in m]


def show_matrix(array):
    for row in array:
        for i in row:
            print(i, end=' ')
        print()
    return ''


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

b = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

c = [5, 6, 7, 8]
print('Original matrix:')
show_matrix(a)
print('Transposed matrix:')
show_matrix(transpose_matrix(a))

print('Original matrix:')
show_matrix(b)
print('Transposed matrix:')
show_matrix(transpose_matrix(b))

print('Original matrix:')
for i in c:
    print(i, end=' ')
print()
print('Transposed matrix:')
show_matrix(transpose_matrix(c))
