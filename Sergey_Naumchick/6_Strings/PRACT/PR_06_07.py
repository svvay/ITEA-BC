'''    `string = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'`
7. Get date from string
    '''
import re


def find_date(my_string):
    temp = re.findall(r'\d\d.\d\d.\d{4}', my_string)
    print(temp)
    return temp
