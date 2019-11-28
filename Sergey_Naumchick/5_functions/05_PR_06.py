list = ["joho", "Andny", "Kate"]
list2 = ["john", "Anny", "Kaate"]



def overlapping(a, x):
    das = 0
    for i in a:

        for j in x:

            if j == i:
                das += 1
    if das != 0:
        return True
    else:
        return False


print(overlapping(list, list2))
