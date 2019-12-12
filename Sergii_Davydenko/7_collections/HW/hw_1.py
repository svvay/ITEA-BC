

#
# Order your favorite pizza:
#
#     Create 3-4 lists with pizza ingredients groups (vegetables, meat_types...).
#     Create list with predefined pizzas.
#     Ask user what pizza he want (custom or predefined).
#     Output variants of pizza or ingredient step by step
#     Return result of ordered pizza


choice = 0
while choice != 'finish':
    try:

        variant = input('Enter what pizza u want, custom ore predefined: ').lower()
        while variant == 'custom':
            # make a selection by ingredients on lower register
            custom_choice = input('What ingredients of pizza u want?: ').lower().split()

            print(f'Thanks for your choice, its right order {custom_choice}')
            unswer = input('Yes ore No: ').lower()
            while unswer == 'yes':
                print('Okkey, waits yours order ')
                choice = 'finish'
                break
            else:
                print('U want change u order? ')
                ch_order = input('Yes ore No: ').lower()
                if ch_order == 'yes':
                    break # return to choice pizza
                else:
                    print('Okkey, waits yours order ')
                    choice = 'finish'
                    break # must stop programm


        while variant == 'predefined':
            pizzas = {
                'vegetariana': 'Sous, royal cheese, tomatoes, corn, broccoli, green peppers, oregano',
                'meat': 'chicken meat, onion, cheese, souse',
                'mix': 'all we have will be on your pizza',
                'paperoni': 'paperoni, cheese, hot souse and tomatos',
                'four cheese': 'Sous, royal cheese, mozzarella, parmesan, feta and gorgonzola',
                'margherita': 'mozzarella cheese, fresh basil, salt and olive oil',
                'diablo': 'Salami, tomato sauce, sweet pepper and chilli',
            }
            print(f'We have some of this predefined pizzas: \n {list(pizzas.keys())}',)
            # make a selection by ingredients on lower register
            custom_choice = input('What pizzas u want?: ').lower()

            if custom_choice in pizzas:
                print(f'U want {custom_choice} pizzas, right?, \n The ingredients of pizza is {pizzas[custom_choice]}')
                unswer = input('Yes ore No: ').lower()
                if unswer == 'yes':
                    print(f'Okey, wait yours {custom_choice} pizzas')
                    choice = 'finish'
                    break
                else:
                    break
            else:
                break

    except TypeError:
        print('Try later')
