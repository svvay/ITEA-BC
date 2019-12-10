#
#
# Person:
#
#     Use a dictionary to store information about a person you know.
#     Store their first name, last name, age, and the city in which they live.
#     You should have keys such as first_name, last_name, age, and city.
#     Print each piece of information stored in your dictionary.
#

# Done

persons = {
    'first_name': 'Slava',
    'last name': 'Samson',
    'age': '21',
    'city': 'Kiev',
}

for person in persons:
    print(f'The {person}: {persons[person]}')

