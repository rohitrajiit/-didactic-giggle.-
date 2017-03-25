#!python3
#Namematcher.py
import re
numobject = re.compile(r'''(^[A-Z][a-z]+                     #matches first name
                 \s                                          #space
             Nakamoto$                                       #matches number of more than 3 digits with number separator
          )''', re.VERBOSE)

print ('Enter Name')
number =input()
if numobject.search(number) != None:
 print("match: " + numobject.search(number).group(0))
else:
 print('No match found')
