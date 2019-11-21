my_string = input("Please input line: ")
letters = 0
input_letters = ""
digits = 0
input_digits = []
symbols = []

for i in my_string:
    if i.isalpha():
        letters += 1
        input_letters += f" {i}"
    elif i.isdigit():
        digits += 1
        input_digits.append(i)
    else:
        symbols.append(i)
print(f"in your line there are {letters} letters:")
print(input_letters)

print(f"in your line there are {digits} digits:")
print(input_digits)

print(symbols)
