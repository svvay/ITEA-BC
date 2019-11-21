# # If email endswith gmail.com, icloud.com…�make output ”Your email provider is {}” Use output for print: First Name,


all_email = {
    'mozilla.com': 'Mozilla',
    'ukr.net': 'Ukrnet',
    'google.com': 'Google',
    'icloud.com': 'Apple'
}

mail = input('Enter email please: ')
if mail in all_email:
    print('Your provider is: ', all_email[mail])
else:
    print('i haven"t this mail')