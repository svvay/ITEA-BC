item_digit = 0
item_alpha = 0

a_string = input("Input a string: ")

for item in a_string:
    if item.isdigit():
        item_digit += 1
    if item.isalpha():
        item_alpha += 1
print(f"Quantity of digits is: {item_digit}. Quantity of letters is: {item_alpha}.")









# 1. Write a Python program that accepts a string
# and calculate the number of digits and letters.
# isdigit()
# isalpha()