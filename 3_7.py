###
# A program that prints the longest name
#

name = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
name_characters = 0
index_name = 0  # index of longest name
current_index = 0

for i in name:
    if len(i) > name_characters:
        name_characters = len(i)
        index_name = current_index
    current_index += 1

print('Names:', end=' ')
for i in name:
    print(i, end=' ')
print()
print('Longest name:', name[index_name])

