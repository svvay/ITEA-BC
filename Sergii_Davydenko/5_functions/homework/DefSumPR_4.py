# 4. Define a function `sum()` and a function `multiply()` that
# sums and multiplies (respectively) all the numbers in a list
# of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
# and `multiply([1, 2, 3, 4])` should return `24`.

# Work only sum ore multiply .. Why?

# numb = [int(item) for item in map(int, input("Enter numbers: ").split())]
#
# lenght = len(numb)
# q = 1


def sums(numb, lenght, q):
    for i in range(lenght):
        numb[0] += numb[q]
        q += 1
        if q == lenght:
            break
    # print(f'The sum is {numb[0]}')
    return numb[0]


# sums(numb, lenght, q)
# sums()
