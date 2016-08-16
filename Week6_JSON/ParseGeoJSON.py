import urllib
import json



url = 'http://maps.googleapis.com/maps/api/geocode/json?'

serviceurl = url + urllib.urlencode({'sensor': 'false', 'address': 'Masdar Institute' })
uh = urllib.urlopen(serviceurl)
# print uh


data = uh.read()


obj = json.loads(data)

# itemList = data['results']

result = obj['results']
# place_id = result['place_id']
print result