# Practise

# 1. Use input/output for get:
#
#     * First Name
#     * Last Name
#     * Email
#     * Age
#     * Phone number

fname= input("Please, input your first name: ")
lname = input ("Please, input your last name: ")
email = input("Please, input your email: ")
age = input ("Please, input your age: ")
phone_number = input ("Please, input your phone number: ")

# 2. If phone number starts from (097, 067) output "Your phone number belongs to
# {}" and create variable operator with value.

code: str = phone_number[0:3]
dict ={"097": "Kyivstar", "067": "Kyivstar", "063": "Life", "073": "Life"}
if phone_number :
    print("Your phone number belongs to", dict[code])

# 3. Try to change age from str to int and catch Exception (ValueError),
# set age None in else case

try:
    age = int(age)
    age = age/0
except ValueError as e:
    print(e)
else:
    print("In Else case")
finally:
    print(age)
pass

# 4. Check that First Name consist of letters (string.ascii_letters)
# else set "No name"

import string
try:
    fname in string.ascii_letters
except Exception as error:
else: fname = "No name"
print("Incorrect input! Please use letters for name")
print("Your name is:", fname)

# 5. Create variable majority and set 'minor' if age less than 18, in
# other case set 'adult'

if age < 18:
    majority = "minor"
else: majority = "adult"
print (f"Your First Name is {fname}, Your majority is {majority}")

# 6. If email endswith gmail.com, icloud.com…make output ”Your email provider is {}”
# Use output for print: First Name, Majority

providers = {"gmail.com": "Google", "icloud.com": "Apple"}
if email.endswith("gmail.com"):
    company = "Google"
if email.endswith("icloud.com"):
    company = "Apple"
print("Your E-mail provider is", providers[company])



