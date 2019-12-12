# Create lambda functions that calculate pow, sum, and multiply.

# Done

from functools import reduce

# sum numbers

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))

# multiply

print(reduce(lambda x, y: x * y, [2, 3, 4]))
print(reduce(lambda x, y: x * y, list(map(int, input('Something numbers: ').split()))))

# powe

print(reduce(lambda x, y: x ** y, [2, 3]))



