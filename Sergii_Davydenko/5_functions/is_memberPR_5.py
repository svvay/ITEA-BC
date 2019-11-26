# 5. Write a function `is_member()` that takes a value
# i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise.
# (Note that this is exactly what the `in` operator does, but
# for the sake of the exercise you should pretend Python
# did not have this operator.)

#Done, Work, maybe right

numbs = input('Enter something number: ')
lists = input("Enter lists of values: ").split()

count = lists.count(numbs)

if count >= 1:
    print('Yep u right: ', count)
else:
    print(f'Sorry, but count is {count}:')