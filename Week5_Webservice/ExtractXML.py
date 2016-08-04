import urllib
import xml.etree.ElementTree as ET

#ref : https://docs.python.org/2/library/xml.etree.elementtree.html


url = 'http://python-data.dr-chuck.net/comments_300259.xml'

print 'Retrieving', url
uh = urllib.urlopen(url)

data = uh.read()
print data

root = ET.fromstring(data)
comments = root.find('comments')
sum = 0
for comment in comments.findall('comment'):
    #name = comment.find('name').text
    count = comment.find('count').text
    sum += int(count)
    #print name, count

print sum
