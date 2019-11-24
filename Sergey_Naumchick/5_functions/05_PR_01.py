# 1. Define a function `max()` that takes two numbers as arguments
# and returns the largest of them. Use the if-then-else construct
# available in Python. (It is true that Python has the `max()` function
# built in, but writing it yourself is nevertheless a good exercise.)
TEMP = 0


def max(a, b):
    if a <= b:
        return b
    if b < a:
        return a


while TEMP == 0:
    try:
        a, b = input("please input two numbers: (like 12/13)\n").split("/")

        a = int(a)
        b = int(b)
        print(max(a, b))
        TEMP = 1

    except ValueError as e:
        print('You entered not numerical type, numbers without "/" try again')
        print(e.args[0])
