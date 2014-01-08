from ftplib import FTP
import os
ftp = FTP('202.120.38.171')
ftp.login('job', 'seiee')

listing = []
ftp.retrlines('LIST', listing.append)
words = listing[1].split(None, 8)
dirname = words[-1].lstrip()

ftp.cwd(dirname)

listing = []
ftp.retrlines('LIST', listing.append)
for i in listing:
    words = i.split(None, 8)
    dirname = words[-1].lstrip()
    if '09' in dirname:
        break
ftp.cwd(dirname)

listing = []
ftp.retrlines('LIST', listing.append)

path = os.getcwd() + '/' + 'download/'
for i in listing:
    i = i.split(None, 8)[-1].lstrip()
    if i == '.' or i == '..':
        continue
    print i
    lfn = path + i
    lf = open(lfn, 'wb')
    ftp.retrbinary("RETR" + i, lf.write, 8*1024)
    lf.close()
