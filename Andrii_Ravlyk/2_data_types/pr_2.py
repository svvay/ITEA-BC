# Practise

# 1. Create each type variables
v_int = 25
v_str = "String"
v_float = 10.2
v_bool = True
v_tuple = (1, 2)
v_list = [1, 2]
v_dictionary = {'a': 1, 'b': 2}
# 2. Get variable type and output it by (print(type(variable_name)))
print("v_int", type(v_int))
print("v_str", type(v_str))
print("v_float", type(v_float))
print("v_bool", type(v_bool))
print("v_tulip", type(v_tuple))
print("v_list", type(v_list))
print("v_dictionary", type(v_dictionary))

# 3. Use input/output for get:
#
# * First Name
# * Last Name
# * Phone number
# * Group
# * a, b, c, d
first_name = input("Type your first name: ")
last_name = input("Type your last name: ")
phone_number = input("Type your phone number: ")
group = input("Type your group: ")
mess1= f"Hi your first name  {first_name}, your last name {last_name}, phone number {phone_number}, group {group} "
print(mess1)
mess2="Hi your first name {}, your last name {}, phone number {}, group {}".format(first_name, last_name, phone_number, group)
print(mess2)
pass
