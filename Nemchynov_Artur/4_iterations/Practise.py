my_list = [0, 1, 2, 3, 4, 5, 6]
for item in my_list:
    if item == 6:
        break
    elif item == 3:
        continue
    print(item, type(item))
pass

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
pass

lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)
pass
