###
# A program that uses module MyArrays
#
import MyArrays

arr = [7, 3, 8, 5, 2]
print('Numbers:', arr)
print('Second largest number:', MyArrays.second_largest(arr))
print('Diffrence between the largest and smallest values:', MyArrays.difference(arr))
print('Median:', MyArrays.median(arr))
small_large = MyArrays.smallest_largest(arr)
print(f'Smallest and largest number: {small_large[0]}, {small_large[1]}')
print(arr)
print('Number as a string:', MyArrays.num_to_string(arr))
