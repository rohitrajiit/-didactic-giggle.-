import urllib
from BeautifulSoup import *

url = raw_input('Enter url- ')
count = raw_input('Enter count- ')
position = raw_input('Enter position- ')
for j in range(0,int(count)):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	# Retrieve all of the anchor tags
	tags = soup('a')
	i=0
	for tag in tags:
		if i == int(position)-1:
		 url = tag.get('href')
		 name = tag.getText()
		 print name, i, j
		 break
		i+=1
