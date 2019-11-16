my_fav_brand = ["toyota", "audi", "land rover"]
my_fav_model = ["camry", "r8", "range rover"]
my_fav_color = ["blue", "black", "gray"]

price = 3000
brand: "str" = input("Brand of your car is: ")
if brand not in my_fav_brand:
    print("Got it!")
else:
    print("Good choice!")
price_1 = price + 100

model = input("Model of your car is: ")
if model not in my_fav_model:
    print("As you wish")
else:
    print("Good choice!")
price_2 = price_1 + 100

color = input("Color of your car is: ")
if color not in my_fav_color:
    print("OK")
else:
    print("Good choice!")
price_3 = price_2 + 100

try:
    year = int(input("Year of your car is: "))
except ValueError as error:
     print("Try again")
     year = int(input("Year of your car is: "))
except Exception as error:
     print(error)
else:
     print("Good but let's try a bit older one")
finally:
     year = year - 1
     print("Year of your car is: ", year)
price_4 = price_3 + 100

try:
    engine_volume = float(input("Engine volume of your car is: "))
except Exeption as error:
    print(error)
    engine_volume = int(input("Engine volume of your car is: "))
else:
    engine_volume = engine_volume + 0.1
    print("Maybe a bit more?")
    print("Engine volume of your car is: ", engine_volume)
price_5 = price_4 + 100

odometer = int(input("Odometer of your car is: "))
if odometer < 1000:
    print("Did you even use it?")
if odometer > 50000:
    print("Wow! Such a traveler!")
if odometer >= 100000:
    print("Don't know when to stop, huh?")
price_6 = price_5 + 100

phone_number = int(input("Your phone number: "))
print("Great! We'll call you!")
end_price = price_6 + 100

print("Let's sum up!")

print("Brand of your car is: ", brand)
print("Model of your car is: ", model)
print("Color of your car is: ", color)
print("Year of your car is: ", year)
print("Engine volume of your car is: ", engine_volume)
print("Odometer of your car is: ", odometer)
print("Price of the car is: ", end_price)

total_rating = [ ]
if brand == "toyota":
    if model in my_fav_model and year == 2012:
        total_rating.append("Exellent choice!")
    elif model in my_fav_model and year <= 2012:
        total_rating.append("Try somthing new")
    elif model not in my_fav_model and year <= 2012:
        total_rating.append("Would you like to change model?")
    elif model not in my_fav_model and year >= 2012:
        total_rating.append("Not bad")
    elif model in my_fav_model and year >= 2012:
        total_rating.append("Ha! We are on the same page!")
    else:
        total_rating.append("Could be better")
elif brand in my_fav_brand:
    if model in my_fav_model and color in my_fav_color:
        total_rating.append("Great choice!")
    if model in my_fav_model and color not in my_fav_color:
        total_rating.append("Well, that's nice too")
    else:
        total_rating.append("You could do better")
else:
    total_rating.append("We sure have different taste")

print("Total rating: ",  total_rating)