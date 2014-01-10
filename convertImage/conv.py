import os

cnt = 1
for filename in os.listdir('.'):
    if '2014' in filename:
        print filename
        os.system("convert -size 300x400 " + filename.replace(" ", "\\ ") + " -resize 300x400 " + str(cnt)  + ".jpg")
        cnt += 1
