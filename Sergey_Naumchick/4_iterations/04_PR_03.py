a = 0
my_list = []
while a != 1:
    my_input = input("Please inpit words without gep and blank lines: ")
    my_list.append(my_input)
    for ri in my_input:
        if ri == " ":
            a = 1
    if my_input == "":
        a = 1
print(my_list)
