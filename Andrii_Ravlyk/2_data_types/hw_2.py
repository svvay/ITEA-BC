# HW

# Create car:

car = 'New_car'

# Create variable price and increase price by 10 after each new input from user.
price = 100

# Use input for get:
#   Brand
brand = input("insert Brand= ")
price +=  10
#   Model
model = input("insert Model= ")
price +=  10
# Color
color = input("insert Color= ")
price +=  10
# Year
year = int(input("insert Year= "))
price +=  10
# Engine volume
engine_volume = input("insert engine_volume= ")
price +=  10
# Odometer
odometer = int(input("insert odometer= "))
price +=  10
# Phone number
phone_number = input("insert phone numbe= ")
price +=  10

# Multiply your price by 10 and divide by 100.
price *= 10
price /= 100

# Decrease value of odometer and year.
odometer -= 1
year -=1

# Output created car

message = f"You car is {car} , price = {price}, brand = {brand}, model = {model}, color = {color}, year = {year}, " \
          f"engine_volume = {engine_volume}, odometer = {odometer}, phone_number = {phone_number}  "
print(message)
