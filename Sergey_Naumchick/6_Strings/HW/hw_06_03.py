# 3. Write a function filter_long_words() that takes a list
#    of words and an integer n and returns the list of words that
#    are longer than n.

def filter_long_words(n, my_list=[]):
    my_list2 = []

    for i in my_list:
        if len(i) > n:
            my_list2.append(i)

    return my_list2
