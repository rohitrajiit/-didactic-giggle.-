#!python3
#Search for occurence of Noun or Adverb or Adjective and asks for replacement string Pg 195
import re
print('Enter String')
text =input()
pattern = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')

while pattern.search(text)!=None:
  match = pattern.search(text).group()
  print('Enter an ' + match)
  sub = input()
  text = pattern.sub(sub,text, count=1)

print (text)

output= open('output.txt','w')
output.write(text)
output.close()
