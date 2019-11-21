my_list = [0, 1, 2, 3, 4, 5, 6]
for item in my_list:
    if item == 6:
        break
    elif item == 3:
        continue
    print(item, type(item))
pass
