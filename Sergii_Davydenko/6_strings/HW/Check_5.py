#  5. Check that mobile phone number is valid.
# `li = ["+380971236789", "+380809123232", "99999x9999"]`
# import re
#

# Done

li = ["+380971236789", "+380809123232", "99999x9999"]
code = '+380'
for numb in li:
    if code in numb:
        print(f'This number is valid - {numb}')
