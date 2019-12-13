'''1. According to Wikipedia, a emordnilap is a word or phrase that spells
a different word or phrase backwards. ("Semordnilap" is itself
"palindromes" spelled backwards.)
Write a semordnilap recogniser that accepts a file name (pointing to a list of words)
from the program arguments and finds
and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the
the output should include the pair "stressed desserts". Note, by the way,
that each pair by itself forms a palindrome!'''


def semordnilap_recogniser(file_name):
    with open(f"{file_name}.txt", "r") as file_semordnilap:

        list_semordnilap = []
        list_lines = file_semordnilap.readlines()

        for lines in list_lines:
            if lines.lower().rstrip() == lines.lower().rstrip()[::-1]:
                list_semordnilap.append(lines.rstrip())
    print(list_semordnilap)
    return list_semordnilap

    with open("../Text_Files/HW_01_result.txt", "w") as file_result:

        for elements in list_semordnilap:
            file_result.write(f"{elements}\n")


semordnilap_recogniser("../Text_Files/HW_01_Semordnilap")
