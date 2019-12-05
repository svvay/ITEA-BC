li = ["+380971236789", "+380809123232", "99999x9999"]
# 5. Check that mobile phone number is valid.


mob_operators = ['+38097', '+38067', '+38093', '+38063', '+38050']


def check_number(li):
    for num in li:
        if num[:6] in mob_operators:
            print(f'This is really phone number: {num}')
        else:
            print(f'This is not a phone number {num}')

check_number(li)