# 3. Write a function that takes a character (i.e. a
# string of length 1) and returns True if it is a vowel,
# False otherwise.

# Done

tryes = (input('enter something string: ')).upper()


def func(tryes):
    vowels_string = ['A', 'E', 'I', 'O', 'U', 'Y']
    if tryes in vowels_string:
        return print(f'{tryes}, True vowel character')
    else:
        return print('Sorry, try again later')


func(tryes)