# 3. Write a function that takes a character (i.e. a
# string of length 1) and returns True if it is a vowel,
# False otherwise.

def if_vowel():
    x_vowels = ("aeiou")
    letter = input("Input the letter, please: ")
    letter = letter[0]
    if letter in x_vowels:
        x_rezult = True
    else:
        x_rezult = False
    return x_rezult

def if_vowel():
    a = str("aeiou")
    b = input("Input a letter: ")
    if len(b) > 1:
        b = b[0]
    if b in a:
        x_res = True
    else:
        x_res = False
    return x_res