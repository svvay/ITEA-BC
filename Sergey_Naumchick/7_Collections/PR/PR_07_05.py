'''5. Rivers:
Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be `'nile': 'egypt'`.
    * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
    * Use a loop to print the name of each river included in the dictionary.
    * Use a loop to print the name of each country included in the dictionary.'''

dict_rivers = {"Nile": "Egipt", "Don": "Ukraine", "Syrdarya": "Tajikistan"}

for country, river in dict_rivers.items():
    print(f"The {country} runs throught {river}")
print()

for key_river in dict_rivers.keys():
    print(key_river)
print()

for river, country in dict_rivers.items():
    print(country)
