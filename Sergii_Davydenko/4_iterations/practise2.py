# Write a Python program to count the number of even
# and odd numbers from a series of numbers.

number = int(input('Make your choice number: '))

even = 0
odd = 0

for i in range(number):
    if i % 2 == 0:
        even += 1
    elif i % 2 != 0:
        odd += 1

print(f'The odd numbers is {odd}')
print(f'The even numbers is {even}')
