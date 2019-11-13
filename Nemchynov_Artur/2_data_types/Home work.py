car_name = input( "Please, enter your car name: " )

car_price = int(input("Please, enter your car price: "))

Brand = input("Please, enter your car brand: ")
Model = input("Please, enter your car model: ")
Color = input("Please, enter your car color: ")
Year = input("Please, enter your car year: ")
Engine_volume = input("Please, enter your engine volume: ")
Odometer = input("Please, enter your car odometer: ")
Phone_number = input("Please, enter your prone number: ")

car_price = car_price * 10 / 100

Year -= 30

Odometer -= 6000

print("car_name" + str(Brand) + str(Model) + str(Color) + str(Year) + str(Engine_volume) + str(Odometer) + str(Phone_number))

