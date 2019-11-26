# 3. Write a Python program that accepts a sequence of lines (blank line to terminate) as input
# and prints the lines as output (all characters in lower case).

enter_lines = ' '
while len(enter_lines) > 0:
    enter_lines = input("Input some lines of text:\n ")
    if enter_lines == " ":
        break
    else:
        print(enter_lines)
