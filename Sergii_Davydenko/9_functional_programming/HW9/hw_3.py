# Create decorator which print the execution time of function.
# Use time or timeit module for it.

# Done

from timeit import default_timer as timer

def my_timer(time):
    def wrapper():
        start = timer()
        result = time
        print('Time is ', start - timer())
        return result
    return wrapper()

