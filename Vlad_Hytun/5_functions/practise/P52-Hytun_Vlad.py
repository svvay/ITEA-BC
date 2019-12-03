# 2. Define a function that computes the length of a
# given list or string. (It is true that Python has
# the len() function built in, but writing it yourself
# is nevertheless a good exercise.)

def  my_len(str):
    count_symbol = 0
    for i in str:
        count_symbol += 1
    return count_symbol

print(my_len('djfkdflk'))