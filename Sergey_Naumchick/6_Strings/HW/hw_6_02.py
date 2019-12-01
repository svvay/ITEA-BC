# 2. Write a function find_longest_word() that takes
#    a list of words and returns the length of the longest one.

def find_longest_word(my_list, x=0):
    for i in my_list:
        if len(i) > x:
            x = len(i)
    return x
