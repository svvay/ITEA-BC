brand = input("Car brand is: ")
rating_value = 1
model = input("Model of the car is: ")
rating_value += 1
color = input("The color of the car is: ")
rating_value += 1
year = input("The year of manufacturing is: ")

rating_value += 1
engine_volume = int(input("Engine volume is (in litters): "))
rating_value += 1
odometer = int(input("The mileage is: "))
if odometer <= 1000:
    rating_value += 5
elif 1000 <= odometer <= 50000:
    rating_value += 3
else:
    rating_value += 1


favourite_brand = ("opel", "ford", "toyota", "GM", "nissan")
try:
    if brand in favourite_brand:
        print( brand, "is in favourite list" )
    else:
        print( brand, "is not in the favourite list" )
finally:
    print("The favourite brand is: ", favourite_brand[0])


try:
    year = int(year)
except ValueError as error:
    print("Year of manufacturing data is invalid")
else:
    print("Year of manufacturing is: ", year)
finally:
    year += 1
    print("Year of manufacturing is: ", year)

try:
    engine_volume = float(engine_volume) + 0.1
except ValueError as error:
    print("Engine volume data is ivalid")
else:
    print("Engine volume is: ", engine_volume)

if rating_value <= 5:
    print("Your car rating index is: ", rating_value, "Car estimated price is low")
elif rating_value <=7:
    print("Your car rating index is: ", rating_value, "Car estimated price is medium")
else:
    print("Your car rating index is: ", rating_value, "Car estimated price is high")


# Home work Part 2, Credit card

credit_card = input("Enter number of your credit card: ")
expiration_date = input("Enter expiration date of your card in format dd/yy: ")
cvv = input("Enter 3 digit cvv code: ")
if len(credit_card) != 16:
    exit()
credit_card = int(credit_card)
if type(credit_card) is int:
    print("ok")
else:
    exit()
if len(cvv) < 3:
    print("Error")
    exit()

else:
    print("Everything is Ok")






