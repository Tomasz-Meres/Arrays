###
# A program that calculates and prints the array and the
# arithmetic mean of array values
#

arr = [15, 8, 31, 47, 2, 19]
array_length = len(arr)
total = 0
for i in arr:
    total += i
arithmetic_mean = total / array_length

print(round(arithmetic_mean, 2))
