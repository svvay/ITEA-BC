# 3. Define a function `overlapping()` that takes two lists and
# returns True if they have at least one member in common,
# False otherwise. You may use your `is_member()` function,
# or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.

a = (1, "a", "b", "c", 3, "x", "y", "z")
b = (2, "f", "g", "h", 4, "o", "p", "q")
c = (5, "i", "j", "k", 1, "s", "m", "o")

def overlapping(x,y):
    for item_x in x:
        for item_y in y:
            if item_x == item_y:
                return True
    return False

overlapping(a,b)
