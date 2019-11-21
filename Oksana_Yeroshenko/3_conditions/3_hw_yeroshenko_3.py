cc_num = input("Input your credit card number: ")
cc_cvv = input("Input your credit card cvv: ")
cc_mmyy = input("Input your credit card expire date (mm/yy): ")

if len(cc_num) != 16:
    exit()

try:
    cc_num = int(cc_num)
except Exception as error:
    print("Your credit card number is not correct")
    exit()
else:
    print("OK")

if len(cc_cvv) != 3:
    print("Your credit card cvv is not correct")
    exit()

print("Everything fine")
