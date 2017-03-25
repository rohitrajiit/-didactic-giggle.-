import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'


address = raw_input('Enter location: ')
#if len(address) < 1 : break

#url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)


results = tree.findall('.//count')
print 'Count:', len(results)
sum=0
for result in results:
 sum = sum + int(result.text)

print 'Sum:',sum
