# Define a function that computes the length of a
# given list or string. (It is true that Python has
# the len() function built in, but writing it yourself
# is nevertheless a good exercise.)

my_list= []
while True:
    a = input("Input item of list: ")
    if a == "" or a == " ": #question!
        break
    else:
        my_list.append(a)

def lenth_of_list(my_list):
    x_len = 0
    for i in my_list:
        x_len += 1
    return x_len