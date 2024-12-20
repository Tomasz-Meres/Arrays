###
# A program that prints the contents of the array in reverse order
#

arr = [15, 8, 31, 47, 2, 19]

print('existed array:', end=' ')
for i in range(len(arr)):
    print(arr[i], end=' ')

print()

print('reverse array:', end=' ')
for i in range(1, len(arr) + 1):
    print(arr[-i], end=' ')