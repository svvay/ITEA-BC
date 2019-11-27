#Write a Python program that accepts a string
#and calculate the number of digits and letters.
#isdigit()
#isalpha()

string = input("Input your data: ")
digits = []
letters = []
signs = []

for i in string:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        signs.append(i)
print(f'there is a list of all digits: {digits}, \n the length of digits is :', len(digits))
print(f'there is a list of all letters: {letters}, \n the length of digits is :', len(letters))


