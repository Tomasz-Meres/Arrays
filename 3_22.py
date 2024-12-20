###
# A function that returns a randomly selected array element
#

import random


def rand_elem(array):
    n = random.randint(0, len(array)-1)
    return array[n]


a = [1, 4, 6, 7, 8, 2, 0]
for i in range(5):
    print(rand_elem(a))
