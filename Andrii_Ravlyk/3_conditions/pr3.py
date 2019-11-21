# Practise

# 1. Use input/output for get:
#   * First Name
#   * Last Name
#   * Email
#   * Age
#   * Phone number

first_name = input("Type your first name: ")
last_name = input("Type your last name: ")
email = input("Type your emai: ")
age = input("Type your age: ")
phone_number = input("Type your phone number: ")

print ("==============Resut=============\n")

# 2. If phone number starts from (097, 067) output "Your phone number belongs to
mob_oper = ['097', '067']
mob_prefix = phone_number[0:3]
if  mob_prefix in  mob_oper:
    mes1= f"Your phone number belongs {mob_prefix}"
    print(mes1)
# 3. Try to change age from str to int and catch Exception (ValueError),
# set age None in else case
try:
    age=int(age)
except ValueError:
    print ("Please insert numbers for age")
else:
    age = None
    print ("age = ", age)
#4. Check that First Name consist of letters (string.ascii_letters)
# else set "No name"
import string

if first_name not in string.ascii_letters:
    first_name = "No name"
print("first_name = ", first_name)

# 5. Create variable majority and set 'minor' if age less than 18, in
# other case set 'adult'
majority =''
if age<18:
    majority = "minor"
else:
    majority = "adult"
print ("majority = ", majority)

pass
