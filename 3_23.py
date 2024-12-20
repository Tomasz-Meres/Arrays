###
# A program that uses MyText module
#
import MyText
text = 'An apple a day keeps the doctor away'
print('Text:', text)
print('Number of words:', MyText.count_words(text))
a = MyText.long_to_short(text)
longest = ''
for i in a:
    longest += i + ', '
print('Words from the longest:', longest[:-2])  # -2 because of ', ' one comma and ona blank space
b = MyText.alphabetically(text)
alphabet = ''
for i in b:
    alphabet += i + ', '
print('Words ordered alphabetically', alphabet[:-2])