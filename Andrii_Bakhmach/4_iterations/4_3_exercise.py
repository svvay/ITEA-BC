#Write a Python program that accepts a sequence of lines (blank line to terminate) as input
#and prints the lines as output (all characters in lower case).

our_line = input("please, input you text: ")
if our_line is None:
    print("input your text once more")
else:
    print(our_line.lower())







