# 3. Write a function that takes a character (i.e. a
# string of length 1) and returns True if it is a vowel,
# False otherwise.

def  my_char(char):
    if char in 'aeiouyAEIOUY':
        print("TRUE")
    else:
        print("FALSE")

my_char('a')