brand = input("Input car brand ")
model = input("Input car model ")
colour = input("Input car colour ")
year = input("Input year of issue ")
eng_vol = input("Input car engine volume ")
odometer = input("Input car odometer reading ")
phone_num = input("input your phone number ")

car_rating = 100
favorite = {"brand": "volvo", "model": "rg51", "colour": "red"}
if brand not in favorite.values(): print(f"This isn`t your favorite brand: {brand}")
elif model not in favorite.values(): print(f"This isn`t your favorite model: {model}")
elif colour not in favorite.values(): print(f"This isn`t your favorite colour: {colour}")
else: print("This is your favorite car: ", brand, model, colour)

if brand not in favorite.values(): car_rating -= 20
if model not in favorite.values(): car_rating -= 10
if colour not in favorite.values(): car_rating -= 5
print("Car rating is: ", car_rating)

try:
    year = int(year)
except Exception as error:
    print(error)
else: year += 1
print("Year of issue: ", year)

try:
    eng_vol = float(eng_vol)
except Exception as error:
    print("Incorrect value of engine volume")
else: eng_vol += 0.1
print("Car engine volume is ", eng_vol)

odometer = int(odometer)
if odometer < 1000: car_rating += 50
if odometer > 50000: car_rating -= 20
if odometer >= 100000: car_rating -= 30
print("Car rating: ", car_rating)

