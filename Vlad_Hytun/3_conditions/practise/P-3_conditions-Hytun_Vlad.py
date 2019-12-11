# 1. Use input/output for get:
#
#     * First Name
#     * Last Name
#     * Email
#     * Age
#     * Phone number

my_operator = ''
phone_operators = {'097': 'Kyivstar',
                   '093': 'Life'}
email_provider = {'gmail.com': 'Google',
                  'icloud.com': 'Apple'}
my_first_name = input('Enter your first name: ')
my_last_name = input('Enter your last name: ')
my_email_provider = input('Enter your email_provider name: ')
my_age = input('Enter your age name: ')
my_phone = input('Enter your phone name: ')

# 2. If phone number starts from (097, 067) output "Your phone number belongs to
# {}" and create variable operator with value.

oper:  str = my_phone[0:3]
if oper in phone_operators.keys():
    operators = phone_operators[oper]

# 4. Check that First Name consist of letters (string.ascii_letters)
# else set "No name"
import string

if my_first_name not in string.ascii_letters:
    my_first_name = "No name"

# 3. Try to change age from str to int and catch Exception (ValueError),
# set age None in else case
try:
    my_age == int(my_age)
except ValueError as e:
    my_age = None
# 5. Create variable majority and set 'minor' if age less than 18, in
# other case set 'adult'
if int(my_age) < 18:
    majority = 'minor'
else:
    majority = 'adult'
# 6. If email endswith gmail.com, icloud.com…make output ”Your email provider is {}”

if my_email_provider in email_provider.keys():
    my_email_prov = email_provider[my_email_provider]

# Use output for print: First Name, Majority
# 7. Output result of each variable
print(f'You are {my_first_name},{majority} and has old {my_age}. You have Phone operators as {operators} and Email '
      f'operator {my_email_prov}.')
