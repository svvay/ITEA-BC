# 5. Write a function `is_member()` that takes a value
# i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise.
# (Note that this is exactly what the `in` operator does, but
# for the sake of the exercise you should pretend Python
# did not have this operator.)

def is_member():
    a = input("Input list of values separating by SPACE key: ").split()
    x = input("Input x: ")
    for item in a:
        if item == x:
            x_res = True
            break
        else:
            x_res = False
    return x_res