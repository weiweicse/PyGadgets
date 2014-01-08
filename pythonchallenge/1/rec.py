import string
frm = 'abcdefghijklmnopqrstuvwxyz'
to = 'cdefghijklmnopqrstuvwxyzab'
trans_table = string.maketrans(frm, to)
src = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
res = src.translate(trans_table)
print res
res = 'http://www.pythonchallenge.com/pc/def/map.html'.translate(trans_table)
print res
