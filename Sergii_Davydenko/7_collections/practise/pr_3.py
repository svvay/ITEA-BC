#
#
# Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
#
#     Use a for loop to print each food the restaurant offers.
#     Try to modify one of the items, and make sure that Python rejects the change.
#     The restaurant changes its menu, replacing two of the items with different foods.
#     Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
#     Use slicing for get last two items of foods.
#     Use slicing for get every second item of food.
#     Reverse your food order.
#

# Done

buffet_style = ('meat', 'fish', 'potatoes', 'pizza', 'dessert')

for dishes in buffet_style:
    print(f'{dishes}')

########################################################
# Try to modify

# buffet_style[1] = ('sea fish')
# print(buffet_style)

#########################################################
# changes menu

new_menu = list(buffet_style)
new_menu[0] = 'chicken', 'makarones'
print(tuple(new_menu))

#########################################################
# rewrites the tuple

buffet_style = new_menu
print('New menu', buffet_style)

for menu in buffet_style:
    print('New menu Done', menu)

#########################################################
# Use slicing

print(buffet_style[-2:])

#########################################################
# Reverse your food order

print(buffet_style[::-1])


