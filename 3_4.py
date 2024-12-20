###
# A program that finds maximum and minimum number
#

arr = [-15, 8, -31, 47, -2, 19]
max_num = 0
min_num = 0

for i in arr:
    if max_num:
        if i > max_num:
            max_num = i
    else:
        max_num = i

for i in arr:
    if min_num:
        if i < min_num:
            min_num = i
    else:
        min_num = i  

print(max_num)
print(min_num)
