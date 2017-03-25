#! Python3
#  Regexsearch.py
import re,os, pprint
print('enter folder path')
path = input()
print('enter expression to search')
pattern = input()
pattern1= re.compile(pattern)
output =[]
for filename in os.listdir(path):
  if '.py' in filename:
   filepath =os.path.join(path,filename)
   fileid = open(filepath)
   text = fileid.read()
   fileid.close()
   if pattern1.search(text) != None:
     output.append(pattern1.findall(text))

print (pprint.pformat(output))
