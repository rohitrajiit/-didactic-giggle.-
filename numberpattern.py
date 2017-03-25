#!python3
#pattern matching for numbering for numbers with comma separator after every 3 digits
import re

numobject = re.compile(r'''(^\d{1,3}$                     #matches number of 1-3 digits without comma
             |^(\d{1,3}[,])?(\d{3}[,])*(\d{3})$          #matches number of more than 3 digits with number separator
          )''', re.VERBOSE)
print ('Enter Number')
number =input()
if numobject.search(number) != None:
 print("match: " + numobject.search(number).group(0))
else:
 print('No match found')
