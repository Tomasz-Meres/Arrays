###
# A program that calculates and prints the array and the
# arithmetic mean of array values
#

arr = [15, 8, 31, 47, 2, 19]
array_length = len(arr)
n = array_length
total = 0

while n > 0:
    total += arr[n-1]
    n -= 1

arithmetic_mean = total / array_length
print(round(arithmetic_mean, 2))
