'''4. Define a function `sum()` and a function `multiply()` that
sums and multiplies (respectively) all the numbers in a list
of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
and `multiply([1, 2, 3, 4])` should return `24`.'''

my_list = []
TEMP = 0

# Making cicle for inputing dict and
my_list = (input("please input numbers :")).split(" ")
print(my_list)


for i in my_list:
    try:
        my_list[i]!=None
        my_list[i] = int(my_list[i])


    except Exception as e:
        print("You make mistake! Please input just numbers!!!")
    break



def my_sum(n_value, temp=0):
    for i in n_value:
        temp += int(i)
    return print(temp)


def multiply(n_value, temp=1):
    for i in n_value:
        temp *= int(i)
    return print(temp)


my_sum(my_list)
multiply(my_list)
