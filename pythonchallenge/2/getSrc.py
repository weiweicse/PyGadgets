import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
src = response.read()
soup = BeautifulSoup(src)
print soup.prettify()
