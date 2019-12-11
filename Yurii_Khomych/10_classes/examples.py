# Instantiating Objects
#
# class Dog:
#     pass
#
# Dog()
# # <__main__.Dog object at 0x1004ccc50>
# Dog()
# # <__main__.Dog object at 0x1004ccc90>
# a = Dog()
# b = Dog()
# del a
# a == b
# # False
# pass
#
# class Dog:

    # Class Attribute
    # species = 'mammal'

    # Initializer / Instance Attributes
    # def __init__(self, name, age, street=None):
    #     self.first_name = name
    #     self.age = age
    #     self["age"] = age
        # self.street = street

#
# # Instantiate the Dog object
# philo = Dog(name="Philo", age=5)
# # philo = Dog("Philo")
# mikey = Dog("Mikey", 6)
# # Access the instance attributes
# print(f"{philo.first_name} is {philo.age} and {mikey.first_name} is {mikey.age}.")
# pass
#
# # Is Philo a mammal?
# if philo.species == "mammal":
#     print("{0} is a {1}!".format(philo.first_name, philo.species))

#
# class Dog:

    # Class Attribute
    # species = 'mammal'

    # Initializer / Instance Attributes
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    # instance method
    # def description(self):
        # return "{} is {} years old".format(self.name, self.age)

    # instance method
    # def speak(self, sound):
    #     return "{} says {}".format(self.name, sound)

# Dog().description()
# Instantiate the Dog object
# mikey = Dog("Mikey", 6)
#
# # call our instance methods
# print(mikey.description())
# print(mikey.speak("Gruff Gruff"))
# jony = Dog("Jony", 6)
# pass
#
# class Email:
#     def __init__(self):
#         self.is_sent = False
#
#     def send_email(self):
#         print("Email is successfully sent")
#         self.is_sent = True
#
#     def prepare_draft(self, body, subject):
#         self.body = body
#         self.subject = subject
#
# my_email = Email()
# my_email.is_sent
# # False
# my_email.send_email()
# my_email.is_sent
# # True
#
#
#
# class Dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
# spencer = Dog("sharik", 1, "German Shepard")
# spencer.breed
# # 'German Shepard'
# sara = Dog("bobik", 2, "Boston Terrier")
# sara.breed
# # 'Boston Terrier'

#
# # Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#
# # Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        if speed in ("slow", "fast"):
            return "{} runs {}".format(self.name, speed)
#
#
# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    def description(self):
        return "{} is {} years old".format(self.name, self.age).upper()
#
#
class Dvorniaga(Bulldog, RussellTerrier):
    species = 'reptile'
#
#
# # Child classes inherit attributes and
# # behaviors from the parent class
sharik = Bulldog("Sharik", 12)
print(sharik.description())
#
# # Child classes have specific attributes
# # and behaviors as well
print(sharik.run("slowly"))
#
bobik = RussellTerrier("bobik", 10)
#

donatello = Dvorniaga(name="Donatello", age=1)
#
donatello.run("rapidly")
