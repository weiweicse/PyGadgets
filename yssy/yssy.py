# login to bbs.sjtu.edu.cn
import urllib2
from bs4 import BeautifulSoup
from urllib import urlencode
import requests
import cookielib
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import datetime
import sched, time
import re

class yssy:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        register_openers()

        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(self.opener)

    def login(self):
        req = urllib2.Request('http://bbs.sjtu.edu.cn')
        r = urllib2.urlopen(req)
        #html = r.read()
        #soup = BeautifulSoup(html)
        #print soup.prettify()

        url = 'https://bbs.sjtu.edu.cn/bbslogin'
        headers = {'Connection': 'keep-alive', 'Origin': 'https://bbs.sjtu.edu.cn', 'Referer': 'https://bbs.sjtu.edu.cn/file/bbs/index/index.htm', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31'
}
        params = {
            'id': self.username,
            'pw': self.password,
            'submit': 'login',
        }
        #print urlencode(params)
        req = urllib2.Request(url, data = urlencode(params), headers=headers)
        r = urllib2.urlopen(req)
        #html = r.read()
        #soup = BeautifulSoup(html)
        #print soup.prettify()

    #url = 'https://bbs.sjtu.edu.cn/html/attach.html'
    #url = 'https://bbs.sjtu.edu.cn/bbsdoc?board=CS'
    def get(self, url):
        r = urllib2.urlopen(url)
        soup = BeautifulSoup(r)
        #print soup.prettify()

    #url = 'https://bbs.sjtu.edu.cn/bbsupload?board=CS'
    def uploadFile(self, board, filename):
        url = 'https://bbs.sjtu.edu.cn/bbsupload?board=' + board
        self.get(url)
        url = 'https://bbs.sjtu.edu.cn/bbsdoupload'
        datagen, headers = multipart_encode({
            'up': open(filename, 'rb'),
            'MAX_FILE_SIZE': '1048577',
            'board': board,
            'level': '0',
            'exp': ' ',
            'live': '180',
        })
        #print datagen, headers
        req = urllib2.Request(url, data="".join(datagen), headers=headers)
        r = urllib2.urlopen(req)
        soup = BeautifulSoup(r)
        print soup.findAll('font')[0].string.strip()

    def postAtTime(self, h, m, board, title, text, sig=1):
        #t = str(datetime.now())
        #m = re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2} ([0-9]{2}):([0-9]{2}):([0-9]{2}\.[0-9]{6})', t)
        s = sched.scheduler(time.time, time.sleep)
        t1 = datetime.datetime.now()
        t2 = datetime.datetime(t1.year, t1.month, t1.day, h, m, 0, 0)
        td = str(t2-t1).split(':')
        print td[1], td[2]
        wait = int(td[1]) * 60 + float(td[2])
        s.enter(wait, 10, self.postText, (board, title, text, sig))
        s.run()
    
    def postText(self, board, title, text, sig=1):
        self.get('https://bbs.sjtu.edu.cn/bbsdoc?board='+board)
        self.get('https://bbs.sjtu.edu.cn/html/attach.html')
        url = 'https://bbs.sjtu.edu.cn/bbssnd'
        datagen, headers = multipart_encode({
            'board': board,
            'file': ' ',
            'reidstr': ' ',
            'reply_to_user': ' ',
            'title': title,
            'signature': sig,
            'autocr': 'on',
            'text': text,
            'up': ' ',
            'MAX_FILE_SIZE': '1048577',
            'board': board,
            'level': '0',
            'live': '180',
            'exp': ' ',
        })
        headers['Referer'] = 'https://bbs.sjtu.edu.cn/bbspst?board=' + board
        headers['Origin'] = 'https://bbs.sjtu.edu.cn'
        req = urllib2.Request(url, data="".join(datagen), headers=headers)
        r = urllib2.urlopen(req)
        print "Post Success at " + str(datetime.datetime.now())
        #soup = BeautifulSoup(r)
        #print soup.prettify()

# enter username and password here
x = yssy('username', 'pwd')
x.login()
#x.uploadFile('test', '/Users/weiwei/Dropbox/Photos/How to use the Photos folder.txt')
#x.postText('test', 'title', 'text')
#x.postAtTime(21, 25, 'test', 'at 9:25', 'asdf')
