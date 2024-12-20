###
# A function that returns True if a given number is present in  an array
#

def occurs(number, array):
    for i in array:
        if i == number:
            return True
    return False


n = int(input('Number: '))
arr = [15, 38, 7, 23, 14]
print(f'Result: number {n} appears in the array {occurs(n, arr)}')
