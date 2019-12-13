"""1. Order your favorite pizza:
    * Create 3-4 lists with pizza ingredients groups (vegetables, meat_types...).
    * Create list with predefined pizzas.
    * Ask user what pizza he want (custom or predefined).
    * Output variants of pizza or ingredient step by step
    * Return result of ordered pizza"""

vegetables = ["potatoes", "сuсumber", "tomatoes", "mushrooms"]
meat_types = ["pork", "beef", "veal", "goat"]
cheese_types = ["Roquefort", "Camembert", "Cheddar", "Feta"]

pizza_list = ["BBQ", "paperony", "gavai"]
x = True

while x == True:
    user_choise = (input("You want custom pizza or predefined? C/P")).upper()
    if user_choise == "P":
        for pizza_type in pizza_list:
            choice = (input(f"You want {pizza_type} pizza? y/n:")).upper()
            while choice != "Y" and choice != "N":
                print("Wrong! Try one more time!")
                choice = (input(f"You want {pizza_type} pizza? y/n:")).upper()
            if choice == "Y":
                print(f"Your order: {pizza_type} pizza")
                break

        break

        x = False
    if user_choise == "C":
        print("Please input what vegetables you want:")
        choosen_veget_list = []
        for vegetable in vegetables:
            veg = (input(f"You want to add {vegetable}? y/n")).upper()
            if veg == "Y":
                choosen_veget_list.append(vegetable)
            else:
                pass
        print("Please input what meet you want:")
        choosen_meet_list = []
        for meat in meat_types:
            met = (input(f"You want to add {meat}? y/n")).upper()
            if met == "Y":
                choosen_veget_list.append(meat)
            else:
                pass
        print("Please input what cheese you want:")
        choosen_cheese_list = []
        for cheese in cheese_types:
            chee = (input(f"You want to add {meat}? y/n")).upper()
            if chee == "Y":
                choosen_cheese_list.append(cheese)
            else:
                pass

        x = False
        print("Your pizza ingradient choice: ")

        for i in choosen_veget_list:
            print(i)

        for i in choosen_meet_list:
            print(i)

        for i in choosen_cheese_list:
            print(i)
    else:
        print("Wrong choice")
