'''4. Define a function `sum()` and a function `multiply()` that
sums and multiplies (respectively) all the numbers in a list
of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
and `multiply([1, 2, 3, 4])` should return `24`.'''

my_list = []
TEMP = 0

# Making cicle for inputing dict and
while TEMP == 0:
    my_list = (input("please input numbers :")).split(" ")
    print(my_list)
    i = 1
    while i < len(my_list):
        try:
            my_list[i] != None
            my_list[i] = int(my_list[i])

            TEMP = 1
        except Exception as e:
            print("You make mistake! Please input just numbers!!!")
        break


'''def sum(n_value, a=0):

    for i in n_value:
        a += int(i)
    print(a)'''

def sum(n_value, temp=0):
    for i in range(len(my_list)):
        temp += int(my_list[i])
    return print(temp)


def multiply(n_value, temp=1):
    for i in range(len(my_list)):
        temp *= int(my_list[i])
    return print(temp)


sum(my_list)
multiply(my_list)
