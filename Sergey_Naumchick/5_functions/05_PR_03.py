'''3. Write a function that takes a character (i.e. a
string of length 1) and returns True if it is a vowel, 
False otherwise.'''
VOLVED = 'aeiouy'

my_input = ""
while len(my_input) != 1:
    my_input = input("please input only one symbol: ")


# my_string = "a"

def my_func():
    if my_input.lower() in VOLVED:
        return print(True)
    else:
        return print(False)


my_func()
