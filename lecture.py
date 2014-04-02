#!/usr/bin/python

import sqlite3

f = open('Dictionnaire.txt','r')
lignes  = f.readlines()
f.close()

conn = sqlite3.connect('dico.db')
print "Opened database successfully";
c = conn.cursor()
c.execute('''create table Mots(Id integer primary key autoincrement, Mot varchar(26));''')
print "Table created successfully";




for ligne in lignes:
    c.execute("insert into Mots (Mot) values ("+"\'"+ligne+"\'"+")");
    
print "Records created successfully";
conn.commit()
c.close()