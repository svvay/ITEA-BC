'''6. Get two symbols of each word in string
result: `['AV', 'is', 'la', 'An', 'co', 'of', 'In']`
'''
import re


def found_first_2_let(input_string):
    result = re.findall(r'\b\w.', input_string)
    print(result)
    return result
