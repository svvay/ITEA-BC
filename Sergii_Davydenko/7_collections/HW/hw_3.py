# List slices:
#
#     Use a slice to print the first three items from that program’s list.
#     Use a slice to print three items from the middle of the list.
#     Reverse your list from first index to the end.
#     Use a slice to print the last three items in the list.

# Done

my_list = ('Use a slice to print the first three items').split()

print(my_list[:3])
print(my_list[3:6])
print(my_list[::-1])
print(my_list[(len(my_list) - 1)])
print(my_list[-1:])
