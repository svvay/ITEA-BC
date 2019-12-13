'''3. Create decorator which print the execution time of function.
Use time or timeit module for it.'''

import time


def execution_time_funk(funk):
    def wrapper():
        now = time.time()
        print(now)
        funk()

        print(time.time() - now)

    return wrapper()


@execution_time_funk
def making_cicle():
    for number in range(1000000):
        print(number)
