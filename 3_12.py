###
# A program that prints all unique elements in an array
#

arr = [2, 3, 2, 5, 8, 1, 9, 8]
for i in range(len(arr)):
    unique = True
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i] == arr[j]:
            unique = False
            break
    if unique:
        print(arr[i], end=' ')
