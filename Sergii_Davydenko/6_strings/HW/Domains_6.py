# Return list of domains from list of emails.
import re


emails = ['svvay@ukr.net', 'abrahim@gmail.com', 'jordan@tutanota.com']

for email in emails:
    for index, dom in enumerate(email):
        dog = '@'
        if dog in dom:
                print(email[index:])
