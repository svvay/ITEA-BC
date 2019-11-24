
'''5. Write a function `is_member ()` that takes a value
i.e. a number, string, etc) x and a list of values ​​a,
and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the `in` operator does, but
for the sake of the exercise you should pretend Python
did not have this operator.)'''
string = "s"
list = ["a", "s", "d", "f", "g"]

if string in list:
    print ("ok")

def is_member(x, a):
    temp_1 = 0
    while temp_1 < len(x):
        temp_2 = 0
        while temp_2 < len(a):
            if a[temp_2] == x[temp_1]:
                print("Yes")
            temp_2 += 1

        temp_1 += 1

is_member(string,list)
