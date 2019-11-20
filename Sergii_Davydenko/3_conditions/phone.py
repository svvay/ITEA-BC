# # # Use input/output for get:
# # # If phone number starts from (097, 067) output "Your phone number belongs to {}" and create variable operator with value.


phone_number = str(input("Enter your number: ").split())
code = {
    '098': 'Kyivstar',
    '093': 'Life',
    '063': 'Life2',
    '067': 'Kyivstar2'
}

a = (phone_number[2:5])
b = len(phone_number)

if b == 14:
    if a in code:
        print(f'Your phone number belongs to {a}, it is {code[a]}')
    else:
        print('Something wrong')
else:
    print("Try again latter")
