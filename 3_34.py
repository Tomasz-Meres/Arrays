###
# A function that returns an identity matrix of size n
# And function to display matrix
#

def identity_matrix(n):
    array = []
    for i in range(n):
        array.append([])
        for j in range(n):
            if i == j:
                array[i].append(1)
            else:
                array[i].append(0)
    return array


def show_matrix(array):
    for row in array:
        for i in row:
            print(i, end=' ')
        print()
    return ''


print('Matrix 3x3:')
show_matrix(identity_matrix(3))
print('Matrix 5x5:')
show_matrix(identity_matrix(5))
print('Matrix 8x8:')
show_matrix(identity_matrix(8))
