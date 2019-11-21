a = list()
i = 0
while i < 7:
    if i != 3 and i != 6:
        a.append(i)
        i += 1
    else:
        i += 1
        continue
print(*a, sep = " ")

# #1. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# #Note : Use 'continue' statement
# #Expected Output : 0 1 2 4 5

b = list()
my_numbers = {1, 2, 3, 4, 5, 6}
i = 0
for i in my_numbers:
    if i != 3 and i != 6:
        b.append(i)
        i += 1
    else:
        i += 1
        continue
print(*a, sep = " ")
