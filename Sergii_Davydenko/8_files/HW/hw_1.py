# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
# ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name
# (pointing to a list of words) from the program arguments and finds and prints all pairs of words that are
# semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output
# should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

# Done

# my_semordnilap = 'file_txt/semordnilap.txt'

def semordnilap(my_semordnilap):
    file = open(my_semordnilap)
    words = file.read().lower().split()
    file.close()
    palindrom = []
    for first in words:
        for second in words:
            if first == second[::-1]:
                palindrom.append(first)
    return palindrom

# print(semordnilap('file_txt/semordnilap.txt'))
