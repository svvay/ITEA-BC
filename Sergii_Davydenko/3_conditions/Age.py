# # # Try to change age from str to int and catch Exception (ValueError), set age None in else case

try:
    age = int(input('Enter your age: '))
    print(f'your age is: {age}')
except Exception as e:
    age = None
    print(f"Your age is {age} for me")
