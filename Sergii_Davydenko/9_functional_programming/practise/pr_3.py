# Write decorator that print function name before and after function execution. func.__name__

# Done

def name_fu(func):
    def wrapper():
        name_fu(func)
        print(f'The names of func is - {func.__name__}')
    return wrapper

@name_fu
def sums():
    print('Hallo world')
    return sums
sums()




# In this kata, you must create a digital root function.
#
# A digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one
# digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# n = 16
# def digital(n):
#     while len(n) != 1:
#
#     for numb in (n):
#         print(numb)
#         # print(lambda x, y: x + y)
#
#
# digital(n)

