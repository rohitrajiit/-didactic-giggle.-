#!python3
#Sentencematcher.py
import re
numobject = re.compile(r'''(^(Alice|Bob|Carol)               #Alice, Bob or Carol
                 \s                                          #space
             (eats|pets|throws)                              #eats, pets or throws
                 \s                                          #space
             (apples|cats|baseballs)                         #apples, cats or baseballs
             \.$                                             #sentence ends with a period
          )''', re.VERBOSE|re.I)

print ('Enter Sentence')
number =input()
if numobject.search(number) != None:
 print("match: " + numobject.search(number).group(0))
else:
 print('No match found')
