###
# A program that, for the given array of real numbers, prints the number of elements that are
# greater than the given value entered from keyboard
#

arr = [13.22, 1, 355.01, 44.44, 23.42, 50]
num = float(input('Enter a real number: '))
print(f'Numbers', end=' ')
for i in arr:
    if i > num:
        print(i, end=' ')
print(f'are greater than {num}')