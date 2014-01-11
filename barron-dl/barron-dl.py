# coding: utf-8
# download barron gre list from www.wordhacker.com/en/article/Barron_gre_list_{a-z}
import urllib2
import re
import sqlite3

url = 'http://www.wordhacker.com/en/article/Barron_gre_list_'
pages = []
for i in range(ord('a'), ord('z')+1):
    geturl = url + chr(i) + '.htm'
    print geturl
    pages.append(urllib2.urlopen(geturl).read())

print "finish downloading pages"

# process each page to extract information
gre_list = []
for page in pages:
    words = re.findall(r'<tr>\s*<td>\s*([a-z]+)\s*</td>\s*<td>\s*([^<]*)</td>\s*</tr>', page)
    gre_list += words

print "finish retrieving words"

# write to file
# f = open('gre_list.txt', 'w')
# for (w, e) in gre_list:
#     f.write(w)
#     f.write('\t')
#     f.write(e)
#     f.write('\n')
# f.close()

# write to database
# con = sqlite3.connect('barron.db')
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE Words(Id INT, Word TEXT, Note TEXT, Count INT)")
#     Id = 0
#     for (w, e) in gre_list:
#         cur.execute('INSERT INTO Words VALUES({0}, "{1}", "{2}", {3})'.format(Id, w, e, 0))
#         Id += 1
#     con.commit()

# using words.db
from wordsDB import *
engine = create_engine('sqlite:///words.db', echo=False)
Session = sessionmaker(bind=engine)
# create_DB(engine)
session = Session()

# add words to db
# import youdao
cnt = 0
for (w, e) in gre_list:
    cnt += 1
    print "#{0}: {1}".format(cnt, w)
    # yd = youdao.YoudaoFanyi(w)
    # add_word(Word(w, e, ''.join([explain + ' ' for explain in yd.explains]), yd.phonetic), session)
    add_word(Word(w, e), session)

session.commit()
