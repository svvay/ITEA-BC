import string

first_name = input("Enter your first name: ")
second_name = input("Enter you second name: ")
email = input("Enter your e-mail address: ")
age = int(input("Enter your age:"))
phone = input("Enter your phone number: ")
operator_code = str(phone[0:3])
if operator_code is "063" or "097":
    print("Your phone is serviced by Kievstar")
elif operator_code is "050" or "095":
    print("Your phone is serviced by MTS")
elif operator_code is "067":
    print("Your phone is serviced by Life")
else:
    print("You phone is serviced by international operator")


try:
    age = int(age)
except ValueError:
    age = None

if first_name not in string.ascii_letters:
    first_name = "No name"

if age < 18:
    majority = "minor"
else:
    majority = "adult"

email_provider = {"gmail.com": "Google", "icloud.com": "Apple"}
if email.endswith("gmail.com"):
    provider = "gmail.com"
elif email.endswith("icloud.com"):
    provider = "icloud.com"
print("Your e-mail provider is", email_provider[provider])

print("Your mayourity is:", majority)
print("Your age is:", age)
print("Your first name is: ", first_name)











