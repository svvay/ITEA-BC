# 1. The function `max()` and `max_of_three()` from previous exercises
# will only work for two and three numbers, respectively.
# But suppose we have a much larger number of numbers,
# or suppose we cannot tell in advance how many they are?
# Write a function max_in_list()
# that takes a list of numbers and returns the largest one.
#
# # Write test with 3-4 cases

# Working BAD, Why ??

numbers = []
while True:
    number = input('Enter something number: ')
    if number:
        numbers.append(number)
    else:
        break
print(max(numbers))

# WOrking norms

numb = map(int, input("Enter : ").split())
nums = [int(item) for item in numb]

def maxmin(nums):
  max = 0
  for n in nums:
    if n > max:
      max = n
  return max
print(maxmin(nums))
