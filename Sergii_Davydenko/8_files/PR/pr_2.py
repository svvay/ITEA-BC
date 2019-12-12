# Create a function that generate 10 random numbers from 1 to 100.
# Call this functions 100 times and append each result of function to file.

# Done

import random


def sto ():
    zero = 10
    rand_numb = []
    while zero != 0:
        pop = open('random.txt', 'w')
        pop.write(str(rand_numb))
        pop.close()
        zero -= 1
        rand_numb.append(random.randint(0, 100))
    return rand_numb

if __name__ == '__main__':
    print(sto())

