'''3. Write a function that takes a character (i.e. a
string of length 1) and returns True if it is a vowel, 
False otherwise.'''
VOLVED = 'aeiouy'

my_input = ""
while len(my_input) != 1:
    my_input = input("please input only one symbol: ")



def my_func(func):
    if func in VOLVED:
        return True
    else:
        return False


if (my_func(my_input))==True:
    print("True")
else: print("False")
