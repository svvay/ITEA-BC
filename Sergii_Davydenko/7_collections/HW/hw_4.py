#
#
# Favorite Numbers:
#
#     Use a dictionary to store people’s favorite numbers. # Done
#     Think of five names, and use them as keys in your dictionary. # DOne
#     Think of a favorite number for each person, and store each as a value in your dictionary.
#     Print each person’s name and their favorite number.
#     For even more fun, poll a few friends and get some actual data for your program.
#

# DOne

favorite_numbers = {
    'Sophi': '1',
    'John': '2',
    'Sonia': '3',
    'Bob': '4',
    'Mira': '5',
}
for number in favorite_numbers:
    print(f'The favorite number of {number} is {favorite_numbers[number]}')
