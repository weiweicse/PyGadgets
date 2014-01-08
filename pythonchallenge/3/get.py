import urllib2
from bs4 import BeautifulSoup
text = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
soup = BeautifulSoup(text)
print soup.prettify()

