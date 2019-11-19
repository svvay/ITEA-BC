import string

# 1 - input/output

First_name = input("Please intut your first name: ")
print(First_name)
Last_name = input("Please intut your last name: ")
print(Last_name)
E_mail = input("Please intut your e-mail: ")
print(E_mail)

temporary = 0

while temporary == 0:
    Age = input("Please input your Age: ")
    try:
        Age = int(Age)
        temporary = 1
    except Exception as e:
        print("You entered not numerical type! Try again please!")
print(Age)

Phone_number = input("Please intut your phone number: ")
print(Phone_number)

# 2 Check if phone number starts with
# Creating operators

Kyivstar = "Kyivstar"
Lifecell = "Lifecell"
MTS = "MTS"

try:
    Phone_number1 = int(Phone_number)
    if str(Phone_number).startswith("067") or str(Phone_number).startswith("097"):
        print(f'Your phone number belongs to {Kyivstar}')
    elif str(Phone_number).startswith("093") or str(Phone_number).startswith("063"):
        print(f'Your phone number belongs to {Lifecell}')
    elif str(Phone_number).startswith("050") or str(Phone_number).startswith("066"):
        print(f'Your phone number belongs to {MTS}')
    else:
        print("Your operator is not from Ukraine!")
except Exception as e:
    print("Error, you entered not numerical type (")

# 3 Trying to change variab type
try:
    Age = int(Age)
except ValueError as e:
    print("Error you entered not numerical type of age!")
    Age = None

# 4. Checking if First Name consists of letters

if string.ascii_letters not in Last_name :
    Last_name = "No name"

print(Last_name)

# 5. Creating var majority
majority = None

try:
    if Age < 18:
        majority = "minor"
    else:
        majority = "adult"
except Exception as e:
    print("You entered not numerical type!")
print(majority)
# 6 E-mail
Google = "google"
Apple = "apple"
if E_mail.endswith("gmail.com"):
    print(f"your e-mail provider is {Google}")
elif E_mail.endswith("icloud.com"):
    print(f"your e-mail provider is {Apple}")

print(f"First name - {First_name}")
print(f"Last name - {Last_name}")
print(f"e-mail - {E_mail}")
print(f"age - {Age}")
print(f"phone number - {Phone_number}")
