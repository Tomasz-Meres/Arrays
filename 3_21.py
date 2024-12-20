###
# A program that checks whether the first array is a subset of the second one
#

arr1 = [1, 3, 5, 7]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8]


def array_subset(array1, array2):
    for i in array1:
        appears = False
        for j in array2:
            if i == j:
                appears = True
                break
        if appears is False:
            return False
    return True


print(array_subset(arr1, arr2))
