# 3. Write a function filter_long_words() that takes
# a list of words and an integer n and returns the list
# of words that are longer than n.

# Done

my_words = input('Enter something words: ').split()
length = int(input('Enter some digit: '))

def filter_long_words(my_words, length):
    words = []
    for word in my_words:
        if len(word) > length:
            words.append(word)
    print(words)
    # return words

filter_long_words(my_words, length)