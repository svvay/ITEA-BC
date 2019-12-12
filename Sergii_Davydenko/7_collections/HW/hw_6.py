#
#
# Pets: Make several dictionaries, where the name of each dictionary is the name of a pet.
#
#     In each dictionary, include the kind of animal and the owner’s name.
#     Store these dictionaries in a list called pets.
#     Next, loop through your list and as you do print everything you know about each pet.
#
# DONE


chappy = {
    'name': 'Chappy',
    'kind': 'robot',
    'owners': 'Sophi',
}

tom = {
    'name': 'Tom',
    'kind': 'yard cat',
    'owners': 'Lina',
}

keks = {
    'name': 'Keks',
    'kind': 'toyteryer',
    'owners': 'Sveta',
}

pets = [chappy, tom, keks]

for pet in pets:
    print(f'We know about {pet["name"]}')
    for key, value in pet.items():
        print(f'{key} : {value}')




