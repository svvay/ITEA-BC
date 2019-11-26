'''1. The function `max()` and `max_of_three()` from previous exercises
will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many they are?
Write a function max_in_list()
that takes a list of numbers and returns the largest one.'''

list1 = [1, 3, 7, 2, 4, 6,8]
print(list1)


def max_in_list(list):
    temp = None
    for i in list:
        if temp == None:
            temp = i
        else:
            if temp < i:
                temp = i
    print(temp)


max_in_list(list1)
