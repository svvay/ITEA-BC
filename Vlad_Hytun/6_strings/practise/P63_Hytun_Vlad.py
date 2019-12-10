# 3. Define a function `overlapping()` that takes two lists and
# returns True if they have at least one member in common,
# False otherwise. You may use your `is_member()` function,
# or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.


def overlapping(list_1, list_2):
    for item_1 in list_1:
        for item_2 in list_2:
            if item_1 == item_2:
                print('True')
                quit()
            else:
                pass
    print('False')


overlapping([1, 2, 3], [3, 4, 5])