# 3. Define a function `overlapping()` that takes two lists and
# returns True if they have at least one member in common,
# False otherwise. You may use your `is_member()` function,
# or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.

# Done


# firstl = input('Enter something: ')
# secondl = input('Enter something: ')

def overlapping(firstl, secondl):
    for over in firstl:
        for lapping in secondl:
            if over == lapping:
                return True
    return False

# print(overlapping(firstl, secondl))