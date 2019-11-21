a = []
a_name = str
while a_name:
    a_name = input("Input your name, please: ")
    if len(a_name) != 0:
        a.append(a_name.lower())
    else:
        break

for item in a:
    print(item)
