# 4. Write decorator that collect result of each function into list.

def decorator_list_result_func(funk_to_decorate):
    def wrapper():

        funk_to_decorate()
        with open("result_list.txt", "a+") as file_to_save:
            file_to_save.write(f"{str(funk_to_decorate())}\n")

    return wrapper()


@decorator_list_result_func
def print_to_list():
    list = []
    for i in range(10):
        list.append(i)
    return list


@decorator_list_result_func
def func_name():
    c = input("введите имя: ")
    return c
