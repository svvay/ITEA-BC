# HW

# 1. Create car:

car = 'New_car'
c_rating = 100
# Use input for get:
#   Brand
brand = input("insert Brand= ").upper()
#   Model
model = input("insert Model= ").upper()
# Color
color = input("insert Color= ").upper()
# Year
year = int(input("insert Year= "))
# Engine volume
engine_volume = input("insert engine_volume= ")
# Odometer
try:
    odometer = int(input("insert odometer= "))
except:
    print("Incorrect type odometer")
# Phone number
phone_number = input("insert phone numbe= ")

# Check that brand (model, color) not in your favourite, print brand name,
#    and in finally clause print your favourite.
my_favorite_car = {"brand" : "AUDI", "model" : "Q3", "color" : "RED" }

print ("==============Resut=============\n")


if brand != my_favorite_car["brand"]:
    c_rating = c_rating - 10
if model != my_favorite_car["model"]:
    c_rating = c_rating - 10
if color != my_favorite_car["color"]:
    c_rating = c_rating - 10
if c_rating == 100:
    print("This not my favorite car = ", brand)
    print ("Car rating = ", c_rating)

# Try to change year type to int and catch exception, else print year
#    and finally decrease year by 1 and print
try:
    year = int(year)
except ValueError as err:
    print ("Incorrect type year")
else:
    print ("year", year)
    year -= 1
    print("year = ", year)

# Change Engine volume type to float and add 0.1 to value
try:
    engine_volume = float(engine_volume)
except ValueError:
    print("Incorrect type Engine volume")
else:
    engine_volume = engine_volume + 0.1
    print("Engine volume = ", engine_volume)

# Change odometer type to int check that odometer value less than 1000,
#   greater than 50000, greater or equal to 100000 and
#    set different value for rating
#  Get final rating for your car by your criterion (3-4 if cases)
if odometer<1000:
    c_rating = c_rating + 15
elif odometer>50000:
    c_rating = c_rating - 10
if odometer>=100000:
    c_rating = c_rating - 50
print ("Final rating = ", c_rating)

pass
# 2. Input: credit card number(fake data), cvv, mm / yy
# Check that credit card number length has 16 symbols in other case call exit()
print ("==============Part 2 HW==========Credit Card==============\n")
card_number = input("Insert card number = ")
cvv = input("Insert cvv = ")
exp_date = input("Insert exp_date in format mm/yy = ")
if len(card_number) != 16:
    exit()

pass

