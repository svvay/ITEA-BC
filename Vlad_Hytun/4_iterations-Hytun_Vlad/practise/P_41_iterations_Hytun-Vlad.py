# 1. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

var = 0
while var < 7:
    if var in [3,6]:
        var += 1
        continue
    else:
        print(var)
    var += 1


for i in range(7):
    if i in [3,6]:
        i += 1
        continue
    else:
        print(i)
        i += 1
