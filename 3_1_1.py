###
# Program that calculates and prints the number of even values in the array
#
arr = [34, 7, 19, 4, 21, 8]
even_number = 0
n = 0
while arr:
    if n < len(arr):
        if arr[n] % 2 == 0:
            even_number += 1
    else:
        break
    n += 1

print(even_number)