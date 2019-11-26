import timeit

def max_in_list(*numbers):
    s = [i for i in numbers]
    s.sort(reverse=True)
    return s[0]

def maxx(my_list):
    i = 0
    for a_num in my_list:
        if i < len(my_list) - 1:
            if my_list[i] > my_list[i + 1]:
                a_num = my_list[i]
            else:
                a_num = my_list[i + 1]
            i += 1
        else:
            break
    return a_num
TEST_CODE_1 = '''
max_in_list(list(range(10000)))
'''
TEST_CODE_2 = '''
maxx(list(range(10000)))
'''
print(timeit.timeit(setup="from __main__ import max_in_list", stmt = TEST_CODE_1, number = 10000))
print(timeit.timeit(setup="from __main__ import maxx", stmt = TEST_CODE_2, number = 10000))