# # Practise
#
# * Write test with 3-4 cases for each exercise
#
# 1. Define a function `generate_n_chars()` that takes an
# integer n and a character c and returns a string, n
# characters long, consisting only of c:s. For example,
# `generate_n_chars(5,"x")` should return the string "xxxxx".
# (Python is unusual in that you can actually write an expression `5 * "x"`
# that will evaluate to "xxxxx". For the sake of the exercise you should
# ignore that the problem can be solved in this manner.)

# Done

symbol = str(input('Enter symbol: '))
number = int(input('Enter number: '))
app = ''

for i in range(number):
    app += symbol
print(app)