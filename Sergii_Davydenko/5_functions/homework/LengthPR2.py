# 2. Define a function that computes the length of a
# given list or string. (It is true that Python has
# the len() function built in, but writing it yourself
# is nevertheless a good exercise.)

# DOne, all good

# string = input('Enter something list or string: ')

def length(string):
    leng = 0
    for i in string:
        leng += 1
    return leng

# print(length(string))
