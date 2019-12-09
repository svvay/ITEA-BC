'''1. Write a version of a palindrome recogniser that accepts a file name
from the sys.argv, reads each line, and prints the line to the screen if it
is a palindrome and write results to file like {source_name}/{result}.'''

def palindrom_finder():
    list_palindrome = []

    with open("../Text_Files/PR_01_Palindrom.txt", "r") as file_palindrome:

        list_lines = file_palindrome.readlines()

        for lines in list_lines:
            lines = lines.rstrip()
            if lines.lower().rstrip().replace(" ","") == lines.lower().rstrip().replace(" ","")[::-1]:
                list_palindrome.append(lines)

    #print(list_palindrome)
    if len(list_palindrome) == 0:
        print("sorry there are no palindrome in text")

    else:
        with open("../Text_Files/PR_01_result.txt", "w+") as file_result:

            for words_pal in list_palindrome:
                file_result.write(f"{words_pal}\n")

            print("all done!")

palindrom_finder()