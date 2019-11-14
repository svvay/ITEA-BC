# a = 1
# b = 2
# c = 4
#
# a == b
# a >= b
# a <= b
# a < b
# a > b

# True and True # True
# False and True # False
# True and False # False
# False and False # False


# True or True # True
# False or True # True
# True or False # True
# False or False # False
#

# my_friends = ["John", "Jack"]
# my_friends_tuple = ("John", "Jack")
# my_friends_set = set(["John", "Jack", "John"])
# my_friends_pets = {"John": "Murzik", "Jack": "Bobik", "Petya": ["Sharik", "Barbos"], "John": "Pesyk"}
# a = "Barbos" in {"John": "Murzik", "Jack": "Bobik", "Petya": ["Sharik", "Barbos"], "John": "Pesyk"}.values()
# my_string = "anaconda"
# my_string_2 = my_string
#
# my_string = "a"
#
# my_list = [1,2,3]
# my_list_2 = my_list
# my_list_2[0] = 5
# my_list
# "a" in my_string

# check = "Pesyk" not in my_friends_pets.values()
# print(a)
# today = "Tuesday"
# today = None
# my_friends = ["John", "Jack"]
# if "Max" not in my_friends:
# if "Max" not in my_friends and today == "Monday":
#     print("We need to add Max to my_friends")
#     my_friends.append("Max")
# elif "Kate" not in my_friends and today == "Tuesday":
#     print("We need to add Kate to my_friends")
#     my_friends.append("Kate")
# elif "Mary" not in my_friends and today == "Wednesday":
#     print("We need to add Mary to my_friends")
#     my_friends.append("Mary")
#
#
# print(f"Max must be in my_friends variable {my_friends}")
# if "Alex" not in my_friends and today is not None:
#     print("We need to add Alex to my_friends")
#     my_friends.append("Alex")

today = "Sunday"

my_visits = []
my_friends = ["John", "Jack"]
if today == "Sunday":
    if "Alise" not in my_friends:
        my_visits.append("Alise")
        my_friends.append("Alise")
    elif "Kate" not in my_friends:
        my_visits.append("Kate")
        my_friends.append("Kate")
    else:
        my_visits.append("Bar")
elif today == "Saturday":
    if "Kate" not in my_friends:
        my_visits.append("Kate")
        my_friends.append("Kate")
    if "Alise" not in my_friends:
        my_visits.append("Alise")
        my_friends.append("Alise")
    else:
        my_visits.append("Disco")
else:
    my_visits.append("Work")
    my_friends = []

today = "Monday" if "Alise" not in my_friends else "Tuesday" if "Kate" not in my_friends else "Friday"
today = None
if "Alise" not in my_friends:
    today = "Monday"
elif "Kate" not in my_friends:
    today = "Tuesday"
else:
    today = "Friday"
pass
