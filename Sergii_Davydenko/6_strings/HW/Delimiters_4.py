# `string = 'asdf fjdk;afed,fjek,asdf,foo' #
# String has multiple delimiters (";",","," ").`
# 4. Split words by  delimiters.

# Done

import re

string = "asdf fjdk;afed,fjek,asdf,foo"
print(re.split('[ ;,.:/?!]', string))
