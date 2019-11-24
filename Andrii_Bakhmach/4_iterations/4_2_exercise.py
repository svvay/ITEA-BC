#Write a Python program to count the number of even
#and odd numbers from a series of numbers.

my_list = [1, 2, 3, 5, 6, 7, 7, 7, 8, 3, 3, 3, 5, 5, 67, 832]
even = 0
odd = 0

for i in my_list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'The have {even} even numbers')
print(f'You have {odd} odd numbers')

