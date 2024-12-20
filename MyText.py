###
# A function to operate of an array of string
#


def count_words(text):
    sentence = text.split()
    return len(sentence)


def long_to_short(text):
    array = text.split()
    for row in range(len(array)):
        for i in range(1, len(array)):
            if len(array[i-1]) < len(array[i]):
                tmp = array[i]
                array[i] = array[i-1]
                array[i-1] = tmp
    return array


def alphabetically(text):
    array = text.split()
    for row in range(len(array)):
        for i in range(1, len(array)):
            if array[i-1].lower() > array[i].lower():
                tmp = array[i]
                array[i] = array[i-1]
                array[i-1] = tmp
    return array


