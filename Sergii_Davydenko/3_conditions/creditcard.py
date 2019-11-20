 # ## Input: credit card number (fake data), cvv, mm/yy


card_date, card_month = map(int, input("Enter date mm/yy: ").split())
card_number = len(input('Enter number: '))
card_cvv = len(input('Enter cvv card: '))

if card_number == 16:
    if card_cvv == 3:
        print('All is good')
    else:
        exit('Sorry but your card cvv is wrong')
else:
    exit('Sorry but your card number is wrong')
print(card_date, '/', card_month)
