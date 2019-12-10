#
#
# My Pizzas, Your Pizzas: Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
#
#     Add a new pizza to the original list. ########## Done
#     Add a different pizza to the list friend_pizzas. ######### Done
#     Prove that you have two separate lists.
#
#     Print the message, My favorite pizzas are:, and then use a for
#     loop to print the first list. ## Done
#
#     Print the message, My friend’s favorite pizzas are:, and then use a
#     for loop to print the second list. Make sure each new pizza is stored
#     in the appropriate list.
#

# Done, maybe

friend_pizzas = {
    'mix': 'all we have will be on your pizza',
    'paperoni': 'paperoni, cheese, hot souse and tomatos',
    'diablo': 'Salami, tomato sauce, sweet pepper and chilli',
}

pizzas = {
    'mix': 'all we have will be on your pizza',
    'paperoni': 'paperoni, cheese, hot souse and tomatos',
    'diablo': 'Salami, tomato sauce, sweet pepper and chilli',
}
pizzas['four friends'] = 'Tomato sauce, mozzarella, bacon, hunting sausages, bogarsky pepper'
friend_pizzas['BBQ'] = 'BBQ sauce, mozzarella cheese, bacon, hunting sausages, smoked chicken'

print('Pizza friend_pizzas', friend_pizzas)
print('Pizza pizzas', pizzas)


for pizza in pizzas:
    # favorite = input('Enter favorite pizzas: ').lower()
    # if favorite in pizzas:
        print(f'My friend’s favorite pizzas are - {pizza.title()}, ' f'the ingredients is {pizzas[pizza]}.')
    #     break
    # else:
    #     print('Sorry ))')

for pizza in friend_pizzas:
    # favorite = input('Enter favorite pizzas my friends: ').lower()
    # if favorite in friend_pizzas:
        print(f'My favorite is - {pizza.title()} pizza, ' f'the ingredients is {friend_pizzas[pizza]}.')
    #     break
    # else:
    #     print('Sorry ))')