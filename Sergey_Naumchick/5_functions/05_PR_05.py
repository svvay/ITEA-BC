
'''5. Write a function `is_member ()` that takes a value
i.e. a number, string, etc) x and a list of values ​​a,
and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the `in` operator does, but
for the sake of the exercise you should pretend Python
did not have this operator.)'''
string = "a"
list = ["a", "s", "d", "f", "g"]


def is_member(x, a):
    for i in x:
        for j in a:
            if j == i:
                return True




if (is_member(string,list))==True:
    print("Yes")
else:print("No")
