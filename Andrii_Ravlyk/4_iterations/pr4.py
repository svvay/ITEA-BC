# Practise

# 1. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
res=''
for i in range (7):
    if i not in (3 , 6):
        res = res + ' ' + str(i)
print((res.strip()))
print("=========2========")
# 2. Write a Python program to count the number of even
# and odd numbers from a series of numbers.
cnum = input("Please input count numbers =")
even = 0
odd = 0
for i in range(1, int(cnum)):
    if i % 2 == 0:
        even = even +1
    else:
        odd = odd + 1
print(f"even = {even}, odd = {odd}")
print("=========3========")
# 3. Write a Python program that accepts a sequence of lines (blank line to terminate) as input
# and prints the lines as output (all characters in lower case).
str = []
blank = ""
while blank == "":
    str_inp = input("Please input, blank line to terminate =")
    if str_inp != " ":
        str.append(str_inp)
    else:
        break
print (*str, sep="" )
