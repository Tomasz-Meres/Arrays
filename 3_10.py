###
# A program that prints the numbers from the first array that
# do not appear in the second array
#

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

for i in arr1:
    not_equal = True
    for j in arr2:
        if i == j:
            not_equal = False

    if not_equal:
        print(i, end=' ')

