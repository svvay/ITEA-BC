price = 150
brand: "str" = input("Brand of your car is: ")
price_1 = price + 10
model = input("Model of your car is: ")
price_2 = price_1 + 10
color = input("Color of your car is: ")
price_3 = price_2 + 10
year = int(input("Year of your car is: "))
price_4 = price_3 + 10
engine_volume = int(input("Engine volume of your car is: "))
price_5 = price_4 + 10
odometer = int(input("Odometer of your car is: "))
price_6 = price_5 + 10
phone_number = int(input("Your phone number: "))
price_7 = price_6 + 10

end_price = price_7 * 10/100
odometer = odometer - 5000
year = year - 1

print("Brand of your car is: ", brand)
print("Model of your car is: ", model)
print("Color of your car is: ", color)
print("Year of your car is: ", year)
print("Engine volume of your car is: ", engine_volume)
print("Odometer of your car is: ", odometer)
print("Your phone number: ", phone_number)
print("Price of the car is: ", end_price)