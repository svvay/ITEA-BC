# Write a function find_longest_word() that takes
# a list of words and returns the length of the longest one.

# Done

# my_words = input('Enter something words: ').split()
# length = 0

def find_longest_word(my_words, length):
    for word in my_words:
        if len(word) > length:
            length = len(word)
    # print(length)
    return length


# find_longest_word(my_words, length)
