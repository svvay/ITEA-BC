# raiting = 0
# lbrand = 'pontiak'
# lmodel = 'airbus'
# lcolor = 'brown'
#
#
# # # # Check that brand (model, color) not in your favourite, print brand name, and in finally clause print your favourite.
#
#
# brand = input('Enter brand: ')
# model = input('Enter model: ')
# color = input('Enter color: ')
#
# if brand == lbrand or model == lmodel or color == lcolor:
#     print(f"Wow, i like this {lbrand} and {lmodel} and {lcolor} to")
# else:
#     print(f"Sorry, i'd like this brand, my favorite brand is {lbrand}, model {lmodel}, color {lcolor}")
# raiting += 1
#
#
# # ### Try to change year type to int and catch exception, else print year and finally decrease year by 1 and print
#
#
# year = input('Enter year: ')
#
# try:
#     print('You have so old car: ', int(year))
# except Exception as e:
#     print('The except is: ', e)
#     year = 10
#     print('You car so old: ', year - 1)
# raiting += 1
#
#
# # ### Change Engine volume type to float and add 0.1 to value (print to user), (use try, except, else)
#
#
# engine_volume = input('Enter engine: ')
# try:
#     float_eng_volume = float(engine_volume) + 0.1
#     print(float_eng_volume)
# except ValueError as e:
#     print('U have a problem with: ', e)
# raiting += 1
#
#
# # ### Измените тип одометра на int, чтобы проверить, что значение одометра меньше 1000, больше 50000, больше или равно 100000, и установите другое значение для рейтинга.
#
#
# try:
#     odometer = int(input('Enter odometer: '))
#
#     if odometer < 1000:
#         print(f'Good rate: {odometer}')
#     elif odometer > 50000:
#         print(f'Not bad rate: {odometer}')
#     elif odometer > 100000:
#         print(f'Иad rate: {odometer}')
# except Exception as e:
#     print('You enter fault information, try more next time: ')
#
# raiting += 1
#
#
# # ### Get final rating for your car by your criterion (3-4 if cases)
#
#
# print(f'Now raiting car is {raiting}')
#
#
# # ## Input: credit card number (fake data), cvv, mm/yy
#
#
# card_date, card_month = map(int, input("Enter date mm/yy: ").split())
# card_number = len(input('Enter number: '))
# card_cvv = len(input('Enter cvv card: '))
#
# if card_number == 16:
#     if card_cvv == 3:
#         print('All is good')
#     else:
#         exit('Sorry but your card cvv is wrong')
# else:
#     exit('Sorry but your card number is wrong')
# print(card_date,'/', card_month)
#
#
# # # Practise
# # # Use input/output for get:
# # # If phone number starts from (097, 067) output "Your phone number belongs to {}" and create variable operator with value.

#
# phone_number = str(input("Enter your number: ").split())
# code = {
#     '098': 'Kyivstar',
#     '093': 'Life',
#     '063': 'Life2',
#     '067': 'Kyivstar2'
# }
# a = (phone_number[2:5])
# b = len(phone_number)
#
# if b == 14:
#     if a in code:
#         print(f'Your phone number belongs to {a}, it is {code[a]}')
#     else:
#         print('Something wrong')
# else:
#     print("Try again latter")


# # #
# # # Try to change age from str to int and catch Exception (ValueError), set age None in else case
#
# # try:
# #     age = int(input('Enter your age: '))
# #     print(f'your age is: {age}')
# # except Exception as e:
# #     age = None
# #     print(f"Your age is {age} for me")
#
#
# # # Check that First Name consist of letters (string.ascii_letters) else set "No name"
#
# #
# # first_name = input('Enter first name: ')
# # big = first_name[0]
# # if big.isupper():
# #     print(f'Your name is: {first_name}')
# # else:
# #     print('No name:')
#
#
# # # Create variable majority and set 'minor' if age less than 18, in other case set 'adult'
#
#
# # try:
# #     age = int(input("Enter your age: "))
# #     if age >= 18:
# #         print('You are adult')
# #     else:
# #         print('You are minor, goodbye')
# # except Exception as e:
# #     print(e)
# #     print('Try again later')
#
#
# # # If email endswith gmail.com, icloud.com…�make output ”Your email provider is {}” Use output for print: First Name,
#
# #
# # all_email = {
# #     'mozilla.com': 'Mozilla',
# #     'ukr.net': 'Ukrnet',
# #     'google.com': 'Google',
# #     'icloud.com': 'Apple'
# # }
# #
# # mail = input('Enter email please: ')
# # if mail in all_email:
# #     print('Your provider is: ', all_email[mail])
# # else:
# #     print('i haven"t this mail')
#
#
# # # Output result of each variable
#
#
