# download .pdf files
# www.comap.com/undergraduate/contests/mcm/contests/2012/results/
# query 2004 - 2012

from threading import Thread, Lock
import urllib
from bs4 import BeautifulSoup

# 2008 - 2012
# www.comap.com/undergraduate/contests/mcm/contests/2012/results/2012_MCM_Problem_A_Results.pdf

# 2000 - 2003
# mcm.php
# icm.php

url = 'http://www.comap.com/undergraduate/contests/mcm/contests/'

for year in [2008, 2010, 2012]:
    u = url + str(year) + '/results/'
    # mcm
    umcm = u
    print umcm
    text = urllib.urlopen(umcm).read()
    soup = BeautifulSoup(text)
    # get links that contains .pdf
    a = soup.findAll('a')
    link = []
    for i in a:
        if ".pdf" in str(i):
            link.append(i.get('href'))
    # download all links
    cnt = 1
    for l in link:
        fn = str(year) + '-' + str(cnt) + '.pdf'
        filename, msg = urllib.urlretrieve(u+l, fn)
        cnt += 1
