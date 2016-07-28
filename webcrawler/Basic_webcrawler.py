import urllib2
import re
from bs4 import BeautifulSoup

parseUrl = urllib2.urlopen('http://python-data.dr-chuck.net/comments_300262.html')

soup = BeautifulSoup(parseUrl,'html.parser')

#regular expression to extract integer value




#print(soup.prettify())

lists = soup.find_all('span')
sum = 0
for e in lists:
    num = str(e.string.encode('utf-8'))
    sum += int(num)


print sum



