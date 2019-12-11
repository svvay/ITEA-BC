import re

li = ["+380971236789", "+380809123232", "99999x9999"]

for val in li:
    if re.match(r"^\+?3?8?(0[5-9][0-9]\d{7})$", val):
        print("yes")
    else:
        print("no")
