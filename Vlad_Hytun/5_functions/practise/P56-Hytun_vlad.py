# 6. Define a function `overlapping()` that takes two lists and
# returns True if they have at least one member in common,
# False otherwise. You may use your `is_member()` function,
# or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.

def is_memeber():
    a = input("Input first list of values about SPACE: ").split()
    x = input("Input second list of values about SPACE: ").split()
    result = False
    for itema in a:
        if result == True:
            break
        for itemx in x:
            if itema == itemx:
                result = True
            else:
                result = False
    print(f"Result of your efforts: {result}")
    return result

is_memeber()