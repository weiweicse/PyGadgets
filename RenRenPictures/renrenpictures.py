import urllib
import urllib2
import cookielib
import re
import json

def login(username, password):
    logpage = 'http://www.renren.com/ajaxLogin/login'
    data = {'email': username, 'password': password}
    login_data = urllib.urlencode(data)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    res = opener.open(logpage, login_data)
    print 'Login now ...'
    html = res.read()

    print 'Getting user id ...'
    res = urllib2.urlopen('http://www.renren.com/home')
    html = res.read()
    uid = re.search("'ruid':'(\d+)'", html).group(1)
    
    print 'Login and get uid successfully'
    print uid

def getPhotoID(userid):
    res = urllib2.urlopen('http://photo.renren.com/photo/' + userid + '/album-profile?curpage=0')
    html = res.read()
    info = re.findall(r'album:(\d+), photo:(\d+), owner:(\d+)', html)
    print 'Get information of album profile ...'
    albumid = info[0][0]
    photoid = info[0][1]
    print 'album: {0}, photo: {1}'.format(albumid, photoid)
    return photoid

def getAlbumID(userid, photoid):
    # get current album id
    res = urllib2.urlopen( \
            'http://photo.renren.com/photo/{0}/latest/photo-{1}' \
            .format(userid, photoid))
    html = res.read()
    # albumid = re.findall(r'a target="_blank" href="http://photo.renren.com/photo/(?:\d+)/album-(\d+)" id="photo-soure-album"', html)

    # get next photo and its album id
    photosJson = re.findall(r'_PCI.photosJson = (\{.*\})', html)[0]
    data = json.loads(photosJson)
    albumIDs = []
    for i in range(len(data['list'])):
        albumIDs.append(int(data['list'][i]['albumId']))
    return list(set(albumIDs))

if __name__ == '__main__':
    username = ''
    password = ''
    login(username, password)
    userid = ''
    photoid = getPhotoID(userid)
    albumIDs = getAlbumID(userid, photoid)
