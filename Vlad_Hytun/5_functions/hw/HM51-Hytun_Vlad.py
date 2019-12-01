# # HW
# # 1. The function `max()` and `max_of_three()` from previous exercises
# # will only work for two and three numbers, respectively.
# # But suppose we have a much larger number of numbers,
# # or suppose we cannot tell in advance how many they are?
# # Write a function max_in_list()
# # that takes a list of numbers and returns the largest one.
# #
# # # Write test with 3-4 cases

def max_in_list(*nums):
    max_num = max(nums)
    print(max_num)

max_in_list(2,4,567,765,1)
max_in_list(1)
max_in_list(1,1)
max_in_list(0)
max_in_list('A')
max_in_list(None)