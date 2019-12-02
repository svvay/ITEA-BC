# 6. Get two symbols of each word in string
# result: `['AV', 'is', 'la', 'An', 'co', 'of', 'In']`


# Work som

string = 'AV is largest Analytics community of India'.split()
lenght = len(string)
words = ''

for i in range(lenght):
    words = string[i]
print(words[:2], end=', ')

# Why not ... ????

# print(' '.join(map(str, range(10, 200))))

# string = 'AV is largest Analytics community of India'
# sti = [i for i in range(len((str, string.split())))]
# print(sti)
