# 2. Define a function `is_palindrome()` that recognizes
# palindromes (i.e. words that look the same written backwards).
# For example, `is_palindrome("radar")` should `return True`.

# Work

# words = input('Try something enter: ')

def palindrom(words):
    back = words[::-1]
    if words == back:
        return True
    return False

# print(palindrom(words))
