#a = 300
#b = 300
#my_list = [1,2,3,4]
#my_list_2 = [1,2,3,4]
#my_string = "abc"
#my_string_2 = "abc"
#a = 0
#while a < 10:
#    print(f"{a}")
#    a += 1

# a = 0
# while True:
#     if a == 5:
#         print(a)
#         break
#     elif a == 2:
#         print(a)
#         continue
#     else:
#         print(a)
#     a += 1
#
# user_value = None
# while not user_value:
#     if not user_value:
#         user_value = input("Please enter your value: ")
#     #else:
#      #   break
#
#
# my_list = [1,2,3,4,5,6]
# for element in my_list:
#     if element == int(user_value):
#         break
#     if element == 3:
#         continue
#     print(element, type(element))
#
# while my_list:
#     my_list.pop()
# pass
#
# while len(my_list) < 10:
#     my_list.append(1)


# my_string = "abcde"
# for char in my_string:
#     print(char)
#

my_dict = {"Kyivstar": ["097", "067"], "Life": "093"}
# for operator_name, operator_code in my_dict.items():
#     print(operator_code,operator_name)
# pass


# for operator_name, operator_code in my_dict.items():
#     if type(operator_code) == list:
#         for code in operator_code:
#             print(operator_name, code)
#         continue
#     print(operator_name,operator_code)
my_dict_iterator = iter(my_dict.items())
