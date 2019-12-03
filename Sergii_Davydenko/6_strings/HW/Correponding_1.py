# 1. Write a program that maps a list of words into
# a list of integers representing the lengths of the
# correponding words.

# Done


my_words = map(int, input('Enter something numbers: ').split())

for index, element in enumerate(my_words):
    print(index, element, end=' // ')
