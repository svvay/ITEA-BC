import re

# pattern = re.compile("ab+", re.IGNORECASE)
#
# example_string = "ab cd abb aaaa abb"
#
# matches = pattern.finditer(example_string)
# print(matches)
# for x in matches:
#     print(x)
#     print(x.group())
# match = pattern.match(example_string)
# print(match)
# pattern = re.compile("[А-Я]", re.IGNORECASE)
# example_string = "АВ ВГ ЖЗ Ё"
# matches = pattern.findall(example_string)
#
# p = re.compile("[a-z]+")
# p = re.compile("[^ \t\n\r\f\v]")
#
# # p.match("abcd")
#
# m = p.match("emTpo")
# m.group()
#
# m.start(), m.end()
# m.span()
#
# print(p.match("::: message"))
#
# m = p.search("::: message")
# print(m)
#
# m.group()
#
# m.span()

# How it used
pattern = re.compile("[a-z]+")
match = pattern.match("string goes here")
find_all = pattern.findall("string goes here")
find_iter_all = pattern.finditer("string goes here")
if match:
    print("Match found: ", match.group())
else:
    print("No match")


pattern = re.compile("\d+")

all_matches = pattern.findall(
    "12 drummers drumming, 11 pipers piping, 10 lords a-leaping"
)
iterator_matches = pattern.finditer("12 drummers drumming, 11 ... 10 ...")

# We can also use directly this functions from re module
print(re.match(r"From\s+", "Fromage amk"))
print(re.match(r"From\s+", "From amk Thu May 14 19:12:10 1998"))
