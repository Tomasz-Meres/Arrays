###
#
#

def compare(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] == array2[i]:
                continue
        return True
    else:
        return False


print('Array1: ', ["water","book","sky"])
print('Array2:', ["water","book","sky"])
print('Arrays are the same', compare(["water","book","sky"], ["water","book","sky"]))
print()
print('Array1: ', [True,False])
print('Array2:', [True,False,True])
print('Arrays are the same', compare([True,False], [True,False,True]))
print()
print('Array1: ', [5,3,1])
print('Array2:', [5,3,1])
print('Arrays are the same', compare([5,3,1], [5,3,1]))
print()
print('Array1: ', [3,2,1])
print('Array2:', [3,2])
print('Arrays are the same', compare([3,2,1], [3,2]))

