###
# A program to separate even and odd numbers of a given array of integers
#

arr = [7, 9, 2, 4, 5, 6]


def even_odd_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] % 2 != 0 and arr[j+1] % 2 == 0:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


print(arr)
print(even_odd_sort(arr))