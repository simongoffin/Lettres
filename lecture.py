#!/usr/bin/python

import sqlite3

f = open('Dictionnaire.txt','r')
lignes  = f.readlines()
f.close()

conn = sqlite3.connect('dico.db')
print "Opened database successfully";
c = conn.cursor()
c.execute('''create table Mots(Mot varchar(9) primary key);''')
print "Table created successfully";



doublons=set(lignes)
for ligne in doublons:
    taille=len(ligne)
    if taille<=10:
        ligne=ligne[0:taille-1]
        print ligne
        c.execute("insert into Mots (Mot) values ("+"\'"+ligne+"\'"+")");
print "Records created successfully";
conn.commit()
c.close()