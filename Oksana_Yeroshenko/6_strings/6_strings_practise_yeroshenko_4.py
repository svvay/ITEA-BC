my_string = "AV is largest Analytics community of India"

# 4. Return first word from string.
# result: `AV`

my_string.split(' ')[0]

# 5. Return last word from string.
# result: `India`

my_string.split(' ')[-1]

# 6. Get two symbols of each word in string
# result: `['AV', 'is', 'la', 'An', 'co', 'of', 'In']`

my_string = "AV is largest Analytics community of India"
my_string_sep = my_string.split(' ')
new_string = []
for item in my_string_sep:
    j = item[0:2]
    new_string.append(j)
print(new_string)

my_string2 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

# 7. Get date from string
