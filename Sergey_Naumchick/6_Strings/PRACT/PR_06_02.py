'''2. Define a function `is_palindrome()` that recognizes
palindromes (i.e. words that look the same written backwards).
For example, `is_palindrome("radar")` should `return True`.'''

def is_palindrom(inp_word):
    inp_word = inp_word.lower()
    print(inp_word)
    if inp_word[::-1] == inp_word:
        print(f"{inp_word} is palindrom")
        return inp_word
