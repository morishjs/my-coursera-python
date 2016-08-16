import json
import urllib


url = 'http://python-data.dr-chuck.net/comments_300263.json'
uh = urllib.urlopen(url)
data = uh.read()
# print data

info = json.loads(data)
# print info
sum = 0
objectList = info['comments']
for item in objectList:
    sum += item['count']


print sum

