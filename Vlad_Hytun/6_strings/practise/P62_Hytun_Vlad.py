# 2. Define a function `is_palindrome()` that recognizes
# palindromes (i.e. words that look the same written backwards).
# For example, `is_palindrome("radar")` should `return True`.


def is_palindrome(my_str):
    result = ''
    for i in range(len(my_str)//2):
        if my_str[i] != my_str[-1-i]:
            result = 'False'
        else:
            result = 'True'
    print(f'{my_str} are palindrome?: {result}')

is_palindrome('radar')