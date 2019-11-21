# # Create variable majority and set 'minor' if age less than 18, in other case set 'adult'


try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print('You are adult')
    else:
        print('You are minor, goodbye')
except Exception as e:
    print(e)
    print('Try again later')
