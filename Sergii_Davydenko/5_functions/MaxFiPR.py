# 1. Define a function `max()` that takes two numbers as arguments
# and returns the largest of them. Use the if-then-else construct
# available in Python. (It is true that Python has the `max()` function
# built in, but writing it yourself is nevertheless a good exercise.)"""

# All done

firstnumb = int(input('Enter first number: '))
secnumb = int(input('Enter second number: '))

def maxi(firstnumb, secnumb):
    if firstnumb > secnumb:
        print(f'The biggest is: {firstnumb}')
    elif secnumb > firstnumb:
        print(f'The biggest is: {secnumb}')
    elif firstnumb == secnumb:
        print(f'Its awesome {firstnumb} = {secnumb}')

maxi(firstnumb, secnumb)
