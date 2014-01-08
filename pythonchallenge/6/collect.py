import zipfile
import re

def run(num):
    filename = num + ".txt"
    comments.append(zip.getinfo(filename).comment)
    cont = zip.read(filename)
    m = p.findall(cont)
    if m:
        for mi in m:
            run(mi)
        else:
            return
num = '90052'
comments = []
zip = zipfile.ZipFile("txt/channel.zip", "r")
p = re.compile('[0-9]+')
run(num)
print "".join(comments)
