price = 100
brand: "str" = input("Car brand is: ")
price = 100 + 10
model = input("Model of the car is: ")
price = price + 10
color = input("The color of the car is: ")
price = price + 10
year = int(input("The year of manufacturing is: "))
price = price + 10
engine_volume = int(input("Engine volume is (in litters): "))
price = price + 10
odometer = int(input("The mileage is: "))
price = price + 10
phone = input("Your phone number is: ")
price_1 = price * 10/100
odometer = odometer - 10000
year = year - 2

print("The car brand is: ", brand)
print("Model of the car is: ", model)
print("Color of the car is: ", color)
print("Year of manufacturing is: ", year)
print("Engine volume is: ", engine_volume)
print("The mileage is: ", odometer)
print("The car price is: ", price)
