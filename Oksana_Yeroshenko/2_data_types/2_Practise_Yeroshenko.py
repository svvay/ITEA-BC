#create a variable type "int" and print type
amount = 1000000
print (type (amount))
#create a variable type "str" and print type
who = "women"
print (type (who))
#create a variable type "float" and print type
pi = 3.14
print (type (pi))
#create a variable type "list" and print type
what = ("dress", "bag", "glasses", "lipstick")
print (type(what))
#create a variable type "bool" and print type
yes_or_no = True
print (type(yes_or_no))
#create a variable type "tuple" and print type
currency = ("USD", "EUR", "UAH")
print (type(currency))
#create a variable type "set" and print type
country = set(["Ukraine", "Poland", "Romania"])
print (type(country))
#create a variable type "dic" and print type
country_currency = {"Ukraine": "UAH", "Poland": "PLZ"}
print (type(country_currency))

#3. Use input/output for get:
first_name = input("Your name: ")
last_name = input("Your last name: ")
phone_num = input("Your phone number: ")
group = input("Your group: ")
a: int= input("Input a=: ")
b: int= input("Input b=: ")
c: int= input("Input c=: ")
d: int= input("Input d=: ")
print("Your name is:", first_name)
print("Your last name is:", last_name)
print("Your phone number is:", phone_num)
print("Your group is:", group)
print("a=", a, "b=", b, "c=", c, "d=", d)

# Use each type of:
# Arithmetic operators
a=int(a)
b=int(b)
c=int(c)
d=int(d)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# Assignment operators
print ("a+=b")
a+=b
print("a=", a)
print("a-=b")
a-=b
print("a=", a)
print("a*=b")
a*=b
print("a=", a)
print("a/=b")
a/=b
print("a=", a)
print("a%=b")
a%=b
print("a=", a)
print("a//=b")
a//=b
print("a=", a)
print("a**=b")
a**=b
print("a=", a)

# String formatting
print(f"Group: {group}, Last Name: {last_name}, First Name: {first_name}, Phone number: {phone_num}")






