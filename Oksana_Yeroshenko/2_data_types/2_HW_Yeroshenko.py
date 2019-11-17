#Create variable price and increase price by 10 after each new input from user.
price = 10000

# Use input for get:
  # Brand
  # Model
  # Color
  # Year
  # Engine volume
  # Odometer
  # Phone number
brand = input("Input car brand, please")
price+=10
model = input("Input car model, please")
price+=10
colour = input("Input car colour, please")
price+=10
year = int(input("Input year of issue, please"))
price+=10
eng_vol = int(input("Input car engine volume, please"))
price+=10
odometer = int(input("Input car odometer reading, please"))
price+=10
phone_num = input("Input your phone number, please")
price+=10

# Multiply your price by 10 and divide by 100.
price *= 10
price //= 100

# Decrease value of odometer and year.
odometer //= 7
year += 10

#Create car:
car = f"Brand - {brand}, Model - {model}, Colour - {colour}, Year - {year}, Engine volume - {eng_vol}, Odometer - {odometer}, Price {price}, Phone Number - {phone_num}"

# Output created car
print(car)