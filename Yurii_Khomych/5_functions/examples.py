# def my_function(first_name):
#     print(f"Hello {first_name}")
#
# my_function("World")
# my_function("Bob")
# my_function("Jonny")
# my_function("Vasya")
#
#
# def get_banana_index(foods):
#     banana_index = 0
#     for num, food in enumerate(foods):
#         if food == "banana":
#             banana_index = num
#             return banana_index
#
#
# fruits = ["apple", "banana", "cherry"]
#
# banana_index = get_banana_index(fruits)
#
# def my_function(x):
#     return 5 * x
#
# result = my_function(10)

def max_in_list(my_list):
    my_list.sort(reverse=True)
    return my_list[0]

def test_max_function():
    assert max([1, 2, 3]) == 3, "Max value is 3"
    assert max([4, 2, 3]) == 4, "Max value in list is 4"
    print("success test_max_function")

def test_min_function():
    assert min([1, 2, 3]) == 1, "Min value in list is 1"
    assert min([4, 2, 3]) == 2, "Min value in list is 2"
    print("success test_min_function")

def test_max_in_list():
    assert max_in_list([1,2,3]) == 3, "Max must be 3"
    assert max_in_list([]) == [], "Max must be 3"
    print("success test_min_function")


test_max_function()
test_min_function()
test_max_in_list()
