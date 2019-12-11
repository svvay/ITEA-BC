# 4. Define a function `sum()` and a function `multiply()` that
# sums and multiplies (respectively) all the numbers in a list
# of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
# and `multiply([1, 2, 3, 4])` should return `24`.


def my_sum(*numbers):
    summa = 0
    for i in numbers:
        summa += i
    return summa

def my_multiply(*numbers):
    summa = 1
    for j in numbers:
        summa *= j
    return summa

print(my_sum(1, 2, 3, 4))
print(my_multiply(1, 2, 3, 4))
