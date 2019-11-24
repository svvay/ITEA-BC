# . Define a function `max()` that takes two numbers as arguments
# and returns the largest of them. Use the if-then-else construct
# available in Python. (It is true that Python has the `max()` function
# built in, but writing it yourself is nevertheless a good exercise.)"""

import random
a = 0
my_list = []

while a < 10:
    b = random.randint(1,500)
    my_list.append(b)
    a += 1

def maxx(my_list):
    i = 0
    for a_num in my_list:
        if i < len(my_list) - 1:
            if my_list[i] > my_list[i+1]:
                a_num = my_list[i]
            else:
                a_num = my_list[i+1]
            i += 1
        else:
            break
    return a_num
