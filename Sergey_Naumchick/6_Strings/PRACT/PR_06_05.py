'''5. Return last word from string.
result: `India`'''
import re
string = "AV is largest Analytics community of India"


def last_word_string(input_string):
    result = re.findall(r"\w+$", input_string)
    print(result)
    return result

last_word_string(string)