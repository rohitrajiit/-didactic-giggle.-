name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()

handle.close()
counter={}
line = text.split('\n')
for lines in line:
  if 'From ' in lines:
    words = lines.split()
    counter[words[1]]= counter.setdefault(words[1],0)+1

max = None
maxkey = None
for key in counter:
 if counter[key] > max:
    max = counter[key]
    maxkey =key
print(maxkey + ' '+ str(max))
