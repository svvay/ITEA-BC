# def yell(text):
#     return text.upper() + '!'
#
# print(yell('hello'))
# 'HELLO!'

# bark = yell
# print(bark('woof'))
# 'WOOF!'
# del yell

# print(yell('hello?'))
# NameError: "name 'yell' is not defined"

# print(bark('hey'))
# 'HEY!'
# print(bark.__name__)
# del bark
# print()
# 'yell'
#
# funcs = [bark, str.lower, str.capitalize]
# for f in funcs:
#      print(f, f('hEy there'))
# funcs[0]('heyho')
# ‘HEYHO!'

#
# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(first_name):
#     return f"Yo {first_name}, together we are the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
#
# greet_bob(say_hello)
# # 'Hello Bob'
#
# greet_bob(be_awesome)
# # 'Yo Bob, together we are the awesomest!’
#
# def first_child():
#     print("some print")
#

# def parent(arg_first_child, arg_second_child):
#     print("Printing from the parent() function")
#
#     def first_child():
#         print(f"Printing from the {arg_first_child} function")
#
#     def second_child():
#         print(f"Printing from the {arg_second_child} function")
#
#     second_child()
#     first_child()
#
# parent("ARG_FOR_FIRST_CHILD", "ARG_FOR_SECOND_CHILD")
# pass
# first_child()
# Printing from the parent() function
# Printing from the second_child() function
# Printing from the first_child() function

#
# def identity(x):
#     return x
#
# lambda x: x
#
# lambda x, y, z: x + 1
#
# (lambda x: x + 1)(2)
# # 3
#
# add_one = lambda x: x + 1
# add_one(2)
# # 3
#
# def add_one(x):
#     return x + 1

# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
# pass
#
# guido = full_name(last='van rossum', first='guido')
# x=1
#
# add = lambda x, y: x + y
#
# def parent(num):
#     def first_child(name):
#         return f"Hi, I am {name}"
#
#     def second_child(name):
#         return f"Call me {name}"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child

# new_func = parent(1)
# new_func_2 = parent(2)
# pass
#
# x = 1
# def my_func():
#     y = 1
#     return x + y
# # print(y)
# # el
# for el in (1,2,3):
#     print(el)
#     if el == 4:
#         new_var = el
#     else:
#         new_var = None
#
# print(new_var)
# print(my_func())
#
# b = 6
# def f1(a):
#     print(a)
#     print(b)
# f1(a=12)
# pass


# b = 6
# def f1(a):
#     print(a)
#     print(b)
#
#     def f2():
#         c = a + b
#         print(c)
#         return c * 3
#
#     return print(f2())
# f1(a=12)
#
# my_lambda = lambda a, b: a + b
# my_lambda(a, b)

# a = 5
# def function(a):
#     print(a)
#     a = 10
#     return a
# print(function(a))
#
#
# a = 5
# def function():
#     global a
#     print(a)
#     a = 10
#     return a
# print(function())

# def f1():
#     a = 1
#     b = 2
#     print(a)
#     print(b)
#     def f2():
#         nonlocal a
#         a += b
#         return print(a)
#     print(a)
#     return f2()
# f1()

# a = 1
# def f1():
#     b = 2
#     def f2():
#         nonlocal a
#         c = a + b
#         a = a + b
#         a += b
#         return c
#         return a
#     return f2()
# print(f1())

global a
a = 123
globals()
x = 1
import time



# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     return "Whee!"
#
# say_whee = my_decorator(say_whee)
#
# say_whee()
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.
# from datetime import datetime
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 21:
#             func()
#         else:
#             say_tshh()  # Hush, the neighbors are asleep
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# def say_tshh():
#     print("Tsshh!")
#
# say_whee = not_during_the_night(say_whee)
#
# say_whee()

# def make_me_shota(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def decorator(func):
#     print("Some print")
#     return func()
#
# @my_decorator()
# def say_whee():
#     print("Whee!")
#
# @decorator
# def say_whee_2():
#     print("Whee!")
#
# say_whee()
# say_whee_2()

# for i in ():
#     print(i)
# else:
#     print("None")
