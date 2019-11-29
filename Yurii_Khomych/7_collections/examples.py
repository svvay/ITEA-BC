# a = ['foo', 'bar', 'baz', 'qux']
# b = ['foo', 'bar', 'baz', ("abc", "cba"), {1: 1}, [[1, [1, ]],2,3], a]
# print(a, b)
# b[0] = 1
# print(b)
#
# a = ['foo', 'bar', 'baz', 'qux']
# b = ['baz', 'qux', 'bar', 'foo']
# c = a
# d = ['foo', 'bar', 'baz', 'qux']
# print(a == c)
# print(a is c)
# print(a is d)

# a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
# list_of_functions = [str, int, len]
# my_obj = "1"
# for my_function in list_of_functions:
#     print(my_function(my_obj))
# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print(a[2:5])
# print(a[2:6:2])
# print(a[3::-1])
# b = a[:]
# print(a is b)
# print(a == b)
# c = a[0]
# print(c is a[0])
# a[0] = 1
# print(c is a[0])
# print(c)
# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print('qux' in a)
# print('quxx' in a)
# print('quxx' not in a)

# print('baz' + 'qux')
# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# b = ['cux', 'caux', 'corge']
# c = [1, 2, 3]
#
# print(a + a)
# print(a + b)
# print(a * 2)
#
# print(len(a))
# print(min(b))
# print(max(b))
# print(sum(c))

# x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# x = [{"name": "My name"}, {"name": "My name 2"}]
# print(x[1][1][1])
# print(x[1][1])

# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# a[2] = 10
# a[-1] = 20
# del a[3]
# print(a)

# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
# print(a)
# a[1:6] = ['Bark!','Bark!','Bark!',]
# print(a)
# a[1:6] = ('Lark!','Lark!','Lark!',)
# print(a)
# a += ['grault', 'garply']
# a = a + ['grault', 'garply']
# print(a)
# a = [10, 20] + a
#
# print(a)
# a += (20,)
# print(a)
# a += 'corge'
# print(a)
# list("abc")

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

# print(a.index("bar"))
# print(a.index("baar"))
# a.append(1)
# a.extend([1,2,3])
# a.extend("abc")
# a.insert(1, "abc")
# a.insert(-1, "cde")
# print(a.remove("corge"))
# print(a.remove("corgea"))
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# print(a)
# print(range(0, 1000000000))

# tuples

# t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
# print(t[0])
# print(t[1])
# print(t[-2])
# print(t[::-1])
# t[0] = 1

# two, three, four, five = [2, 3, 4, 5]
# print(two, three, four, five)

# Other lang
# temp = y
# y = x
# x = temp

# Python
# x = 1
# y = 2
# x, y = y, x

# user = {
#     'name': 'Taras',
#     'age': 17,
#     'address': 'Kyiv'
# }
#
# user = {
#     ["Name"]: 'Taras',
#     'age': 17,
#     'address': 'Kyiv'
# }

# dict([('name’,‘Taras’), ('age’, 17), ('address’, Kyiv’)])
# user = dict(
#     [
#         ("name", "Taras"),
#         ("age", 17),
#         ("address", "Kyiv"),
#     ]
# )
#
# user = dict(name="Taras", age=17, address="Kyiv")
# print(user)
# user["name"] = "Danylo"
# user["age"] = 21
# print(user)
# user[-1] = 1
# print(user)
#
# person = {}
# print(type(person))
# print(person)
# person["name"] = "Taras"
# print(person)
# person["age"] = 17
# print(person)
# person["from"] = "Kyiv"
# print(person)
# person["name"] = f"Danylo_{person['name']}"
# print(person)
# person["cities"] = [{"Kyiv": ["VDNH", {"MAYDAN": ("Globus", "ЦУМ")}]}, "Zhytomyr", "Lviv", "Rivne"]
# print(person)
# print(person["cities"])
# print(person["cities"][0])
# person['pets'] = {'dog': 'Petrushka', 'cat': 'Murzik'}
# print(person)
# print(person['pets'])

# d = {int: 1, float: 2, bool: 3}
# print(d)

# d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
# print(d)
# print(d[(1, 1)])
# a = set([1, 2, 3, 3])
# {a: 1}


# user = {
#     'name': 'Taras',
#     'age': 17,
#     'address': 'Kyiv'
# }
# user.clear()
# print(user.pop("age"))
# print(user["name"])
# print(user["names"])


# print(user.get("name"))
# print(user.get("names", "No Name"))
#
# print(user.items())
# print("name" in user)
# for key, value in user.items():
#     print(key, value)
# print(user)
# user.popitem()
# print(user)
# other_data = {"cities": ["Kyiv"], "other": (1,2,3)}
# user.update(other_data)
# c = dict(**user, **other_data, **{"as":1})
# print(user)
# print(c)

# Sets
# my_list = [1,2,3,4,4]
# my_set = {1,2,3,4,4}
# print(my_set)
# my_set = {1,2,3,4,[1,2]}
# my_set = {1,{1,2,2},3,4}
# my_set = {1,{1:2},3,4}
# print(my_set)
# print(list(my_set))
# print(set(my_list))
# my_set = {1}
# my_dict = {}
# x1 = {'foo', 'bar', 'baz'}
# x2 = {'baz', 'qux', 'quux'}
# print(x1 | x2)
# print(x1.union(x2))

# x1 | ('baz', 'qux', 'quux')
# x1.union(('baz', 'qux', 'quux'))
# print(x1.union(('baz', 'qux', 'quux')))
# print(x1 & x2)
# print(x1.intersection(x2))

# print(x1.update(['corge', 'garply']))
# x1 |= x2
# x1.add('qux')
# x1.add('qux1')
# x1.remove('baz')
# x1.remove('baza')
# x1.discard("baz")
# x1.pop()
# x1.clear()
# print(x1)

# x1 = {'foo', 'bar', 'baz'}
# x2 = frozenset(['foo', 'bar', 'baz'])
# x1.update([x2])
# print(x1)


# def main(one, two):
#     my_function_1(one)
#     my_function_2(two)
#
# one= []
# two= []
# main(one=one, two=two)
def my_func(word):
    pass


