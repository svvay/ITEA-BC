# 2. Write a function find_longest_word() that takes
#    a list of words and returns the length of the longest one.

def find_longest_word(my_list, word_lenght=0):
    for word in my_list:
        if len(word) > word_lenght:
            word_lenght = len(word)
    return word_lenght
