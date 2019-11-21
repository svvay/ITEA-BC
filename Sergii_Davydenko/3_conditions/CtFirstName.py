# # # Check that First Name consist of letters (string.ascii_letters) else set "No name"


first_name = input('Enter first name: ')
big = first_name[0]
if big.isupper():
    print(f'Your name is: {first_name}')
else:
    print('No name:')

