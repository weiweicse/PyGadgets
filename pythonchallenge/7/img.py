import Image

im = Image.open("oxygen.png")
out = ""
tp = None
count = 0
for i in range(im.getbbox()[2]):
    tmp = im.getpixel((i, im.getbbox()[3]/2))
    print tmp
    count += 1
    if count > 6:
        out += chr(tmp[0])
        count = 0
print out
