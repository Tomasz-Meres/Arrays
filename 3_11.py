###
# A program that sorts elements of an array containing integer numbers.
#

def bubble_sort(array):
    for i in array:
        for j in range(1, len(array)):
            if array[j-1] > array[j]:
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp
    return array


a = [1, 42, 53, 3, -21, 13, 5]
b = [13, 4, 13, 24]
c = [-1, 0, 42, 1, 5, 9]
print('Array:', a)
print('Sorted array:', bubble_sort(a))
print('Array:', b)
print('Sorted array:', bubble_sort(b))
print('Array:', c)
print('Sorted array:', bubble_sort(c))