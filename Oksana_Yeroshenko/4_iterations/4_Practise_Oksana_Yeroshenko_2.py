import random
b = []
i = 0

while i < 10:
    a = random.randint(0,3000)
    b.append(a)
    i += 1
print(b)
my_odd = 0
my_even = 0
for c in b:
    if c % 2 > 0:
        my_odd +=1
    else:
        my_even +=1
print("Quantity of odd numbers = ", my_odd)
print("Quantity of even numbers = ", my_even)
