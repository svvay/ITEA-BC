# 2. Write a function find_longest_word() that takes
# a list of words and returns the length of the longest one.


def find_longest_word(my_list):
    # lenlist = [len(i) for i in my_list.split(',')]
    # print(max(lenlist))
    print(max([len(i) for i in my_list.split(',')]))


ent_list = input("Enter list of words use separator , : ")
find_longest_word(ent_list)