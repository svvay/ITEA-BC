# 1. Write a Python program that accepts a string
# and calculate the number of digits and letters.
# isdigit()
# isalpha()
# "a".isdigit() - проверка на стринг или же дигитал

digit = 0
letter = 0
my_string = input("Enter please your string: ")
for symbol in my_string:
    if symbol.isdigit():
        digit += 1
    elif symbol.isalpha():
        letter += 1
print(f"Here is {digit} symbols of digit")
print(f"Here is {letter} symbols of letters")