'''2. Define a function that computes the length of a
given list or string. (It is true that Python has
the len() function built in, but writing it yourself
is nevertheless a good exercise.)'''
while True:

    question_1 = input("Do you want to input string? y/n: ")
    if question_1 == 'y':
        question_2 = 'n'
        break
    elif question_1 == 'n':
        break
    else:
        print("Please input only y/n letters")
if question_1 == 'n':
    while True:
        question_2 = input("Maybe you want to input list? y/n:")
        if question_2 == 'y':
            break
        elif question_2 == 'n':
            break
        else:
            print("Please input only y/n letters")


def string_len(a, temp=0):
    for i in a:
        temp += 1
    return print(temp)


if question_1 == "y":
    string_input = input("input String: ")
    string_len(string_input)


def list_len(a, temp=0):
    for i in a:
        temp += 1
    return print(temp)


if question_2 == "y":
    list_input = input("please input list splits by ' ':").split(' ')
    list_len(list_input)
