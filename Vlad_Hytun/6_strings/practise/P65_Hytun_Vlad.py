#     `string = AV is largest Analytics community of India`
# 5. Return last word from string.
# result: `India`

def last_word():
    import re
    my_result = re.findall(r'\w+$', 'AV is largest Analytics community of India')
    print(my_result)


last_word()