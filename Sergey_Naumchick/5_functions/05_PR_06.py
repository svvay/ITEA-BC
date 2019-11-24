list = ["joho", "Anny", "Kate"]
list2 = ["john", "Anny", "Kaate"]

a = 0


def overlapping(a, x):
    das = 0
    for i in range(len(list)):

        for j in range(len(list2)):

            if list2[j] == list[i]:
                das += 1
    if das != 0:
        return True
    else:
        return False


print(overlapping(list, list2))
