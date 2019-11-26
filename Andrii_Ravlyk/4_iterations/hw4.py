# HW

#1. Write a Python program that accepts a string
#and calculate the number of digits and letters.
c_dig = 0
c_alpha = 0
str1 = input ("Please insert a string with numbers= ")
for i in str1:
    if i.isdigit():
        c_dig = c_dig +1
    elif i.isalpha():
        c_alpha = c_alpha +1
print (f"c_dig = {c_dig},  c_alpha = {c_alpha}")

#2. Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number
#and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(51):
  if i % 3 == 0 and i % 5 == 0:
      print ("FizzBuzz")
  elif i % 3 == 0:
      print("Fizz")
  elif i % 5 == 0:
      print("Buzz")
  else:
      print(str(i))
pass