# 3. from your list making list longer than inputed n
def filter_long_words(n, my_list=[]):
    my_list2 = []

    for i in my_list:
        if len(i) > n:
            my_list2.append(i)

    return my_list2