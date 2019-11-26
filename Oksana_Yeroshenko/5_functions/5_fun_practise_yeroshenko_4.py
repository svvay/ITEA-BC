# 4. Define a function `sum()` and a function `multiply()` that
# sums and multiplies (respectively) all the numbers in a list
# of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
# and `multiply([1, 2, 3, 4])` should return `24`.

import random
a_list = []
b = random.randint(2,10)
while b > 0:
    c = random.randint(1,100)
    a_list.append(c)
    b -= 1

def x_sum(a_list):
    the_sum = 0
    for item in a_list:
        the_sum += item
    return the_sum

def x_mult(a_list):
    the_mult = 1
    for item in a_list:
        the_mult *= item
    return the_mult
