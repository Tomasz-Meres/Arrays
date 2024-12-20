###
# A program that counts the numbers of occurrences of any value from a tuple
#

tup = [50, 20, 40, 50, 30, 50]
print('Tuple: ', end=' ')
for i in tup:
    print(i, end=' ')
print()

num = int(input('Value: '))

occurs = 0
for i in tup:
    if i == num:
        occurs += 1
print('Number of occurrences: ', occurs)
