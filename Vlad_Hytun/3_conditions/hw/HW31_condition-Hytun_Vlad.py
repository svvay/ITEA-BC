# 1. Create car:
#
#     * Use input for get:
#         * Brand
#         * Model
#         * Color
#         * Year
#         * Engine volume
#         * Odometer
#         * Phone number
#     * Create rating value for car and increase or decrease at each step
#     * Check that brand (model, color) not in your favourite, print brand name,
#     and in finally clause print your favourite.
#     * Try to change year type to int and catch exception, else print year
#     and finally decrease year by 1 and print
#     * Change Engine volume type to float and add 0.1 to value
#     (print to user), (use try, except, else)
#     * Change odometer type to int check that odometer value less than 1000,
#     greater than 50000, greater or equal to 100000 and
#     set different value for rating
#     * Get final rating for your car by your criterion (3-4 if cases)

reating_car = 0
premium_brand_car = ['BMW', 'MB', 'LEXUS']
favorite_color = ['BLUE', 'RED']

brand_car = input("Enter brand car: ")
if brand_car in premium_brand_car:
    reating_car += 2
else:
    reating_car += 1
model_car = input("Enter model car (from 1 to 10): ")
if int(model_car) >= 5:
    reating_car += 2
else:
    reating_car += 1
color_car = input("Enter color car: ")
if color_car is 'blue':
    reating_car += 10
else:
    reating_car += 1
year_car = input('Year of car: ')
if int(year_car) < 2010:
    reating_car += 1
else:
    reating_car += 2
engine_volume_car = input('Enter engine volume like 2000: ')
if int(engine_volume_car) > 2000:
    reating_car += 5
else:
    reating_car += 1
odometer_car = input('Enter odometer in km: ')
if int(odometer_car) > 100000:
    reating_car += 1
else:
    reating_car += 2
phone_number = input('Please enter your phone number:')

if brand_car.upper() in premium_brand_car:
    if color_car.upper() in favorite_color:
        print("It's greate! You know my favorite car!!!")
else:
    print("You don't know my favorite car")

try:
    my_change_year = int(year_car)
    print('You enter Year Car is right! So i decrease year by 1: ' + str(int(year_car)*0.1))
except ValueError as e:
    print("You should enter number in Year Car!")

try:
    my_change_engine = int(engine_volume_car)
    print('You enter Engine Car is right! So i add 0.1: ' + str(int(engine_volume_car)+0.1))
except ValueError as e:
    print("You should enter number in Engine Car!")

if int(odometer_car) < 1000:
    reating_car += 10
elif int(odometer_car) > 50000:
    reating_car += 5
elif int(odometer_car) >= 100000:
    reating_car += 0

print(f'Reating of your car is {reating_car} points of 27 available ')
