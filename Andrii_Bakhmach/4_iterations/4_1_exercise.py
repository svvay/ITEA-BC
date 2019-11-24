
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.

digit = 0
while digit <= 6:
    if digit != 3 and digit != 6:
        print(digit)
    digit += 1
    continue
