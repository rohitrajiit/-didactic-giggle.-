#! python3
#spwd.py strong password detection

import re
numofchar = re.compile(r'''([a-zA-Z0-9]{8,}                    #8 or more character
                         )''', re.VERBOSE)
uppercase = re.compile(r'''([A-Z]+                           #1 upper case character
                         )''', re.VERBOSE)
lowercase = re.compile(r'''([a-z]+                           #1 lower case character
                         )''', re.VERBOSE)
numchar   = re.compile(r'''([0-9]+                           #1 numeric character
                         )''', re.VERBOSE)

print ('Enter Password')
number =input()
if numofchar.search(number) == None:
 print("Weak Password ")
elif uppercase.search(number) == None:
 print('Weak Password')
elif lowercase.search(number) == None:
 print('Weak Password')
elif lowercase.search(number) == None:
 print('Weak Password')
else:
 print('Strong Password')
