# 2.
#     * Input: credit card number (fake data), cvv, mm/yy
#     * Check that credit card number length has 16 symbols in other case call exit()
#     * Try to change credit card number type to int() if you get error print error message for user and call exit(),
#      in other case output "OK"
#     * Check length of cvv if less than 3 symbols, print error and call exit()
#     * If all checks passed print "Everything fine"

cred_card = input('Please enter your cardnumber: ')
if len(cred_card) != 16:
    exit()
elif len(cred_card) == 16:
    try:
        cred_card == int(cred_card)
        print('Cardnumber is integer. So its OK!')
    except ValueError as e:
        print('Entered cardnumber is not valid, so: GOOD BAY!')
        exit()

cvv_card = input('Please enter your cvv from entered card: ')
try:
    len(cvv_card) < 3
except ValueError as e:
    print('CVV is too short. Good bay!')
    exit()

exp_card = input('Please enter you mm/yy from entered card in format mm/yy: ')
print("Everything fine")
