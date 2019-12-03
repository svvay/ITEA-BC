menu = ("pizza", "apple", "burger", "soup", "pancake")
new_dishes = ["fish", "dog"]


def new_menu(old_menu, new_dish_list):
    new_menu = []
    for dish in old_menu:
        if dish != "pizza" and dish != "soup":
            new_menu.append(dish)
    for dish in new_dish_list:
        new_menu.append(dish)

    print(tuple(new_menu))
    print(tuple(new_menu[len(new_menu) - 2:len(new_menu)]))
    print(tuple(new_menu[::2]))
    print(tuple(new_menu[::-1]))


new_menu(menu, new_dishes)
