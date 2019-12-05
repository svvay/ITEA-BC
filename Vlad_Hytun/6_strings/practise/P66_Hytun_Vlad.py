# 6. Get two symbols of each word in string
# # result: `['AV', 'is', 'la', 'An', 'co', 'of', 'In']`


def two_symbols():
    import re
    result = re.findall(r'\w\w', 'AV is largest Analytics community of India')
    print(result)


two_symbols()
