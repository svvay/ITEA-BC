# 3. Write a Python program that accepts a sequence of lines (blank line to terminate) as input
# and prints the lines as output (all characters in lower case).

sequence = []
while True:
    text = input('Enter something lines: ')
    if text:
        sequence.append(text.lower())
    else:
        break
for text in sequence:
    print(text)
