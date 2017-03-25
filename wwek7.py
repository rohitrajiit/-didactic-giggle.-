import urllib
import json

#url = 'http://python-data.dr-chuck.net/comments_42.json'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : 
	  break
	url= address
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'
	print data
	input= data
	info = json.loads(input)
	print 'User count:', len(info['comments'])
	sum =0
	for item in info['comments']:
		print 'Name', item['name']
		print 'count', item['count']
		sum +=int(item['count'])
	print sum
