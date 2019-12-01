# 1. Write a program that maps a list of words into a list
#    of integers representing the lengths of the corresponding words.

def num_let_word(my_list):
    my_list2 = []
    for i in my_list: my_list2.append(len(i))
    return my_list2
