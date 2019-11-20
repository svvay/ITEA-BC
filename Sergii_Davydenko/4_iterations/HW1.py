# Write a Python program that accepts a string
# and calculate the number of digits and letters.
# isdigit()
# isalpha()


text = input('Enter something text: ')

number = ''
string = ''
sign = ''

for i in text:
    if i.isdigit():
        number += f'{i}'
    elif i.isalpha():
        string += f'{i}'
    else:
        sign += f'{i}'

print(f'All numbers is: {number}, \nlenght is: ', len(number))
print(f'All string is: {string}, \nlenght is: ', len(string))
print(f'All sign is: {sign}, \nlenght is: ', len(sign))
