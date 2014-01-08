MCM-STAT
========

Aim at creating a database that contains all the information about institutions and designations of MCM contests from the .pdf files available on the Internet. 

First, use pdf2txt.py to convert pdf to text files.

Then we can simply process the text and extract all the information from the text and insert it into a database (here we simply use sqlite3).

Every time we want to access the database, we should connect to it first.

1. connectDB()

We can use processText(filename) to process text files of MCM results with year 2008-2012.

The standard process of writing to database is:

1. writeToDB(stat)

Finally, we should close database:

1. closeDB()

The current version can deal with MCM 2008-2012 pretty well. However, when it comes to years before 2008, the text files converted from the pdf is a mess and I didn't find a way to fix it.
