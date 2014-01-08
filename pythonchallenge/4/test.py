import urllib2
import re
from bs4 import BeautifulSoup
text = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read()
print text

# nothing = '12345'
nothing = '8022'
while 1:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
    print "url: " + url
    text = urllib2.urlopen(url).read()
    print "get: " + text
    nothing = re.findall("is ([0-9]*)$", text)
    nothing = nothing[0]
    print "nothing: " + nothing
