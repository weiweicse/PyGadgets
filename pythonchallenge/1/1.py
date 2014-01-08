m = {}
for i in range(ord('a'), ord('z')+1):
    m[chr(i)] = chr(i+2)
m['y'] = 'a'
m['z'] = 'b'
s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

res = ''
for i in s:
    if i in m:
        res += m[i]
    else:
        res += i
print res
