'''2. Create a function that generate 10 random numbers from 1 to 100.
Call this functions 100 times and append each result of function to file.'''
import random


def randomiser():
    rand_string = ""

    for i in range(10):
        rand_string += f"{random.randint(1, 100)} "
    return rand_string


with open("../Text_Files/PR_02_result.txt", "w+") as file:
    for i in range(100):
        file.write(f"{randomiser()}\n")
