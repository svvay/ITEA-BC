#
#
# Animals: Think of at least three different animals that have a common characteristic.
#
#     Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#     Modify your program to print a statement about each animal, such as: A dog would make a great pet.
#     Add a line at the end of your program stating what these animals have in common.
#
# You could print a sentence such as Any of these animals would make a great pet!

# Done

animals = ['dog', 'cat', 'elephant', 'mouse']

charactesr = {
    'dog': 'best friend of people',
    'cat': 'one of the most popular home animals',
    'elephant': 'one of the biggest animals',
    'mouse': 'one of the smallest animals'
}

for animal in animals:
    print(f'The {animal} is a {charactesr[animal]}')
print(f'The common of all this animal is mammals, and any of these animals would make a great pet end even {animals[2]}!')

