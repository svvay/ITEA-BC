# 4. Split words by delimiters.
# String has multiple delimiters (";",","," ").`
import re

'''def delim_words(inputed_string):
    list_delimited_words = []
    list_delimeters = [' ', ',', ";", ".", "/"]
    temp_word = ""
    for letters in inputed_string:
        if letters not in list_delimeters:
            temp_word += letters
        else:
            list_delimited_words.append(temp_word)
            temp_word = ""
    list_delimited_words.append(temp_word)
    print(list_delimited_words)
    return list_delimited_words'''


def delim_words(inputed_string):
  
    result = re.split(r"[' ', ',', ';', '.', '/']", inputed_string)
    print(result)
    return result


'''# Problem - doesn't work or in split and even in 10 line!!!
ed_string = 'asdf fjdk;afed,fjek,asdf,foo'

def deliming_string(inputed_string):
    list_delimited_words = inputed_string.split(" " or ";")
    print(list_delimited_words)

deliming_string(ed_string)'''
