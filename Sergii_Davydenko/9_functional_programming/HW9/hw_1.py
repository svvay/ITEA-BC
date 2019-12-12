# The third person singular verb form in English is distinguished by the suffix
# -s, which is added to the stem of the infinitive form: run -> runs. A simple
# set of rules can be given as follows:
# If the verb ends in y, remove it and add ies If the verb ends in o, ch, s, sh,
# x or z, add es By default just add s Your task in this exercise is to define a
# function make_3sg_form() which given a verb in infinitive form returns its third
# person singular form. Test your function with words like try, brush, run and fix.
# Note however that the rules must be regarded as heuristic, in the sense that you
# must not expect them to work for all cases. Tip: Check out the string method endswith().

# DOne + test

# my_file = 'text_file/test.txt'


def singular(my_file):
    text = open(my_file)
    words = text.read().lower().split()
    text.close()
    sing_word = []
    for word in words:
        len_word = len(word)
        if word.endswith('y'):
            sing_word.append(str(word)[:(len_word-1)] + 'ies')
        elif word.endswith(('o', 's', 'x', 'z')):
            sing_word.append(str(word)[:(len_word - 1)] + 'es')
        elif word.endswith(('ch', 'sh')):
            sing_word.append(str(word)[:(len_word - 2)] + 'es')
    return sing_word

# print(singular(my_file))
