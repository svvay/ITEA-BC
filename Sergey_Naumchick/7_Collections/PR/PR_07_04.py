# Person:
#    * Use a dictionary to store information about a person you know.
#    * Store their first name, last name, age, and the city in which they live.
#    * You should have keys such as first_name, last_name, age, and city.
#    * Print each piece of information stored in your dictionary.

dict_david = {"first_name": "Sergey", "last_name": "Davidenko", "age": 18, "city": "New York"}

for i in dict_david:
    print(f"{i} - {dict_david[i]}")

s = dict_david.pop("city")
print(s)

print(dict_david.items())
