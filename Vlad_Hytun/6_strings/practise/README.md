# Practise

* Write test with 3-4 cases for each exercise

1. Define a function `generate_n_chars()` that takes an 
integer n and a character c and returns a string, n 
characters long, consisting only of c:s. For example, 
`generate_n_chars(5,"x")` should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression `5 * "x"` 
that will evaluate to "xxxxx". For the sake of the exercise you should 
ignore that the problem can be solved in this manner.)

2. Define a function `is_palindrome()` that recognizes 
palindromes (i.e. words that look the same written backwards). 
For example, `is_palindrome("radar")` should `return True`.

3. Define a function `overlapping()` that takes two lists and 
returns True if they have at least one member in common, 
False otherwise. You may use your `is_member()` function, 
or the in operator, but for the sake of the exercise, 
you should (also) write it using two nested for-loops.

    `string = AV is largest Analytics community of India`
4. Return first word from string.
result: `AV`

5. Return last word from string.
result: `India`

6. Get two symbols of each word in string
result: `['AV', 'is', 'la', 'An', 'co', 'of', 'In']`

    `string = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'`
7. Get date from string