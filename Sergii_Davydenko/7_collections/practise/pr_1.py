#
#
# Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza
# names in a list, and then use a for loop to print the name of each pizza.
#
#     Modify your for loop to print a sentence using the name of the pizza
#     instead of printing just the name of the pizza. For each pizza you should
#     have one line of output containing a simple statement like: I like pepperoni pizza.
#     Add a line at the end of your program, outside the for loop, that states
#     how much you like pizza. The output should consist of three or more lines
#     about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
#
# pizzas = {
#     'vegetariana': 'Sous, royal cheese, tomatoes, corn, broccoli, green peppers, oregano',
#     'margherita': 'mozzarella cheese, fresh basil, salt and olive oil',
#     'diablo': 'Salami, tomato sauce, sweet pepper and chilli',
# }
#
# vegetariana = 'Sous, royal cheese, tomatoes, corn, broccoli, green peppers, oregano'
# margherita = 'mozzarella cheese, fresh basil, salt and olive oil'
# diablo = 'Salami, tomato sauce, sweet pepper and chilli'

favorite_pizza = ['vegetariana', 'margherita', 'diablo']



for pizz in favorite_pizza:
    print(pizz)
print(f'Im so much love {favorite_pizza[2]} pizza')


