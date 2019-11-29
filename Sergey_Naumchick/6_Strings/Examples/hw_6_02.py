# 2. finding longest words lenght
def num_longest_word(my_list=[], _=0):
    for i in my_list:
        if len(i) > _:
            _ = len(i)
    return _