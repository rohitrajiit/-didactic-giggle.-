#! python3
# Regexstrip.py - Removes whitespace from beginning or end of string, if no parameter is specified otherwise removes character in #parmenter
import sys, re

pattern = r'((^\s+)|(\s+$))'
if len(sys.argv)==2:
 if sys.argv[1] != None:
  pattern = sys.argv[1]

print('Enter String')
text = input()
pattern = re.compile(pattern)
output = pattern.sub('',text)
print('Output: '+ output)
