#     `string = AV is largest Analytics community of India`
# 4. Return first word from string.
# result: `AV`

def first_word():
    import re
    my_res = re.match(r'AV', 'AV is largest Analytics community of India')
    print(my_res.group(0))

first_word()