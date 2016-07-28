import urllib2
import re
from bs4 import BeautifulSoup


prefix = "http://python-data.dr-chuck.net/known_by_"
suffix = ".html"
pos = 18
count = 7
name = "Seane"


def parseURL(name):
    parseUrl = urllib2.urlopen(prefix + name + suffix)
    soup = BeautifulSoup(parseUrl, 'html.parser')
    lists = soup.find_all('a')
    tag = lists.pop(pos-1)
    name = str(tag.string.encode('utf-8'))
    print name
    return name
#init setting



for i in range(0,count):
    name = parseURL(name)





