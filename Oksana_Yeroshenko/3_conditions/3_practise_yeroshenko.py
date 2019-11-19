first_name = input("Enter your first name, please ")
last_name = input("Enter your surname, please ")
email = input("Enter your E-mail, please ")
age: str = input("Enter your age, please ")
phone_num = input("Enter your phone number, please ")

code_operator: str = phone_num[0:3]
dict = {"097": "Kyivstar", "067": "Kyivstar", "098": "Kyivstar", "068": "Kyivstar", "050": "MTC", "095": "MTC", "099": "MTC", "063": "Life", "093": "Life"}
if code_operator in dict.keys():
    print("Your phone number belongs to", dict[code_operator])

try:
    age = int(age)
except Exception as error:
    print("Incorrect input! Please use numbers for age")
else: age = None
print("Your age = ", age)

import string
try:
    first_name in string.ascii_letters
except Exception as error:
else: first_name = "No name"
print("Incorrect input! Please use letters for name")
print("Your name is:", first_name)

if age < 18:
    majority = "minor"
else: majority = "adult"
print(f"Your First Name is {first_name}, Your majority is {majority}")

providers = {"gmail.com": "Google", "icloud.com": "Apple"}
if email.endswith("gmail.com"):
    service = "gmail.com"
if email.endswith("icloud.com"):
    service = "icloud.com"
print("Your E-mail provider is", providers[service])