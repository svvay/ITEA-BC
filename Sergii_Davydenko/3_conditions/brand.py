raiting = 0
lbrand = 'pontiak'
lmodel = 'airbus'
lcolor = 'brown'


# # # # Check that brand (model, color) not in your favourite, print brand name, and in finally clause print your favourite.

brand = input('Enter brand: ')
model = input('Enter model: ')
color = input('Enter color: ')

if brand == lbrand or model == lmodel or color == lcolor:
    print(f"Wow, i like this {lbrand} and {lmodel} and {lcolor} to")
else:
    print(f"Sorry, i'd like this brand, my favorite brand is {lbrand}, model {lmodel}, color {lcolor}")
raiting += 1


# # ### Try to change year type to int and catch exception, else print year and finally decrease year by 1 and print


year = input('Enter year: ')

try:
    print('You have so old car: ', int(year))
except Exception as e:
    print('The except is: ', e)
    year = 10
    print('You car so old: ', year - 1)
raiting += 1


# # ### Change Engine volume type to float and add 0.1 to value (print to user), (use try, except, else)


engine_volume = input('Enter engine: ')
try:
    float_eng_volume = float(engine_volume) + 0.1
    print(float_eng_volume)
except ValueError as e:
    print('U have a problem with: ', e)
raiting += 1


# # ### Измените тип одометра на int, чтобы проверить, что значение одометра меньше 1000, больше 50000, больше или равно 100000, и установите другое значение для рейтинга.


try:
    odometer = int(input('Enter odometer: '))

    if odometer < 1000:
        print(f'Good rate: {odometer}')
    elif odometer > 50000:
        print(f'Not bad rate: {odometer}')
    elif odometer > 100000:
        print(f'Иad rate: {odometer}')
except Exception as e:
    print('You enter fault information, try more next time: ')

raiting += 1


### Get final rating for your car by your criterion (3-4 if cases)


print(f'Now raiting car is {raiting}')
