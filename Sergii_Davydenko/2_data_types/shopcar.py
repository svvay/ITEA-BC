
price = 0

b = input('Enter Brand: ')
m = input('Enter model: ')
c = input('Enter color: ')
y = int(input('Enter year: '))
ev = int(input('Enter engine: '))
o = int(input('Odometer: '))**8
pn = int(input('Enter Phone: '))

newprice = int(((price + 10*7) * 10) / 100)
od = o / 2
ye = y / 2

print('you new car is: Brand: {}, Model: {}, Year: {}, Odometer: {}, and price {}'.format(b, m, y, o, newprice))
