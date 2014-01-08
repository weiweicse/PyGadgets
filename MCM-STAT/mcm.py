#! /usr/bin/python
import pickle
import sys
import sqlite3

c = 0
conn = 0

def processText(filename):
    year = range(2000, 2013)
    year = [str(i) for i in year]
    stat = []
    with open(filename, "r") as f:
        text = f.read()
        cnt = 0
        result = []

        # get pages
        pages = text.split('\x0c')
        pages = pages[1:] # the first page is useless
        del pages[pages.index('')]

        # process each page
        for page in pages:
            cnt += 1
            print "Page#: ", cnt
            p = page.split('\n')
            p = [i for i in p if i != '']
            # del year
            for i in p:
                if i in year:
                    mcmyear = i
                    del p[p.index(i)]
                    break

            # get institutions
            univ = [p[p.index(i)+1] for i in p if i.isdigit()]
            # print "Univ#", len(univ), univ

            # get problem
            # prob = []
            # if 'A' in p:
            #     prob = ['A'] * len(univ)
            # elif 'B' in p:
            #     prob = ['B'] * len(univ)
            # elif 'C' in p:
            #     prob = ['C'] * len(univ)
            # print "Prob#", len(prob), prob
            prob = []
            for i in p:
                 if i == 'A' or i == 'B' or i == 'C':
                     prob.append(i)

            if len(prob) != len(univ):
                print "#### Warning:", cnt, "####"
                if 'A' in p:
                    prob = ['A'] * len(univ)
                elif 'B' in p:
                    prob = ['B'] * len(univ)
                elif 'C' in p:
                    prob = ['C'] * len(univ)

            # get designation
            designation = []
            for i in p:
                if i == 'Meritorious Winner' or i == 'Outstanding Winner' or i == 'Finalist' or i == 'Honorable Mention' or i == 'Successful Participant' or i == 'Unsuccessful':
                    designation.append(i)
            # print "Designation#", len(designation), designation

            # check
            if len(prob) == len(designation) and len(designation) == len(univ):
                for (i, j, k) in zip(univ, prob, designation):
                    result.append((unicode(i, 'UTF-8'), unicode(j, 'UTF-8'), unicode(mcmyear, 'UTF-8'), unicode(k, 'UTF-8')))
            else:
                print "Error: page number is:" + str(cnt)
                print p
                print univ
                print prob
                print designation
        # print result
        return result
        
def transDict(result):
# process each univ
    stat = {}
    for r in result:
        for z in r:
            if z[0] not in stat:
                stat[z[0]] = []
            stat[z[0]].append(z[3])
    return stat

def readFromDisk(filename):
    with open(filename, 'r') as f:
        stat = pickle.load(f)
        return stat
    return False

def writeToDisk(stat, filename):
# write to hard disk
    with open(filename, 'w') as f:
        pickle.dump(stat, f)

def connectDB():
    global conn
    global c
    conn = sqlite3.connect('mcm.db')
    c = conn.cursor()

def createDB():
# create a database
    c.execute('''CREATE TABLE mcm
                (univ text, problem text, year text, desig text)''')
    conn.commit()

# table is a dict!
def writeToDB(stat):
    c.executemany("INSERT INTO mcm VALUES (?, ?, ?, ?)", stat)
    conn.commit()

# query univ
def queryUniv(univ):
    for row in c.execute("SELECT * FROM mcm WHERE univ = '%s'" % univ):
        print row

def closeDB():
    conn.close()

if __name__ == '__main__':
    # stat = processText('TXT/2012-A.txt')
    connectDB()
    # createDB()
    # writeToDB(stat)
    for row in c.execute("SELECT * FROM mcm"):
        print row
    queryUniv("Peking University")
    closeDB()
