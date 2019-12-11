'''    `string = AV is largest Analytics community of India`
4. Return first word from string.
result: `AV`'''
import re


def first_word_string(input_string):
    result = re.findall(r'^\w+', input_string)
    print(result)
    return result
