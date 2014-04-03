#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('dico.db')
print "Opened database successfully";
c = conn.cursor()
mot='mange'
c.execute("SELECT * FROM Mots where Mot like "+"\'"+mot+"_"+"\'"+";")
r=c.fetchall()

for i in r:
    print i[0][0:len(i[0])-1];

conn.commit()
c.close()