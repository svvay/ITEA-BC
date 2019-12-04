# 7. Get date from string

import re
my_string2 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
pattern = r'\d{2}-\d{2}-\d{4}'
# pattern = r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[01][0-9])(?!\d)'
result = re.findall(pattern, my_string2)
print(result)

