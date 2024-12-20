###
# A program that prints the array values graphically
#

arr = [2, 6, 4, 9, 7]


def star(n):
    text = ''
    for i in range(n):
        text += '*'
    return text


for i in range(len(arr)):
    print(f'{arr[i]}: {star(arr[i])}')
