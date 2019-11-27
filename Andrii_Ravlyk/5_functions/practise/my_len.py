#Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def flen (str1):
    n = 0
    for i in str1:
        n = n + 1
    return n