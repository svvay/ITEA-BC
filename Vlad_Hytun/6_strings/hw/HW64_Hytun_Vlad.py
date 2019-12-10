# `string = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").`
# 4. Split words by delimiters.

import re


def split_the_string(string):
    print(re.split(';|,| ', string))


my_str = 'asdf fjdk;afed,fjek,asdf,foo'
split_the_string(my_str)