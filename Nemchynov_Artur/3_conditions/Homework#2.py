My_favourite_brands = ("Ferrari", "Porsche", "Lincoln")
Brand = ("Please, input brand your car: ")
# Users brand car
if Brand not in My_favourite_brands:
    Brand = input(f"No, {Brand} its not my favourite, please input my favourite:")
    if Brand in My_favourite_brands:
        print(f"Yes {Brand} its my favourite brand")
    else:
        print(f"NO {Brand} not my favourite brand!")
        Brand = input( "Try again: ")
        if Brand in My_favourite_brands:
            print (f"Yes {Brand} is my favourite brand")
        else:
            print(f"{Brand} sorry, but its not my favourite brands, my favourite brand are: {My_favourite_brands}")

else:
        print (f"Yes {Brand} its my favourite brand")
# Users model car
Model = input ("Please, input model your car: ")
#Users car color
Year = input("Please input your car color: ")
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
print(f"We will help you - now your car is older - {Year}, don't tell me thank's")
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
Odometer = input("Please input The Odometer of the car: ")
print("Sorry, you should enter only numerical type ")
Phone_number = input("Please input your phone number: ")
CreditCard_Number = input("Please input your card number: ")

if len(CreditCard_Number) != 16:
    print("Error")
    exit()
try:
    CreditCard_Number = int(CreditCard_Number)
    print("OK")
except Exception as e:
    print("Error")
    exit()
CreditCard_CVV = input("Please input your CVV code: ")

if len(CreditCard_CVV) < 3:
    print("Error!!!")
    exit()
else:
    print("OK")

CreditCard_mmyy = input("Please input your month and year (mm/yy): ")

print("Everything fine!")



