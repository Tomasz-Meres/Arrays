###
# Functions to operate on an array of numbers
#

def second_largest(array):
    max_num = array[0]  # maximum number
    sec_num = int  # second maximum number

    # Finding the largest number
    for i in array:
        if i > max_num:
            max_num = i

    for i in array:
        # if first element is largest then set second element of the array to variable
        if i == max_num:
            sec_num = array[1]
        else:
            sec_num = array[0]

    # Finding the second-largest number
    for i in array:
        if max_num > i > sec_num:
            sec_num = i
    return sec_num


def difference(array):
    max_num = array[0]
    min_num = array[0]
    # Finding the largest number
    for i in array:
        if i > max_num:
            max_num = i

    # Finding the smallest number
    for i in array:
        if i < min_num:
            min_num = i
    return max_num - min_num


def smallest_largest(array):
    max_num = array[0]
    min_num = array[0]
    # Finding the largest number
    for i in array:
        if i > max_num:
            max_num = i

    # Finding the smallest number
    for i in array:
        if i < min_num:
            min_num = i
    return [min_num, max_num]


def median(array1):
    n = len(array1)
    array = array1[:]  # copy list
    # sorting values ascending
    for row in range(len(array)):
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                tmp = array[i]
                array[i] = array[i-1]
                array[i-1] = tmp

    if n % 2 == 0:
        med1 = n//2
        med2 = n//2+1
        return [(array[med1-1] + array[med2-1])/2]
    else:
        med = (n+1)//2
        return array[med-1]


def num_to_string(array):
    text = ''
    for i in array:
        text += str(i)
    return text
