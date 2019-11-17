# Input variables

Rating_value = 0
# RAiting_value will be increased each time, when user will add some characteristics


MyFavouritBrand = ("Ferrari", "Lexus", "Nissan")

# Input brand from user

Brand = input("Please input The brand of the car: ")

# Testing if Brand is in Favourite brand 3 times and if not - show favourite

if Brand not in MyFavouritBrand:

    Brand = input(f"No, {Brand} is not my favourite, please input my favourite: ")
    if Brand in MyFavouritBrand:
        print(f"Yes {Brand} is my favourite brand")

    else:
        print(f"NO!!! {Brand} not my favourite!!!")
        Brand = input("Try again: ")

        if Brand in MyFavouritBrand:
            print(f"Yes {Brand} is my favourite brand")

        else:
            print(f"What? WTF? {Brand}? That's very bad you don't guess, my favourite brands are:\n{MyFavouritBrand}")

else:
    print(f"Yes {Brand} is my favourite brand")

Rating_value += 1

# Input model from user

Model = input("Please input The Model of the car: ")

Rating_value += 1

# Input colour from user

Colour = input("Please input The Colour of the car: ")

Rating_value += 1

# Input Year from user

Year = input("Please input The Year of the car: ")

try:
    Year = int(Year)
except Exception:
    print(f"you entered {Year} - this is not a numeral type!")
    Year = input("Please input Year of your car in numeral type: ")
    try:
        Year = int(Year)
    except Exception as e:
        print(f"you entered {Year} - this is not a numeral type!")

print(f"You enter {Year}")
# Decreasin
try:
    Year -= 1
    print(f"We will help you - now your car is older - {Year}, don't tell me thank's")

except Exception as e:
    print("wrong type that's not good( ")

Rating_value += 1

# Input colour from user

Engine_volume = input("Please input The Engine volume of the car: ")

try:
    Engine_volume = float(Engine_volume)
    Engine_volume += 0.1
except Exception as e:
    Engine_volume = input(f"You entered wrong type of {Engine_volume}, please input numeral: ")

    try:
        Engine_volume = float(Engine_volume)
        Engine_volume += 0.1

    except Exception as e:
        print(f"That's not very good you entered {Engine_volume} - this is not numerical (")
print(f"Your new Engine volume is - {Engine_volume}")

Rating_value += 1

# Input colour from user

Odometer = input("Please input The Odometer of the car: ")

try:
    Odometer = int(Odometer)
    if Odometer < 1000:
        Rating_value += 4
    elif Odometer > 50000:
        Rating_value += 2

    elif Odometer >= 100000:
        Rating_value += 1
    else:
        Rating_value += 3

except Exception as e:
    print("Sorry, you should enter only numerical type ")

# Input colour from user

Phone_number = input("Please input your phone number: ")
Rating_value += 1

print(f"\nRating of your car is: {Rating_value}\n\n\n")

# Inputing data of the credit card
CreditCard_Number = input("Please input your card number: ")

if len(CreditCard_Number) != 16:
    print("Error")
    exit()
try:
    CreditCard_Number = int(CreditCard_Number)
    print("OK")
except Exception as e:
    print("Error - wrong type!")
    exit()
CreditCard_CVV = input("Please input your CVV code: ")

if len(CreditCard_CVV) < 3:
    print("Error")
    exit()
else:
    print("OK")

CreditCard_mmyy = input("Please input your month and year (mm/yy): ")

print("Everything fine!")
