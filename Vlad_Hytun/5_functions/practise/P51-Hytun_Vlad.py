# 1. Define a function `max()` that takes two numbers as arguments
# and returns the largest of them. Use the if-then-else construct
# available in Python. (It is true that Python has the `max()` function
# built in, but writing it yourself is nevertheless a good exercise.)"""

def my_max(first_num, second_num):
    if first_num >= second_num:
        return first_num
        # print(f"First number is MAX and ={first_num}")
    elif second_num > first_num:
        return second_num
        # print(f"Second number is MAX and ={second_num}")

print(my_max(101,78))
