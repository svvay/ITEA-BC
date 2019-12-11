'''3. Define a function `overlapping()` that takes two lists and
returns True if they have at least one member in common,
False otherwise. You may use your `is_member()` function,
or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.'''
l1 = ["111", "asd", "dsa"]
l2 = ["111", "asd", "dssa"]


def overlaping(list_1, list_2):
    temp = []
    for word in list_1:
        for word_2 in list_2:
            if word == word_2:
                print(f"{word} is common for both lists!")
                temp.append(word)
    print(temp)
    return temp


overlaping(l1, l2)
