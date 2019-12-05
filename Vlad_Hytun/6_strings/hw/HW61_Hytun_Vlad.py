# 1. Write a program that maps a list of words into a list
# of integers representing the lengths of the correponding words.


def list_to_int(ent_list):
    len_list = []
    enter_list = ent_list.split(',')
    for word in enter_list:
        len_list.append(len(word))
    print(f"List in numbers looks like: {len_list}")


ent_list = input("Enter your list of word, please use separator , : ")
list_to_int(ent_list)
