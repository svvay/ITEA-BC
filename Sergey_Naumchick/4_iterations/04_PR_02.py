my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i <= len(my_list):

    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1
