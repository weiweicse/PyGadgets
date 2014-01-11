# get photo of the day from national geographic
import urllib, urllib2
import re

class NGPOD:
    def __init__(self):
        "Init"
        # self.getPage()
        # self.getImage('./Images/')
    def getPage(self):
        "Get Page From National Geographic"
        url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
        page = urllib2.urlopen(url)
        self.page = page.read()
        print "OPEN URL:", url, '...'
    def getImage(self, path):
        "Using RegExp"
        self.imageURL = 'http:' + re.findall(r'<div class="primary_photo">\s*<a href="[^"]*" title="[^"]*">\s*<img src="([^"]*)"', self.page)[0]
        print self.imageURL
        # self.imageURL = self.imageURL.replace('990x742','360x270') # get small picture
        self.imagePath = path + self.imageURL.split('/')[-1]
        "Save Image"
        f = open(self.imagePath, 'wb')
        f.write(urllib.urlopen(self.imageURL).read())
        f.close()
        print "WRITE TO FILE:", self.imagePath, '...'
    def getImageInfo(self):
        """Use BeautifulSoup to extract caption and note

        BeautifulSoup is really powerful

        """
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(self.page)
        self.imageCaption = soup.find(id="caption").h2.text
        self.imageNote = soup.find(id="caption").find_all('p')[3].text

        # it works using the following regexp
        # it utilizes (?= ...), really powerful!
        # re.findall(r'<div id="caption">\s*<p class="publication_time">[^<]*</p>\s*<h2>([^<]*)</h2>\s*<p class="credit">.*(?=/p>)/p>\s*<p>.*(?=/p>)/p>\s*<p>(.*)(?=/p>)', self.page)


if __name__ == '__main__':
    photo = NGPOD()
    photo.getPage()
    photo.getImage('./Images/')
    photo.getImageInfo()
    print photo.imageCaption
    print photo.imageNote
