# Creating a variable for car name
car_name = input("Please input name of car: ")

# Creating variable for car price

car_prise = int(input("please input the prise of your car: "))

# Using input from User for car characteristics

Brand = input("Please input car brand: ")
Model = input("Please input car model: ")
Color = input("Please input car color: ")
Year = int(input("Please input car year: "))
Engine_volume = input("Please input car engine volume: ")
Odometer = int(input("Please input car odometer: "))
Phone_Number = input("Please input your phone number: ")

# Multiplying car price

car_prise = car_prise * 10 / 100

# Decreasing year of the car
Year -= 10
# Decreasing odometer of the car
Odometer -= 30000
# Output creating car with new properties
print("Your car " + car_name + " has next properties: \n" +
      "    Brand - " + str(Brand) + "\n" +
      "    Model - " + str(Model) + "\n" +
      "    Color - " + str(Color) + "\n" +
      "    Year - " + str(Year) + "\n" +
      "    Engine volume - " + str(Engine_volume) + "\n" +
      "    Odometer - " + str(Odometer) + "\n" +
      "Phone number of the owner - " + str(Phone_Number))