matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

n = 0  # index of row in matrix
m = 0  # index of column in matrix
for row in matrix:
    for i in row:
        if m == n:
            matrix[n][m] = 1
        else:
            m += 1
    n += 1
    m = 0

print('=====')
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()