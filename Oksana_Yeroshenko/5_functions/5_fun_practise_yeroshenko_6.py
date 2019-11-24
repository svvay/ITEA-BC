# 6. Define a function `overlapping()` that takes two lists and
# returns True if they have at least one member in common,
# False otherwise. You may use your `is_member()` function,
# or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.

def overlapping():
    a_list = input("Input list A by space: ").split()
    b_list = input("Input list B by space: ").split()
    for i in a_list:
        for j in b_list:
            if i != j:
                x_res = False
            else:
                x_res = True
                return x_res
    return x_res